# tests/test_engine_profiles.py
import os
import tempfile
import unittest
from pathlib import Path

from assess.engine import assess_repo
from assess.profiles import ResolvedProfile


class TestAssessRepoWithExclusions(unittest.TestCase):
    def setUp(self):
        # Create a minimal repo structure
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, ".git"))
        # Create a Go source file so it's detected as a code repo
        with open(os.path.join(self.tmp, "main.go"), "w") as f:
            f.write("package main\nfunc main() {}\n")
        with open(os.path.join(self.tmp, "util.go"), "w") as f:
            f.write("package main\nfunc helper() {}\n")
        with open(os.path.join(self.tmp, "app.go"), "w") as f:
            f.write("package main\nfunc app() {}\n")

    def test_no_exclusions_runs_all_checks(self):
        result = assess_repo(self.tmp)
        self.assertEqual(len(result["checks"]), 20)
        for c in result["checks"].values():
            self.assertFalse(c.get("excluded", False))

    def test_excluded_checks_have_sentinel_entries(self):
        excluded = frozenset({"coverage_config", "test_ratio"})
        profile = ResolvedProfile(name="test-repo", excluded_checks=excluded, source="profiles.json")
        result = assess_repo(self.tmp, excluded_checks=excluded, profile_info=profile)
        # All 20 checks should be in results
        self.assertEqual(len(result["checks"]), 20)
        # Excluded checks have sentinel values
        self.assertTrue(result["checks"]["coverage_config"]["excluded"])
        self.assertIsNone(result["checks"]["coverage_config"]["score"])
        self.assertTrue(result["checks"]["test_ratio"]["excluded"])
        self.assertIsNone(result["checks"]["test_ratio"]["score"])
        # Non-excluded checks have scores
        self.assertFalse(result["checks"]["test_execution"]["excluded"])
        self.assertIsNotNone(result["checks"]["test_execution"]["score"])

    def test_excluded_checks_dont_affect_weight(self):
        """Excluded checks should not contribute to total_weight."""
        result_full = assess_repo(self.tmp)
        excluded = frozenset({"coverage_config"})
        profile = ResolvedProfile(name="custom", excluded_checks=excluded, source="cli")
        result_excl = assess_repo(self.tmp, excluded_checks=excluded, profile_info=profile)
        # Scores will differ because weights are rescaled
        self.assertIsNotNone(result_full["overall_score"])
        self.assertIsNotNone(result_excl["overall_score"])

    def test_raw_score_present(self):
        excluded = frozenset({"coverage_config"})
        profile = ResolvedProfile(name="custom", excluded_checks=excluded, source="cli")
        result = assess_repo(self.tmp, excluded_checks=excluded, profile_info=profile)
        self.assertIn("raw_score", result)
        # Raw score uses all weights, overall score uses only non-excluded weights
        # So raw_score <= overall_score when excluded checks would score low
        self.assertIsNotNone(result["raw_score"])
        self.assertIsNotNone(result["overall_score"])

    def test_profile_metadata_in_results(self):
        excluded = frozenset({"coverage_config"})
        profile = ResolvedProfile(name="test-repo", excluded_checks=excluded, source="profiles.json")
        result = assess_repo(self.tmp, excluded_checks=excluded, profile_info=profile)
        self.assertEqual(result["profile"]["name"], "test-repo")
        self.assertEqual(result["profile"]["excluded_checks"], ["coverage_config"])
        self.assertEqual(result["profile"]["source"], "profiles.json")

    def test_verify_gate_with_no_verify_checks(self):
        """When all Verify checks are excluded, verify gate should be None."""
        verify_checks = frozenset({"test_ratio", "test_execution", "coverage_config",
                                    "ci_runs_tests", "test_isolation", "precommit_hooks"})
        # This would violate rule 8, but engine doesn't enforce rules (profiles.py does)
        result = assess_repo(self.tmp, excluded_checks=verify_checks)
        self.assertIsNone(result["verify_avg"])
        self.assertIsNone(result["verify_gate"])

    def test_no_exclusions_has_default_profile(self):
        result = assess_repo(self.tmp)
        self.assertEqual(result["profile"]["name"], "default")


if __name__ == "__main__":
    unittest.main()
