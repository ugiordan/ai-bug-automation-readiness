# tests/test_multi_org_report.py
"""Integration tests for multi-org HTML report generation."""

import os
import tempfile
import unittest

from assess.cli import discover_repos
from assess.engine import assess_repo
from assess.profiles import resolve_profile
from assess.reports.html import generate_html, generate_html_tabbed
from assess.reports import prepare_report_data


class TestMultiOrgHTMLReport(unittest.TestCase):

    def _make_minimal_repo(self, base_dir, org, repo_name):
        """Create a minimal repo with .git dir and a Python file."""
        repo_path = os.path.join(base_dir, org, repo_name)
        os.makedirs(os.path.join(repo_path, ".git"))
        os.makedirs(os.path.join(repo_path, "src"))
        with open(os.path.join(repo_path, "src", "main.py"), "w") as f:
            f.write("def hello():\n    return 'hello'\n")
        with open(os.path.join(repo_path, "README.md"), "w") as f:
            f.write(f"# {repo_name}\n")
        return repo_path

    def test_tabbed_report_has_tabs(self):
        tmpdir = tempfile.mkdtemp()
        repo1 = self._make_minimal_repo(tmpdir, "org1", "repo-a")
        repo2 = self._make_minimal_repo(tmpdir, "org2", "repo-b")

        results = []
        for org, repo_name, repo_path in discover_repos(tmpdir, set()):
            profile = resolve_profile(repo_path)
            result = assess_repo(repo_path,
                                 excluded_checks=profile.excluded_checks,
                                 profile_info=profile)
            result["org"] = org
            results.append(result)

        results_by_org = {}
        for r in results:
            results_by_org.setdefault(r["org"], []).append(r)

        html = generate_html_tabbed(results_by_org)

        self.assertIn('class="tab-bar"', html)
        self.assertIn('data-tab="org1"', html)
        self.assertIn('data-tab="org2"', html)
        self.assertIn('data-tab="all"', html)
        self.assertIn('id="panel-org1"', html)
        self.assertIn('id="panel-org2"', html)
        self.assertIn('id="panel-all"', html)
        self.assertIn('data-chart', html)  # Lazy chart init

    def test_single_org_no_tabs(self):
        tmpdir = tempfile.mkdtemp()
        self._make_minimal_repo(tmpdir, "org1", "repo-a")

        results = []
        for org, repo_name, repo_path in discover_repos(tmpdir, set()):
            profile = resolve_profile(repo_path)
            result = assess_repo(repo_path,
                                 excluded_checks=profile.excluded_checks,
                                 profile_info=profile)
            result["org"] = org
            results.append(result)

        # Single org: use generate_html, no tabs
        html = generate_html(results, org="org1")
        self.assertNotIn('class="tab-bar"', html)
        self.assertNotIn('tab-panel', html)


if __name__ == "__main__":
    unittest.main()
