"""Tests for scan-config.json validation."""

import json
import tempfile
import unittest
from pathlib import Path

from assess.scan_config import load_scan_config


class TestLoadScanConfig(unittest.TestCase):

    def _write_config(self, config):
        """Write config dict to a temp file, return path."""
        f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        json.dump(config, f)
        f.close()
        return f.name

    def test_valid_all_mode(self):
        path = self._write_config({
            "orgs": {
                "opendatahub-io": {
                    "description": "Core",
                    "mode": "all",
                    "exclude": []
                }
            }
        })
        config = load_scan_config(path)
        self.assertEqual(config["orgs"]["opendatahub-io"]["mode"], "all")

    def test_valid_include_mode(self):
        path = self._write_config({
            "orgs": {
                "project-codeflare": {
                    "description": "CodeFlare",
                    "mode": "include",
                    "repos": ["codeflare-sdk"]
                }
            }
        })
        config = load_scan_config(path)
        self.assertEqual(config["orgs"]["project-codeflare"]["repos"], ["codeflare-sdk"])

    def test_empty_orgs_raises(self):
        path = self._write_config({"orgs": {}})
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_missing_orgs_key_raises(self):
        path = self._write_config({"something": "else"})
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_invalid_mode_raises(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "selective", "repos": ["a"]}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_include_mode_empty_repos_raises(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "include", "repos": []}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_include_mode_missing_repos_raises(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "include"}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_all_mode_with_repos_key_raises(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "all", "repos": ["a"]}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_include_mode_with_exclude_key_raises(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "include", "repos": ["a"], "exclude": ["b"]}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_repo_name_with_slash_raises(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "include", "repos": ["org/repo"]}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_invalid_org_name_raises(self):
        path = self._write_config({
            "orgs": {"my org!": {"mode": "all"}}
        })
        with self.assertRaises(ValueError):
            load_scan_config(path)

    def test_all_mode_exclude_defaults_empty(self):
        path = self._write_config({
            "orgs": {"my-org": {"mode": "all"}}
        })
        config = load_scan_config(path)
        self.assertEqual(config["orgs"]["my-org"].get("exclude", []), [])

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            load_scan_config("/nonexistent/scan-config.json")

    def test_multi_org_config(self):
        path = self._write_config({
            "orgs": {
                "opendatahub-io": {"mode": "all", "exclude": ["archived-repo"]},
                "project-codeflare": {"mode": "include", "repos": ["codeflare-sdk"]}
            }
        })
        config = load_scan_config(path)
        self.assertEqual(len(config["orgs"]), 2)
        self.assertEqual(config["orgs"]["opendatahub-io"]["exclude"], ["archived-repo"])


if __name__ == "__main__":
    unittest.main()
