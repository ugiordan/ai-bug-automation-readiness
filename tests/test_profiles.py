# tests/test_profiles.py
import json
import os
import tempfile
import unittest

from assess.profiles import load_central_profiles, resolve_profile


class TestLoadCentralProfiles(unittest.TestCase):
    """Tests for loading central profiles configuration."""

    def test_loads_builtin_profiles(self) -> None:
        """Verify built-in profiles are loaded correctly."""
        data = load_central_profiles()
        self.assertIn("default", data["profiles"])
        self.assertIn("test-repo", data["profiles"])
        self.assertEqual(data["profiles"]["default"]["exclude"], [])

    def test_missing_file_returns_defaults(self) -> None:
        """Verify missing profiles.json returns default configuration."""
        data = load_central_profiles(path="/nonexistent/profiles.json")
        self.assertIn("default", data["profiles"])
        self.assertEqual(data["profiles"]["default"]["exclude"], [])


class TestResolveProfile(unittest.TestCase):
    """Tests for profile resolution logic with repo overrides."""

    def setUp(self) -> None:
        """Create temporary directory for test repos."""
        self.tmp = tempfile.mkdtemp()
        self.repo_path = os.path.join(self.tmp, "my-repo")
        os.makedirs(self.repo_path)

    def test_default_profile_no_config(self) -> None:
        """Verify default profile is used when no config exists."""
        result = resolve_profile(self.repo_path)
        self.assertEqual(result.name, "default")
        self.assertEqual(result.excluded_checks, frozenset())
        self.assertEqual(result.source, "default")

    def test_repo_override_in_profiles_json(self) -> None:
        """Verify repo-specific profile override from profiles.json."""
        profiles = {
            "profiles": {
                "default": {"description": "all", "exclude": []},
                "test-repo": {"description": "test", "exclude": ["coverage_config", "test_ratio", "test_isolation"]},
            },
            "repos": {"my-repo": {"profile": "test-repo"}},
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.name, "test-repo")
        self.assertEqual(result.excluded_checks, frozenset({"coverage_config", "test_ratio", "test_isolation"}))
        self.assertEqual(result.source, "profiles.json")
        os.unlink(cfg_path)

    def test_exclude_also_adds_to_profile(self) -> None:
        """Verify exclude_also adds checks to profile exclusions."""
        profiles = {
            "profiles": {
                "default": {"description": "all", "exclude": []},
                "test-repo": {"description": "test", "exclude": ["coverage_config"]},
            },
            "repos": {
                "my-repo": {"profile": "test-repo", "exclude_also": ["fixture_data"], "reason": "no fixtures needed"}
            },
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.excluded_checks, frozenset({"coverage_config", "fixture_data"}))
        os.unlink(cfg_path)

    def test_include_back_removes_from_profile(self) -> None:
        """Verify include_back removes checks from profile exclusions."""
        profiles = {
            "profiles": {
                "default": {"description": "all", "exclude": []},
                "test-repo": {"description": "test", "exclude": ["coverage_config", "test_ratio", "test_isolation"]},
            },
            "repos": {"my-repo": {"profile": "test-repo", "include_back": ["test_ratio"]}},
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.excluded_checks, frozenset({"coverage_config", "test_isolation"}))
        os.unlink(cfg_path)

    def test_cli_profile_overrides_json(self) -> None:
        """Verify CLI profile argument overrides profiles.json."""
        result = resolve_profile(self.repo_path, cli_profile="test-repo")
        self.assertEqual(result.name, "test-repo")
        self.assertEqual(result.source, "cli")

    def test_cli_exclude_checks_additive(self) -> None:
        """Verify CLI exclude checks are additive to profile exclusions."""
        result = resolve_profile(self.repo_path, cli_exclude_checks=["coverage_config"])
        self.assertIn("coverage_config", result.excluded_checks)
        self.assertEqual(result.source, "cli")

    def test_unknown_check_id_warns(self) -> None:
        """Verify unknown check IDs are silently dropped with stderr warning."""
        result = resolve_profile(self.repo_path, cli_exclude_checks=["nonexistent_check"])
        self.assertEqual(result.excluded_checks, frozenset())

    def test_cannot_exclude_all_checks(self) -> None:
        """Verify excluding all checks raises SystemExit."""
        from assess.config import CHECKS

        all_ids = list(CHECKS.keys())
        with self.assertRaises(SystemExit):
            resolve_profile(self.repo_path, cli_exclude_checks=all_ids)

    def test_cannot_exclude_all_checks_in_category(self) -> None:
        """Verify excluding all checks in a category raises SystemExit (Rule 8)."""
        verify_checks = [
            "test_ratio",
            "test_execution",
            "coverage_config",
            "ci_runs_tests",
            "test_isolation",
            "precommit_hooks",
        ]
        with self.assertRaises(SystemExit):
            resolve_profile(self.repo_path, cli_exclude_checks=verify_checks)

    def test_max_5_exclusions(self) -> None:
        """Verify max 5 checks can be excluded per repo (Rule 9)."""
        six_checks = [
            "coverage_config",
            "test_ratio",
            "test_isolation",
            "fixture_data",
            "generated_code",
            "dependency_complexity",
        ]
        with self.assertRaises(SystemExit):
            resolve_profile(self.repo_path, cli_exclude_checks=six_checks)

    def test_unknown_profile_falls_back_to_default(self) -> None:
        """Verify unknown profile name falls back to default."""
        result = resolve_profile(self.repo_path, cli_profile="nonexistent")
        self.assertEqual(result.name, "default")

    def test_no_profile_key_uses_default(self) -> None:
        """Verify repo entry without profile key gets default (Rule 7)."""
        profiles = {
            "profiles": {"default": {"description": "all", "exclude": []}},
            "repos": {"my-repo": {"exclude_also": ["coverage_config"], "reason": "test"}},
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.name, "default")
        self.assertIn("coverage_config", result.excluded_checks)
        os.unlink(cfg_path)


class TestOrgRepoLookup(unittest.TestCase):
    """Tests for org/repo qualified name lookup in profiles."""

    def setUp(self) -> None:
        """Create temporary directory for test repos."""
        self.tmp = tempfile.mkdtemp()
        self.repo_path = os.path.join(self.tmp, "codeflare-sdk")
        os.makedirs(self.repo_path)

    def _write_profiles(self, data: dict) -> str:
        path = os.path.join(self.tmp, "profiles.json")
        with open(path, "w") as f:
            json.dump(data, f)
        return path

    def test_qualified_name_takes_priority(self) -> None:
        """Verify qualified org/repo key takes priority over bare repo key."""
        path = self._write_profiles(
            {
                "profiles": {
                    "default": {"description": "All checks", "exclude": []},
                    "test-repo": {
                        "description": "Test",
                        "exclude": ["coverage_config", "test_ratio", "test_isolation"],
                    },
                },
                "repos": {
                    "codeflare-sdk": {"profile": "default"},
                    "project-codeflare/codeflare-sdk": {"profile": "test-repo"},
                },
            }
        )
        result = resolve_profile(self.repo_path, central_path=path, org="project-codeflare")
        self.assertEqual(result.name, "test-repo")

    def test_bare_name_fallback_when_no_qualified(self) -> None:
        """Verify fallback to bare repo key when no qualified key exists."""
        path = self._write_profiles(
            {
                "profiles": {
                    "default": {"description": "All checks", "exclude": []},
                    "test-repo": {
                        "description": "Test",
                        "exclude": ["coverage_config", "test_ratio", "test_isolation"],
                    },
                },
                "repos": {"codeflare-sdk": {"profile": "test-repo"}},
            }
        )
        result = resolve_profile(self.repo_path, central_path=path, org="project-codeflare")
        self.assertEqual(result.name, "test-repo")

    def test_no_org_uses_bare_name(self) -> None:
        """Verify bare name lookup is used when org param is not provided."""
        path = self._write_profiles(
            {
                "profiles": {
                    "default": {"description": "All checks", "exclude": []},
                    "test-repo": {
                        "description": "Test",
                        "exclude": ["coverage_config", "test_ratio", "test_isolation"],
                    },
                },
                "repos": {"codeflare-sdk": {"profile": "test-repo"}},
            }
        )
        result = resolve_profile(self.repo_path, central_path=path)
        self.assertEqual(result.name, "test-repo")


if __name__ == "__main__":
    unittest.main()
