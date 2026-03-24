# tests/test_profiles.py
import json
import os
import tempfile
import unittest
from pathlib import Path

from assess.profiles import resolve_profile, load_central_profiles, ResolvedProfile


class TestLoadCentralProfiles(unittest.TestCase):
    def test_loads_builtin_profiles(self):
        data = load_central_profiles()
        self.assertIn("default", data["profiles"])
        self.assertIn("test-repo", data["profiles"])
        self.assertEqual(data["profiles"]["default"]["exclude"], [])

    def test_missing_file_returns_defaults(self):
        data = load_central_profiles(path="/nonexistent/profiles.json")
        self.assertIn("default", data["profiles"])
        self.assertEqual(data["profiles"]["default"]["exclude"], [])


class TestResolveProfile(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.repo_path = os.path.join(self.tmp, "my-repo")
        os.makedirs(self.repo_path)

    def test_default_profile_no_config(self):
        result = resolve_profile(self.repo_path)
        self.assertEqual(result.name, "default")
        self.assertEqual(result.excluded_checks, frozenset())
        self.assertEqual(result.source, "default")

    def test_repo_override_in_profiles_json(self):
        profiles = {
            "profiles": {
                "default": {"description": "all", "exclude": []},
                "test-repo": {"description": "test", "exclude": ["coverage_config", "test_ratio", "test_isolation"]},
            },
            "repos": {
                "my-repo": {"profile": "test-repo"}
            }
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.name, "test-repo")
        self.assertEqual(result.excluded_checks, frozenset({"coverage_config", "test_ratio", "test_isolation"}))
        self.assertEqual(result.source, "profiles.json")
        os.unlink(cfg_path)

    def test_exclude_also_adds_to_profile(self):
        profiles = {
            "profiles": {
                "default": {"description": "all", "exclude": []},
                "test-repo": {"description": "test", "exclude": ["coverage_config"]},
            },
            "repos": {
                "my-repo": {
                    "profile": "test-repo",
                    "exclude_also": ["fixture_data"],
                    "reason": "no fixtures needed"
                }
            }
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.excluded_checks, frozenset({"coverage_config", "fixture_data"}))
        os.unlink(cfg_path)

    def test_include_back_removes_from_profile(self):
        profiles = {
            "profiles": {
                "default": {"description": "all", "exclude": []},
                "test-repo": {"description": "test", "exclude": ["coverage_config", "test_ratio", "test_isolation"]},
            },
            "repos": {
                "my-repo": {
                    "profile": "test-repo",
                    "include_back": ["test_ratio"]
                }
            }
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.excluded_checks, frozenset({"coverage_config", "test_isolation"}))
        os.unlink(cfg_path)

    def test_cli_profile_overrides_json(self):
        result = resolve_profile(self.repo_path, cli_profile="test-repo")
        self.assertEqual(result.name, "test-repo")
        self.assertEqual(result.source, "cli")

    def test_cli_exclude_checks_additive(self):
        result = resolve_profile(self.repo_path, cli_exclude_checks=["coverage_config"])
        self.assertIn("coverage_config", result.excluded_checks)
        self.assertEqual(result.source, "cli")

    def test_unknown_check_id_warns(self):
        """Unknown check IDs should be silently dropped (with stderr warning)."""
        result = resolve_profile(self.repo_path, cli_exclude_checks=["nonexistent_check"])
        self.assertEqual(result.excluded_checks, frozenset())

    def test_cannot_exclude_all_checks(self):
        from assess.config import CHECKS
        all_ids = list(CHECKS.keys())
        with self.assertRaises(SystemExit):
            resolve_profile(self.repo_path, cli_exclude_checks=all_ids)

    def test_cannot_exclude_all_checks_in_category(self):
        """Rule 8: cannot exclude all checks in any single category."""
        verify_checks = ["test_ratio", "test_execution", "coverage_config",
                         "ci_runs_tests", "test_isolation", "precommit_hooks"]
        with self.assertRaises(SystemExit):
            resolve_profile(self.repo_path, cli_exclude_checks=verify_checks)

    def test_max_5_exclusions(self):
        """Rule 9: max 5 checks excludable per repo."""
        six_checks = ["coverage_config", "test_ratio", "test_isolation",
                      "fixture_data", "generated_code", "dependency_complexity"]
        with self.assertRaises(SystemExit):
            resolve_profile(self.repo_path, cli_exclude_checks=six_checks)

    def test_unknown_profile_falls_back_to_default(self):
        result = resolve_profile(self.repo_path, cli_profile="nonexistent")
        self.assertEqual(result.name, "default")

    def test_no_profile_key_uses_default(self):
        """Rule 7: repo entry without profile key gets default."""
        profiles = {
            "profiles": {"default": {"description": "all", "exclude": []}},
            "repos": {
                "my-repo": {
                    "exclude_also": ["coverage_config"],
                    "reason": "test"
                }
            }
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(profiles, f)
            cfg_path = f.name
        result = resolve_profile(self.repo_path, central_path=cfg_path)
        self.assertEqual(result.name, "default")
        self.assertIn("coverage_config", result.excluded_checks)
        os.unlink(cfg_path)


if __name__ == "__main__":
    unittest.main()
