"""Verify phase checks: can the agent run tests to verify the fix works?"""

import random
import re
from pathlib import Path

from ..config import SOURCE_EXTS
from ..utils import is_generated_file, read_file_safe
from ._shared import _is_test_file


def check_test_ratio(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check ratio of test files to source files."""
    source_files = []
    test_files = []

    for f in all_files or []:
        if f.is_file() and f.suffix.lower() in SOURCE_EXTS and not is_generated_file(f):
            if _is_test_file(f):
                test_files.append(f)
            else:
                source_files.append(f)

    total_source = len(source_files)
    total_tests = len(test_files)

    if total_source == 0:
        return 0, ["No source files found (config-only repo?)"]

    ratio = total_tests / total_source

    ts_js_source = sum(1 for f in source_files if f.suffix.lower() in {".ts", ".tsx", ".js", ".jsx"})
    is_frontend_heavy = ts_js_source / total_source > 0.6 if total_source else False

    if is_frontend_heavy:
        if ratio >= 0.6:
            score = 100
        elif ratio >= 0.3:
            score = 85
        elif ratio >= 0.15:
            score = 70
        elif ratio >= 0.08:
            score = 50
        elif ratio >= 0.03:
            score = 25
        elif total_tests > 0:
            score = 10
        else:
            score = 0
    else:
        if ratio >= 1.0:
            score = 100
        elif ratio >= 0.6:
            score = 85
        elif ratio >= 0.4:
            score = 70
        elif ratio >= 0.2:
            score = 50
        elif ratio >= 0.05:
            score = 25
        elif total_tests > 0:
            score = 10
        else:
            score = 0

    evidence = [f"{total_tests} test files / {total_source} source files (ratio: {ratio:.2f})"]
    if is_frontend_heavy:
        evidence.append("Frontend-heavy repo (relaxed thresholds)")

    if test_files and score > 0:
        sample = rng.sample(test_files, min(20, len(test_files))) if rng else test_files[:20]
        assertion_re = re.compile(
            r"(?:"
            r"assert\b|self\.assert|assertEqual|assertTrue|assertRaises"
            r"|expect\(|\.toBe|\.toEqual|\.toContain|\.toThrow"
            r"|\.Should\(|Expect\(|It\("
            r"|t\.Run\(|t\.Error|t\.Fatal|t\.Log"
            r"|@Test|assertEquals|assertThat|verify\("
            r")",
            re.IGNORECASE,
        )
        substantial = 0
        for tf in sample:
            content = read_file_safe(tf, max_bytes=5000)
            lines = [line for line in content.splitlines() if line.strip() and not line.strip().startswith(("#", "//"))]
            has_assertions = bool(assertion_re.search(content))
            if has_assertions and len(lines) >= 5:
                substantial += 1

        quality_ratio = substantial / len(sample)
        if quality_ratio < 0.5:
            penalty = int(score * 0.5)
            score = max(score - penalty, 10)
            evidence.append(
                f"Low test quality: {substantial}/{len(sample)} sampled test files have assertions (stub penalty applied)"
            )
        elif quality_ratio < 0.8:
            penalty = int(score * 0.25)
            score = max(score - penalty, 10)
            evidence.append(f"Mixed test quality: {substantial}/{len(sample)} sampled test files have assertions")

    return score, evidence


def check_test_execution(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check if tests can be run with a single command."""
    score = 0
    evidence = []

    makefiles = []
    root_makefile = Path(repo_path) / "Makefile"
    if root_makefile.exists():
        makefiles.append(("", root_makefile))
    root = Path(repo_path)
    for depth1 in root.iterdir():
        if depth1.is_dir() and not depth1.name.startswith("."):
            mf1 = depth1 / "Makefile"
            if mf1.exists():
                makefiles.append((depth1.name, mf1))
            for depth2 in depth1.iterdir():
                if depth2.is_dir() and not depth2.name.startswith("."):
                    mf2 = depth2 / "Makefile"
                    if mf2.exists():
                        rel = f"{depth1.name}/{depth2.name}"
                        makefiles.append((rel, mf2))

    all_test_targets: list[str] = []
    for prefix, makefile in makefiles:
        content = read_file_safe(makefile)
        test_targets = re.findall(
            r"^(test|check|verify|unittest|unit-test|unit_test|unit-test-cli|"
            r"test-unit|test-e2e|test-integration|"
            r"e2e-test|e2e_test|e2e|"
            r"integration-test|integration_test|functest)\s*:",
            content,
            re.MULTILINE,
        )
        if test_targets:
            label = f"{prefix}/" if prefix else ""
            all_test_targets.extend(f"{label}{t}" for t in test_targets)

    if all_test_targets:
        score = 80
        evidence.append(f"Makefile targets: {', '.join(all_test_targets)}")
        if len(all_test_targets) >= 3:
            score = 100
            evidence.append("Multiple test types available")
        elif len(all_test_targets) >= 2:
            score = 90

    for script in ["scripts/test.sh", "hack/test.sh", "test.sh"]:
        if (Path(repo_path) / script).exists():
            score = max(score, 60)
            evidence.append(f"Test script: {script}")

    pkg_json = Path(repo_path) / "package.json"
    if pkg_json.exists():
        content = read_file_safe(pkg_json)
        scripts_match = re.search(r'"scripts"\s*:\s*\{([^}]*)\}', content, re.DOTALL)
        if scripts_match and re.search(r'"test[^"]*"\s*:', scripts_match.group(1)):
            score = max(score, 80)
            evidence.append("npm test script defined")

    pyproject = Path(repo_path) / "pyproject.toml"
    if pyproject.exists():
        content = read_file_safe(pyproject)
        if "[tool.pytest" in content:
            score = max(score, 60)
            evidence.append("pytest configured in pyproject.toml")

    if (Path(repo_path) / "tox.ini").exists():
        score = max(score, 60)
        evidence.append("tox.ini found")
    if (Path(repo_path) / "noxfile.py").exists():
        score = max(score, 60)
        evidence.append("noxfile.py found")

    if (Path(repo_path) / "pytest.ini").exists():
        score = max(score, 70)
        evidence.append("pytest.ini found")
    setup_cfg = Path(repo_path) / "setup.cfg"
    if setup_cfg.exists():
        content = read_file_safe(setup_cfg)
        if "[tool:pytest]" in content or "[pytest]" in content:
            score = max(score, 70)
            evidence.append("pytest configured in setup.cfg")

    has_test_files = any(
        f.is_file() and f.suffix.lower() in {".java", ".kt", ".scala", ".groovy"} and _is_test_file(f)
        for f in (all_files or [])
    )
    if (Path(repo_path) / "build.gradle").exists() or (Path(repo_path) / "build.gradle.kts").exists():
        score = max(score, 70 if has_test_files else 30)
        evidence.append("Gradle build found" + (" with test files" if has_test_files else " (no test files detected)"))
    if (Path(repo_path) / "pom.xml").exists():
        score = max(score, 70 if has_test_files else 30)
        evidence.append("Maven build found" + (" with test files" if has_test_files else " (no test files detected)"))

    if not evidence:
        evidence.append("No obvious one-command test execution found")

    return score, evidence


def check_coverage_config(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check if code coverage is configured."""
    score = 0
    evidence = []

    coverage_indicators = {
        ".coveragerc": "Python coverage config",
        "codecov.yml": "Codecov configured",
        ".codecov.yml": "Codecov configured",
    }

    for filename, desc in coverage_indicators.items():
        if (Path(repo_path) / filename).exists():
            score = max(score, 60)
            evidence.append(desc)

    makefile = Path(repo_path) / "Makefile"
    if makefile.exists():
        content = read_file_safe(makefile)
        if "-coverprofile" in content or "-cover" in content:
            score = max(score, 80)
            evidence.append("Go coverage flags in Makefile")
        elif re.search(r"\bcover(age)?\b", content):
            score = max(score, 50)
            evidence.append("Coverage-related target in Makefile")

    ci_dir = Path(repo_path) / ".github" / "workflows"
    if ci_dir.exists():
        for cf in list(ci_dir.glob("*.yml")) + list(ci_dir.glob("*.yaml")):
            content = read_file_safe(cf)
            if re.search(r"coverprofile|coverage|\bcodecov\b", content, re.IGNORECASE):
                score = max(score, 60)
                evidence.append(f"Coverage in CI workflow: {cf.name}")
                break

    pyproject = Path(repo_path) / "pyproject.toml"
    if pyproject.exists():
        content = read_file_safe(pyproject)
        if re.search(r"\[tool\.(coverage|pytest\.ini_options)\]", content) and "cov" in content.lower():
            score = max(score, 60)
            evidence.append("Coverage config in pyproject.toml")

    if len(evidence) >= 2 and score < 100:
        score = min(score + 20, 100)
        evidence.append("Multiple coverage signals detected")

    if not evidence:
        evidence.append("No coverage configuration found")

    return min(score, 100), evidence


def check_ci_runs_tests(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check if CI pipeline actually runs tests on PRs."""
    ci_dir = Path(repo_path) / ".github" / "workflows"
    if not ci_dir.exists():
        return 0, ["No .github/workflows/ directory"]

    ci_files = list(ci_dir.glob("*.yml")) + list(ci_dir.glob("*.yaml"))
    if not ci_files:
        return 0, ["No CI workflow files found"]

    has_pr_trigger = False
    has_test_step = False
    has_pr_and_test = False
    test_workflows = []

    test_patterns = [
        r"make\s+test",
        r"make\s+unittest",
        r"make\s+unit-test",
        r"make\s+unit_test",
        r"make\s+functest",
        r"make\s+e2e",
        r"make\s+check",
        r"go\s+test",
        r"pytest",
        r"python\s+-m\s+pytest",
        r"npm\s+(run\s+)?test",
        r"yarn\s+(run\s+)?test",
        r"vitest",
        r"jest",
        r"mvn\s+test",
        r"gradle\w*\s+test",
        r"cargo\s+test",
        r"tox\b",
        r"nox\b",
    ]

    for cf in ci_files:
        content = read_file_safe(cf)
        file_has_pr = bool(re.search(r"\bpull_request\b(?!_target)", content))
        file_has_test = False
        if file_has_pr:
            has_pr_trigger = True
        for tp in test_patterns:
            if re.search(tp, content):
                has_test_step = True
                file_has_test = True
                if cf.name not in test_workflows:
                    test_workflows.append(cf.name)
                break
        if file_has_pr and file_has_test:
            has_pr_and_test = True

    evidence = []
    if test_workflows:
        evidence.append(f"Tests found in {len(test_workflows)} CI workflow(s): {', '.join(test_workflows[:3])}")

    if has_pr_and_test:
        score = 100
        evidence.insert(0, "CI runs tests on pull requests")
    elif has_pr_trigger and has_test_step:
        score = 70
        evidence.insert(0, "CI has PR triggers and test steps, but in separate workflows")
    elif has_test_step:
        score = 60
        evidence.insert(0, "CI runs tests (but may not trigger on PRs)")
    elif has_pr_trigger:
        score = 30
        evidence.insert(0, "CI triggers on PRs but no test step found")
    else:
        score = 0
        evidence.append("CI exists but no PR trigger or test steps found")

    return score, evidence


def check_test_isolation(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check if tests can run without external infrastructure."""
    test_files = [f for f in (all_files or []) if f.is_file() and f.suffix.lower() in SOURCE_EXTS and _is_test_file(f)]

    if not test_files:
        return 0, ["No test files found"]

    sample = rng.sample(test_files, min(30, len(test_files))) if rng else test_files[:30]
    infra_patterns = [
        r"kubeconfig",
        r"kubectl",
        r"docker\.",
        r"http://localhost",
        r"127\.0\.0\.1",
        r"port.?forward",
        r"openshift",
        r"ClusterRole",
        r"ServiceAccount",
        r"Namespace\(",
    ]
    unit_patterns = [
        r"envtest",
        r"fake\.NewSimpleClientset",
        r"fake\.New",
        r"\bmock\b",
        r"\bMock\b",
        r"httptest\.NewServer",
        r"pytest",
        r"jest",
        r"//go:build\s+!e2e",
        r"//go:build\s+unit",
    ]
    e2e_tag_patterns = [
        r"//go:build\s+(test_)?e2e",
        r"//go:build\s+test_integration",
        r"//\s*\+build\s+(test_)?e2e",
        r"//\s*\+build\s+test_integration",
    ]

    infra_count = 0
    unit_count = 0

    for tf in sample:
        content = read_file_safe(tf, max_bytes=10000)
        has_infra = any(re.search(pat, content) for pat in infra_patterns)
        has_e2e_tag = any(re.search(pat, content) for pat in e2e_tag_patterns)
        has_unit = any(re.search(pat, content) for pat in unit_patterns)
        path_str = str(tf).lower()
        in_e2e_dir = "/e2e/" in path_str or "/integration/" in path_str

        if has_e2e_tag or (has_infra and not has_unit) or (in_e2e_dir and has_infra):
            infra_count += 1
        elif has_unit or (not has_infra and not in_e2e_dir):
            unit_count += 1

    makefile = Path(repo_path) / "Makefile"
    has_test_separation = False
    if makefile.exists():
        content = read_file_safe(makefile)
        if re.search(r"(unittest|unit-test|unit_test)\s*:", content) and re.search(
            r"(e2e|integration|functest)\s*:", content
        ):
            has_test_separation = True

    total_classified = infra_count + unit_count
    if total_classified == 0:
        score = 50
        evidence = ["Could not classify test types from sample"]
    else:
        unit_pct = unit_count / total_classified * 100
        if unit_pct >= 70:
            score = 90
        elif unit_pct >= 50:
            score = 70
        elif unit_pct >= 30:
            score = 50
        else:
            score = 30
        evidence = [
            f"~{unit_pct:.0f}% unit tests, ~{100 - unit_pct:.0f}% infra-dependent ({unit_count}/{total_classified} sampled)"
        ]

    if has_test_separation:
        score = min(score + 15, 100)
        evidence.append("Makefile separates unit and integration test targets")

    return score, evidence


def check_precommit_hooks(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for pre-commit hooks or local validation configuration."""
    score = 0
    evidence = []

    if (Path(repo_path) / ".pre-commit-config.yaml").exists():
        content = read_file_safe(Path(repo_path) / ".pre-commit-config.yaml")
        score = 70
        evidence.append(".pre-commit-config.yaml found")
        has_lint = bool(
            re.search(
                r"\b(black|ruff|flake8|isort|prettier|eslint|gofmt|golangci|staticcheck|revive|"
                r"go.vet|rustfmt|clippy|checkstyle|spotbugs|ktlint|scalafmt|rubocop|shellcheck)\b",
                content,
                re.IGNORECASE,
            )
        )
        has_test = bool(
            re.search(
                r"\b(pytest|mypy|pyright|go[\s-]test|cargo[\s-]test|junit|maven-surefire|"
                r"jest|vitest|mocha|nox|tox)\b",
                content,
                re.IGNORECASE,
            )
        )
        if has_lint and has_test:
            score = 100
            evidence.append("Includes both linting and type/test hooks")
        elif has_lint:
            score = 90
            evidence.append("Includes linting hooks")

    pkg_json = Path(repo_path) / "package.json"
    if pkg_json.exists():
        content = read_file_safe(pkg_json)
        if '"husky"' in content or '"prepare": "husky' in content:
            score = max(score, 70)
            evidence.append("Husky git hooks configured")

    if (Path(repo_path) / ".husky").is_dir():
        score = max(score, 70)
        evidence.append(".husky/ directory found")

    if (Path(repo_path) / "lefthook.yml").exists() or (Path(repo_path) / ".lefthook.yml").exists():
        score = max(score, 70)
        evidence.append("Lefthook configured")

    if (Path(repo_path) / ".githooks").is_dir():
        score = max(score, 60)
        evidence.append(".githooks/ directory found")

    if not evidence:
        evidence.append("No pre-commit hooks or local validation configured")

    return min(score, 100), evidence
