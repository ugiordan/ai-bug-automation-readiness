"""Tests for individual check functions."""

import random
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
import tempfile
import os

from assess.checks import (
    check_architecture_docs,
    check_contributing_guide,
    check_structured_logging,
    check_fixture_data,
    check_test_ratio,
)


class TestCheckArchitectureDocs(unittest.TestCase):
    """Tests for check_architecture_docs - Issue #3 fix."""

    def _make_repo_with_readmes(self, count):
        """Create a temp repo with N module-level READMEs."""
        tmpdir = tempfile.mkdtemp()
        all_files = []
        for i in range(count):
            subdir = Path(tmpdir) / f"module_{i}"
            subdir.mkdir()
            readme = subdir / "README.md"
            readme.write_text(f"# Module {i}")
            all_files.append(readme)
        return tmpdir, all_files

    def test_no_readmes_scores_zero(self):
        tmpdir = tempfile.mkdtemp()
        score, evidence = check_architecture_docs(tmpdir, all_files=[])
        self.assertEqual(score, 0)

    def test_one_readme_scores_15(self):
        tmpdir, all_files = self._make_repo_with_readmes(1)
        score, evidence = check_architecture_docs(tmpdir, all_files=all_files)
        self.assertEqual(score, 15)

    def test_three_readmes_scores_30(self):
        tmpdir, all_files = self._make_repo_with_readmes(3)
        score, evidence = check_architecture_docs(tmpdir, all_files=all_files)
        self.assertEqual(score, 30)

    def test_four_readmes_scores_30(self):
        tmpdir, all_files = self._make_repo_with_readmes(4)
        score, evidence = check_architecture_docs(tmpdir, all_files=all_files)
        self.assertEqual(score, 30)

    def test_five_readmes_scores_40(self):
        tmpdir, all_files = self._make_repo_with_readmes(5)
        score, evidence = check_architecture_docs(tmpdir, all_files=all_files)
        self.assertEqual(score, 40)

    def test_many_readmes_scores_40(self):
        tmpdir, all_files = self._make_repo_with_readmes(20)
        score, evidence = check_architecture_docs(tmpdir, all_files=all_files)
        self.assertEqual(score, 40)

    def test_arch_doc_plus_five_readmes(self):
        tmpdir, all_files = self._make_repo_with_readmes(5)
        arch = Path(tmpdir) / "ARCHITECTURE.md"
        arch.write_text("# Architecture")
        score, evidence = check_architecture_docs(tmpdir, all_files=all_files)
        self.assertEqual(score, 80)  # 40 (arch) + 40 (readmes)


class TestCheckContributingGuide(unittest.TestCase):
    """Tests for check_contributing_guide - Issue #5 fix."""

    def test_best_score_across_files(self):
        """Sparse CONTRIBUTING.md + rich DEVELOPMENT.md should use best score."""
        tmpdir = tempfile.mkdtemp()
        # Sparse contributing
        (Path(tmpdir) / "CONTRIBUTING.md").write_text("Please contribute.")
        # Rich development guide
        (Path(tmpdir) / "DEVELOPMENT.md").write_text(
            "How to test, build, run, setup, install, and debug this project."
        )
        score, evidence = check_contributing_guide(tmpdir)
        self.assertEqual(score, 100)
        self.assertIn("DEVELOPMENT.md", evidence[0])

    def test_early_return_bug_fixed(self):
        """Should NOT return score from first file if second is better."""
        tmpdir = tempfile.mkdtemp()
        # First file: only 1 keyword match → 60
        (Path(tmpdir) / "CONTRIBUTING.md").write_text("Please help us test.")
        # Second file: all 6 keywords → 100
        (Path(tmpdir) / "DEVELOPMENT.md").write_text(
            "test build run setup install debug"
        )
        score, _ = check_contributing_guide(tmpdir)
        self.assertGreaterEqual(score, 100)

    def test_github_contributing_detected(self):
        tmpdir = tempfile.mkdtemp()
        gh_dir = Path(tmpdir) / ".github"
        gh_dir.mkdir()
        (gh_dir / "CONTRIBUTING.md").write_text(
            "How to test, build, run, setup, install, and debug."
        )
        score, evidence = check_contributing_guide(tmpdir)
        self.assertEqual(score, 100)

    def test_developer_guide_detected(self):
        tmpdir = tempfile.mkdtemp()
        docs_dir = Path(tmpdir) / "docs"
        docs_dir.mkdir()
        (docs_dir / "DEVELOPER_GUIDE.md").write_text(
            "test build run setup install debug"
        )
        score, evidence = check_contributing_guide(tmpdir)
        self.assertEqual(score, 100)

    def test_no_guide_scores_zero(self):
        tmpdir = tempfile.mkdtemp()
        score, evidence = check_contributing_guide(tmpdir)
        self.assertEqual(score, 0)

    def test_readme_fallback_still_works(self):
        tmpdir = tempfile.mkdtemp()
        (Path(tmpdir) / "README.md").write_text("## Contributing\nPlease help.")
        score, evidence = check_contributing_guide(tmpdir)
        self.assertEqual(score, 40)


class TestCheckStructuredLogging(unittest.TestCase):
    """Tests for check_structured_logging - Issue #6 fix."""

    def _make_repo_with_source(self, filenames_content):
        """Create repo with source files. Returns (tmpdir, all_files)."""
        tmpdir = tempfile.mkdtemp()
        all_files = []
        for name, content in filenames_content.items():
            p = Path(tmpdir) / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
            all_files.append(p)
        return tmpdir, all_files

    def test_logger_uppercase_detected(self):
        tmpdir, all_files = self._make_repo_with_source({
            f"test_{i}.py": 'LOGGER.info("message")' for i in range(10)
        })
        rng = random.Random(42)
        score, evidence = check_structured_logging(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 80)

    def test_logger_lowercase_detected(self):
        tmpdir, all_files = self._make_repo_with_source({
            f"app_{i}.py": 'logger.debug("msg")' for i in range(10)
        })
        rng = random.Random(42)
        score, evidence = check_structured_logging(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 80)

    def test_logging_warning_detected(self):
        tmpdir, all_files = self._make_repo_with_source({
            f"svc_{i}.py": 'logging.warning("msg")' for i in range(10)
        })
        rng = random.Random(42)
        score, evidence = check_structured_logging(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 80)

    def test_underscore_log_detected(self):
        tmpdir, all_files = self._make_repo_with_source({
            f"mod_{i}.py": '_log.error("fail")' for i in range(10)
        })
        rng = random.Random(42)
        score, evidence = check_structured_logging(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 80)

    def test_go_pascal_case_still_works(self):
        tmpdir, all_files = self._make_repo_with_source({
            f"handler_{i}.go": 'log.Info("starting")' for i in range(10)
        })
        rng = random.Random(42)
        score, evidence = check_structured_logging(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 80)


class TestCheckFixtureData(unittest.TestCase):
    """Tests for check_fixture_data - Issue #4 fix."""

    def test_kustomize_e2e_overlay_detected(self):
        tmpdir = tempfile.mkdtemp()
        overlay = Path(tmpdir) / "manifests" / "kustomize" / "overlays" / "e2e"
        overlay.mkdir(parents=True)
        (overlay / "test-catalog.yaml").write_text("kind: ConfigMap")
        all_files = list(Path(tmpdir).rglob("*"))
        rng = random.Random(42)
        score, evidence = check_fixture_data(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 50)

    def test_config_overlays_test_detected(self):
        tmpdir = tempfile.mkdtemp()
        overlay = Path(tmpdir) / "config" / "overlays" / "test"
        overlay.mkdir(parents=True)
        (overlay / "resource.yaml").write_text("kind: Service")
        all_files = list(Path(tmpdir).rglob("*"))
        rng = random.Random(42)
        score, evidence = check_fixture_data(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 50)

    def test_traditional_testdata_still_works(self):
        tmpdir = tempfile.mkdtemp()
        td = Path(tmpdir) / "testdata"
        td.mkdir()
        for i in range(10):
            (td / f"fixture_{i}.json").write_text("{}")
        all_files = list(Path(tmpdir).rglob("*"))
        rng = random.Random(42)
        score, evidence = check_fixture_data(tmpdir, all_files=all_files, rng=rng)
        self.assertEqual(score, 90)

    def test_no_fixtures_scores_zero(self):
        tmpdir = tempfile.mkdtemp()
        score, evidence = check_fixture_data(tmpdir, all_files=[], rng=random.Random(42))
        self.assertEqual(score, 0)

    def test_deploy_testdata_detected(self):
        tmpdir = tempfile.mkdtemp()
        overlay = Path(tmpdir) / "deploy" / "kustomize" / "testdata"
        overlay.mkdir(parents=True)
        (overlay / "fixture.yaml").write_text("kind: Deployment")
        all_files = list(Path(tmpdir).rglob("*"))
        rng = random.Random(42)
        score, evidence = check_fixture_data(tmpdir, all_files=all_files, rng=rng)
        self.assertGreaterEqual(score, 50)


class TestCheckTestRatioQuality(unittest.TestCase):
    """Tests for test file quality validation in check_test_ratio - Issue #9."""

    def _make_repo(self, source_content, test_content, num_source=10, num_tests=10,
                   source_ext=".py", test_prefix="test_"):
        """Create repo with source and test files. Returns (tmpdir, all_files)."""
        tmpdir = tempfile.mkdtemp()
        all_files = []
        for i in range(num_source):
            p = Path(tmpdir) / f"module_{i}{source_ext}"
            p.write_text(source_content)
            all_files.append(p)
        for i in range(num_tests):
            p = Path(tmpdir) / f"{test_prefix}{i}{source_ext}"
            p.write_text(test_content)
            all_files.append(p)
        return tmpdir, all_files

    def test_substantial_tests_keep_full_score(self):
        """Test files with real assertions should not be penalized."""
        tmpdir, all_files = self._make_repo(
            source_content="def foo():\n    return 1\n",
            test_content=(
                "import unittest\n"
                "class TestFoo(unittest.TestCase):\n"
                "    def test_foo(self):\n"
                "        self.assertEqual(foo(), 1)\n"
                "    def test_bar(self):\n"
                "        self.assertTrue(bar())\n"
            ),
        )
        rng = random.Random(42)
        score, evidence = check_test_ratio(tmpdir, all_files=all_files, rng=rng)
        self.assertEqual(score, 100)
        # Should NOT mention stub/quality issues
        self.assertFalse(any("stub" in e.lower() for e in evidence))

    def test_stub_tests_reduce_score(self):
        """Test files with no assertions should reduce the score."""
        tmpdir, all_files = self._make_repo(
            source_content="def foo():\n    return 1\n",
            test_content="# empty test\npass\n",
        )
        rng = random.Random(42)
        score, evidence = check_test_ratio(tmpdir, all_files=all_files, rng=rng)
        # 10:10 ratio would normally be 100, but stubs should reduce it
        self.assertLess(score, 100)
        self.assertTrue(any("stub" in e.lower() or "quality" in e.lower() for e in evidence))

    def test_mixed_quality_partial_penalty(self):
        """Mix of real and stub tests should get partial penalty."""
        tmpdir = tempfile.mkdtemp()
        all_files = []
        # 10 source files
        for i in range(10):
            p = Path(tmpdir) / f"module_{i}.py"
            p.write_text("def foo():\n    return 1\n")
            all_files.append(p)
        # 5 real test files
        for i in range(5):
            p = Path(tmpdir) / f"test_real_{i}.py"
            p.write_text("def test_it():\n    assert foo() == 1\n")
            all_files.append(p)
        # 5 stub test files
        for i in range(5):
            p = Path(tmpdir) / f"test_stub_{i}.py"
            p.write_text("# TODO: add tests\npass\n")
            all_files.append(p)
        rng = random.Random(42)
        score, evidence = check_test_ratio(tmpdir, all_files=all_files, rng=rng)
        # Should be between stub-only and full-quality scores
        self.assertGreater(score, 0)
        self.assertLess(score, 100)

    def test_go_assertions_detected(self):
        """Go test assertions (t.Run, t.Error, t.Fatal) should count."""
        tmpdir, all_files = self._make_repo(
            source_content="package main\nfunc Foo() int { return 1 }\n",
            test_content=(
                "package main\n"
                "import \"testing\"\n"
                "func TestFoo(t *testing.T) {\n"
                "    t.Run(\"case\", func(t *testing.T) {\n"
                "        if Foo() != 1 { t.Error(\"wrong\") }\n"
                "    })\n"
                "}\n"
            ),
            source_ext=".go",
            test_prefix="",
            num_tests=0,
        )
        # Add Go test files manually (they use _test.go suffix)
        for i in range(10):
            p = Path(tmpdir) / f"foo_{i}_test.go"
            p.write_text(
                "package main\n"
                "import \"testing\"\n"
                "func TestFoo(t *testing.T) {\n"
                "    t.Run(\"case\", func(t *testing.T) {\n"
                "        if Foo() != 1 { t.Error(\"wrong\") }\n"
                "    })\n"
                "}\n"
            )
            all_files.append(p)
        rng = random.Random(42)
        score, evidence = check_test_ratio(tmpdir, all_files=all_files, rng=rng)
        self.assertEqual(score, 100)

    def test_js_expect_assertions_detected(self):
        """JS/TS test assertions (expect, it, describe) should count."""
        tmpdir, all_files = self._make_repo(
            source_content="export const foo = () => 1;\n",
            test_content=(
                "describe('foo', () => {\n"
                "  it('returns 1', () => {\n"
                "    expect(foo()).toBe(1);\n"
                "  });\n"
                "});\n"
            ),
            source_ext=".ts",
            test_prefix="",
            num_tests=0,
        )
        # Add TS test files with .test.ts suffix
        for i in range(10):
            p = Path(tmpdir) / f"foo_{i}.test.ts"
            p.write_text(
                "describe('foo', () => {\n"
                "  it('returns 1', () => {\n"
                "    expect(foo()).toBe(1);\n"
                "  });\n"
                "});\n"
            )
            all_files.append(p)
        rng = random.Random(42)
        score, evidence = check_test_ratio(tmpdir, all_files=all_files, rng=rng)
        # Frontend-heavy with good ratio and real assertions
        self.assertGreaterEqual(score, 85)

    def test_no_tests_unaffected(self):
        """Zero test files should still score 0 (quality check doesn't interfere)."""
        tmpdir, all_files = self._make_repo(
            source_content="def foo():\n    return 1\n",
            test_content="",
            num_tests=0,
        )
        rng = random.Random(42)
        score, evidence = check_test_ratio(tmpdir, all_files=all_files, rng=rng)
        self.assertEqual(score, 0)


if __name__ == "__main__":
    unittest.main()
