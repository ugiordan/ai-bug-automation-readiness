"""Tests for batch directory discovery with flat and nested layouts."""

import os
import tempfile
import unittest

from assess.cli import discover_repos


class TestDiscoverRepos(unittest.TestCase):

    def _make_flat_layout(self, repo_names):
        """Create flat layout: batch_dir/repo/.git/"""
        tmpdir = tempfile.mkdtemp()
        for name in repo_names:
            os.makedirs(os.path.join(tmpdir, name, ".git"))
        return tmpdir

    def _make_nested_layout(self, org_repos):
        """Create nested layout: batch_dir/org/repo/.git/
        org_repos: dict mapping org name to list of repo names.
        """
        tmpdir = tempfile.mkdtemp()
        for org, repos in org_repos.items():
            for repo in repos:
                os.makedirs(os.path.join(tmpdir, org, repo, ".git"))
        return tmpdir

    def test_flat_layout(self):
        tmpdir = self._make_flat_layout(["repo-a", "repo-b"])
        results = discover_repos(tmpdir, set())
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], (None, "repo-a", os.path.join(tmpdir, "repo-a")))
        self.assertEqual(results[1], (None, "repo-b", os.path.join(tmpdir, "repo-b")))

    def test_nested_layout(self):
        tmpdir = self._make_nested_layout({
            "opendatahub-io": ["model-registry", "odh-dashboard"],
            "project-codeflare": ["codeflare-sdk"],
        })
        results = discover_repos(tmpdir, set())
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0][0], "opendatahub-io")
        self.assertEqual(results[0][1], "model-registry")
        self.assertEqual(results[1][0], "opendatahub-io")
        self.assertEqual(results[1][1], "odh-dashboard")
        self.assertEqual(results[2][0], "project-codeflare")
        self.assertEqual(results[2][1], "codeflare-sdk")

    def test_flat_exclude(self):
        tmpdir = self._make_flat_layout(["repo-a", "repo-b", "skip-me"])
        results = discover_repos(tmpdir, {"skip-me"})
        self.assertEqual(len(results), 2)
        names = [r[1] for r in results]
        self.assertNotIn("skip-me", names)

    def test_nested_exclude_bare_name(self):
        tmpdir = self._make_nested_layout({"org1": ["repo-a", "skip-me"]})
        results = discover_repos(tmpdir, {"skip-me"})
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "repo-a")

    def test_nested_exclude_qualified_name(self):
        tmpdir = self._make_nested_layout({"org1": ["repo-a"], "org2": ["repo-a"]})
        results = discover_repos(tmpdir, {"org2/repo-a"})
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "org1")

    def test_empty_dir(self):
        tmpdir = tempfile.mkdtemp()
        results = discover_repos(tmpdir, set())
        self.assertEqual(results, [])

    def test_ignores_files(self):
        tmpdir = self._make_flat_layout(["repo-a"])
        with open(os.path.join(tmpdir, "README.md"), "w") as f:
            f.write("hello")
        results = discover_repos(tmpdir, set())
        self.assertEqual(len(results), 1)

    def test_mixed_layout_handles_both(self):
        """If some entries have .git (flat) and some don't (nested org), handle both."""
        tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmpdir, "flat-repo", ".git"))
        os.makedirs(os.path.join(tmpdir, "my-org", "nested-repo", ".git"))
        results = discover_repos(tmpdir, set())
        self.assertEqual(len(results), 2)
        flat = [r for r in results if r[0] is None]
        nested = [r for r in results if r[0] is not None]
        self.assertEqual(len(flat), 1)
        self.assertEqual(flat[0][1], "flat-repo")
        self.assertEqual(len(nested), 1)
        self.assertEqual(nested[0][1], "nested-repo")


if __name__ == "__main__":
    unittest.main()
