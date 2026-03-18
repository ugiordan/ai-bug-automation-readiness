"""Individual check functions for AI Bug Automation Readiness Assessment."""

import re
from pathlib import Path

from .config import SOURCE_EXTS
from .utils import find_files, is_generated_file, read_file_safe, count_lines_fast, detect_languages


# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------
TEST_FILE_PATTERNS = ["_test.", "test_", "_spec.", ".spec.", ".test.", ".cy.", "Test.", "Tests."]

TEST_HELPER_PATTERNS = [
    "conftest", "helper", "helpers", "utils", "util", "fixture", "fixtures",
    "factory", "factories", "common", "setup", "base", "shared", "support",
    "mock", "mocks", "matchers", "scheme", "types", "testutil", "testutils",
]


def _source_files_from(all_files):
    """Filter to non-generated source files."""
    return [f for f in all_files
            if f.is_file() and f.suffix.lower() in SOURCE_EXTS and not is_generated_file(f)]


def _is_test_file(path):
    """Check if a file is a test file (not a test helper)."""
    name = path.name.lower()
    in_test_dir = "__tests__" in path.parts or "tests" in path.parts or "test" in path.parts
    is_helper = any(name.startswith(hp) or f"_{hp}" in name for hp in TEST_HELPER_PATTERNS)
    return any(tp in name for tp in TEST_FILE_PATTERNS) or (in_test_dir and not is_helper)


# ---------------------------------------------------------------------------
# Check functions — all accept (repo_path, *, all_files=None, rng=None)
# ---------------------------------------------------------------------------

def check_agent_context(repo_path, *, all_files=None, rng=None):
    """Check for CLAUDE.md, AGENTS.md, or similar AI context files."""
    score = 0
    evidence = []

    context_files = ["CLAUDE.md", "claude.md", "AGENTS.md", "Agents.md", "agents.md",
                     "COPILOT.md", ".cursorrules", "CONTEXT.md"]
    found = []
    for cf in context_files:
        if (Path(repo_path) / cf).exists():
            found.append(cf)
            content = read_file_safe(Path(repo_path) / cf)
            quality_keywords = ["test", "debug", "architecture", "structure", "run", "build", "make"]
            matches = sum(1 for kw in quality_keywords if re.search(rf'\b{kw}\b', content, re.IGNORECASE))
            score += 20 + min(matches * 12, 80)
            evidence.append(f"{cf} found ({matches}/{len(quality_keywords)} quality keywords)")

    if not found:
        evidence.append("No AI context files found (CLAUDE.md, AGENTS.md, etc.)")
        score = 0

    return min(score, 100), evidence


def check_bug_template(repo_path, *, all_files=None, rng=None):
    """Check if bug report template exists and has reproduction steps."""
    score = 0
    evidence = []

    template_paths = [
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/bug_report.yaml",
        ".github/ISSUE_TEMPLATE/bug-report.md",
        ".github/ISSUE_TEMPLATE/bug-report.yml",
        ".github/ISSUE_TEMPLATE/bug-report.yaml",
    ]

    found = False
    for tp in template_paths:
        full_path = Path(repo_path) / tp
        if full_path.exists():
            content = read_file_safe(full_path).lower()

            # Validate that this is actually a bug template by checking
            # the 'name' or 'about' fields in frontmatter, not just any
            # occurrence of "bug" (which could be in labels)
            is_bug_template = True
            if tp.endswith(".md"):
                frontmatter = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if frontmatter:
                    fm_text = frontmatter.group(1)
                    # Check name/about fields specifically, not labels
                    name_match = re.search(r'^name\s*:.*\b(bug|defect|problem)\b', fm_text, re.MULTILINE)
                    about_match = re.search(r'^about\s*:.*\b(bug|issue|problem|defect)\b', fm_text, re.MULTILINE)
                    if not name_match and not about_match:
                        is_bug_template = False
                        evidence.append(f"Found {tp} but name/about fields don't indicate a bug template")

            if not is_bug_template:
                score = 15
                found = True
                break

            found = True
            score = 30

            if re.search(r'\b(reproduc|repro\b|steps to|steps did)', content):
                score += 25
                evidence.append("Has reproduction steps")

            if re.search(r'\bexpect(ed)?\b.*\bactual\b|\bactual\b.*\bexpect(ed)?\b|\bbehavior\b', content):
                score += 20
                evidence.append("Has expected/actual behavior fields")

            if re.search(r'\benvironment\b|\bversion\b|\bplatform\b', content):
                score += 15
                evidence.append("Has environment/version fields")

            if re.search(r'\blog(s|ging)?\b|\berror\b|\bstack.?trace\b|\boutput\b', content):
                score += 10
                evidence.append("Has log/error output fields")

            if tp.endswith((".yml", ".yaml")):
                if "required: true" in content or "required:true" in content:
                    score += 10
                    evidence.append("YAML template with required fields")

            evidence.insert(0, f"Found: {tp}")
            break

    if not found:
        template_dir = Path(repo_path) / ".github" / "ISSUE_TEMPLATE"
        if template_dir.exists():
            templates = [t for t in template_dir.iterdir() if t.is_file()]
            if templates:
                evidence.append(f"Issue templates exist ({len(templates)}) but no dedicated bug template")
                score = 15
            else:
                evidence.append("Empty .github/ISSUE_TEMPLATE/ directory")
        else:
            evidence.append("No .github/ISSUE_TEMPLATE/ directory")

    return min(score, 100), evidence


def check_structured_logging(repo_path, *, all_files=None, rng=None):
    """Check for structured logging patterns."""
    score = 0
    evidence = []

    dep_files = ["go.mod", "requirements.txt", "pyproject.toml", "package.json", "Cargo.toml"]
    logging_libs = {
        r'\bzap\b': "Go structured logging (zap)",
        r'\blogr\b': "Go structured logging (logr)",
        r'\bzerolog\b': "Go structured logging (zerolog)",
        r'\bstructlog\b': "Python structured logging",
        r'\bloguru\b': "Python structured logging",
        r'\bwinston\b': "Node structured logging",
        r'\bpino\b': "Node structured logging",
        r'log/slog': "Go structured logging (slog)",
        r'k8s\.io/klog': "Kubernetes-style logging (klog)",
        r'\bslf4j\b': "Java structured logging (SLF4J)",
        r'\blogback\b': "Java structured logging (Logback)",
        r'\blog4j': "Java structured logging (Log4j)",
        r'"@sentry/': "Frontend error tracking (Sentry)",
        r'\bsentry-sdk\b': "Frontend error tracking (Sentry)",
        r'"@datadog/browser': "Frontend monitoring (Datadog)",
        r'"loglevel"': "Frontend logging (loglevel)",
        r'"log4javascript"': "Frontend logging (log4javascript)",
    }

    found_libs = set()
    for df in dep_files:
        dep_path = Path(repo_path) / df
        if dep_path.exists():
            content = read_file_safe(dep_path)
            for pattern, desc in logging_libs.items():
                if re.search(pattern, content):
                    if desc not in found_libs:
                        found_libs.add(desc)
                        score = max(score, 70)
                        evidence.append(f"{desc} found in {df}")

    files = all_files or []
    source_files = [f for f in files if f.is_file() and f.suffix.lower() in {".go", ".py", ".ts", ".js", ".java", ".kt"} and not is_generated_file(f)]
    sample = rng.sample(source_files, min(50, len(source_files))) if source_files and rng else source_files[:50]

    log_patterns = 0
    error_wrap_patterns = 0

    for sf in sample:
        content = read_file_safe(sf)
        if (re.search(r'\.(Info|Warn|Error|Debug)\(', content)
                or re.search(r'log\.(info|warn|error|debug)\(', content)
                or re.search(r'console\.(error|warn|info|debug)\(', content)
                or re.search(r'Sentry\.(captureException|captureMessage)', content)):
            log_patterns += 1
        if re.search(r'(fmt\.Errorf|errors\.Wrap|errors\.New|raise \w+Error|throw new \w*Error|ErrorBoundary)', content):
            error_wrap_patterns += 1

    if sample:
        log_ratio = log_patterns / len(sample)
        if log_ratio > 0.3:
            score = max(score, 80)
            evidence.append(f"Good logging coverage ({log_patterns}/{len(sample)} sampled files)")
        elif log_ratio > 0.1:
            score = max(score, 50)
            evidence.append(f"Some logging ({log_patterns}/{len(sample)} sampled files)")

        if error_wrap_patterns > 0:
            score = min(score + 20, 100)
            evidence.append(f"Error wrapping patterns ({error_wrap_patterns} files)")

    if not evidence:
        evidence.append("No structured logging detected")

    return min(score, 100), evidence


def check_code_navigability(repo_path, *, all_files=None, rng=None):
    """Check file sizes, excluding generated files."""
    files = _source_files_from(all_files or [])

    if not files:
        return 0, ["No source files found (config-only repo?)"]

    sizes = []
    huge_files = []
    for f in files:
        lines = count_lines_fast(f)
        if lines > 0:
            sizes.append(lines)
            if lines > 500:
                huge_files.append((f.name, lines))

    if not sizes:
        return 0, ["Could not measure file sizes"]

    avg_lines = sum(sizes) / len(sizes)
    huge_pct = len(huge_files) / len(sizes) * 100

    langs = detect_languages(repo_path, all_files)
    primary = langs[0] if langs else "Unknown"
    if primary in ("Go", "Java"):
        thresholds = (200, 400, 700)
    else:
        thresholds = (150, 300, 500)

    if avg_lines < thresholds[0]:
        score = 90
    elif avg_lines < thresholds[1]:
        score = 70
    elif avg_lines < thresholds[2]:
        score = 50
    else:
        score = 30

    if huge_pct > 20:
        score = max(score - 20, 0)

    evidence = [
        f"Average file: {avg_lines:.0f} lines ({len(sizes)} source files, generated excluded)",
        f"Files >500 lines: {len(huge_files)} ({huge_pct:.0f}%)",
    ]
    if huge_files:
        top3 = sorted(huge_files, key=lambda x: x[1], reverse=True)[:3]
        evidence.append(f"Largest: {', '.join(f'{n} ({l}L)' for n, l in top3)}")

    return score, evidence


def check_generated_code(repo_path, *, all_files=None, rng=None):
    """Check what percentage of source code is auto-generated."""
    all_source = [f for f in (all_files or [])
                  if f.is_file() and f.suffix.lower() in SOURCE_EXTS]

    if len(all_source) <= 2:
        return 0, ["No source files (not applicable)"]

    generated = [f for f in all_source if is_generated_file(f)]
    gen_pct = len(generated) / len(all_source) * 100

    if gen_pct < 5:
        score = 100
    elif gen_pct < 15:
        score = 80
    elif gen_pct < 30:
        score = 60
    elif gen_pct < 50:
        score = 40
    else:
        score = 20

    evidence = [f"{len(generated)}/{len(all_source)} files are generated ({gen_pct:.0f}%)"]
    if generated:
        examples = [f.name for f in generated[:5]]
        evidence.append(f"Examples: {', '.join(examples)}")

    return score, evidence


def check_codeowners(repo_path, *, all_files=None, rng=None):
    """Check for CODEOWNERS file."""
    paths = [".github/CODEOWNERS", "CODEOWNERS", "docs/CODEOWNERS"]
    for p in paths:
        full = Path(repo_path) / p
        if full.exists():
            content = read_file_safe(full)
            lines = [l.strip() for l in content.splitlines() if l.strip() and not l.strip().startswith("#")]
            if len(lines) >= 3:
                return 100, [f"CODEOWNERS found ({p}) with {len(lines)} rules"]
            elif lines:
                return 60, [f"CODEOWNERS found ({p}) with {len(lines)} rules (sparse)"]
            else:
                return 30, [f"CODEOWNERS found ({p}) but empty"]

    if (Path(repo_path) / "OWNERS").exists():
        content = read_file_safe(Path(repo_path) / "OWNERS")
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.strip().startswith("#")]
        has_aliases = (Path(repo_path) / "OWNERS_ALIASES").exists()
        if len(lines) >= 3 or has_aliases:
            return 100, ["OWNERS file found (OpenShift/Kubernetes-style)" + (", OWNERS_ALIASES present" if has_aliases else f", {len(lines)} entries")]
        elif lines:
            return 70, [f"OWNERS file found (OpenShift/Kubernetes-style, {len(lines)} entries)"]
        else:
            return 30, ["OWNERS file found but empty"]

    return 0, ["No CODEOWNERS or OWNERS file"]


def check_test_ratio(repo_path, *, all_files=None, rng=None):
    """Check ratio of test files to source files."""
    source_files = []
    test_files = []

    for f in (all_files or []):
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

    # Frontend/component-heavy repos (TS/JS/TSX/JSX) naturally have many small
    # component files, so use relaxed thresholds
    ts_js_source = sum(1 for f in source_files if f.suffix.lower() in {".ts", ".tsx", ".js", ".jsx"})
    is_frontend_heavy = ts_js_source / total_source > 0.6 if total_source else False

    if is_frontend_heavy:
        # Relaxed: React repos with 1 test per 8 source files is decent
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
    return score, evidence


def check_test_execution(repo_path, *, all_files=None, rng=None):
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

    all_test_targets = []
    for prefix, makefile in makefiles:
        content = read_file_safe(makefile)
        test_targets = re.findall(
            r'^(test|check|verify|unittest|unit-test|unit_test|unit-test-cli|'
            r'test-unit|test-e2e|test-integration|'
            r'e2e-test|e2e_test|e2e|'
            r'integration-test|integration_test|functest)\s*:',
            content, re.MULTILINE
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
        # Only match "test" inside the "scripts" block
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

    # Check for tox.ini or nox
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

    # Gradle / Maven — only score if test files likely exist
    has_test_files = any(
        f.is_file() and f.suffix.lower() in {".java", ".kt", ".scala", ".groovy"}
        and _is_test_file(f)
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


def check_coverage_config(repo_path, *, all_files=None, rng=None):
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
        elif re.search(r'\bcover(age)?\b', content):
            score = max(score, 50)
            evidence.append("Coverage-related target in Makefile")

    ci_dir = Path(repo_path) / ".github" / "workflows"
    if ci_dir.exists():
        for cf in list(ci_dir.glob("*.yml")) + list(ci_dir.glob("*.yaml")):
            content = read_file_safe(cf)
            if re.search(r'coverprofile|coverage|\bcodecov\b', content, re.IGNORECASE):
                score = max(score, 60)
                evidence.append(f"Coverage in CI workflow: {cf.name}")
                break

    pyproject = Path(repo_path) / "pyproject.toml"
    if pyproject.exists():
        content = read_file_safe(pyproject)
        if re.search(r'\[tool\.(coverage|pytest\.ini_options)\]', content) and "cov" in content.lower():
            score = max(score, 60)
            evidence.append("Coverage config in pyproject.toml")

    # Multiple coverage signals = high confidence
    if len(evidence) >= 2 and score < 100:
        score = min(score + 20, 100)
        evidence.append("Multiple coverage signals detected")

    if not evidence:
        evidence.append("No coverage configuration found")

    return min(score, 100), evidence


def check_ci_runs_tests(repo_path, *, all_files=None, rng=None):
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
        r'make\s+test', r'make\s+unittest', r'make\s+unit-test', r'make\s+unit_test',
        r'make\s+functest', r'make\s+e2e', r'make\s+check',
        r'go\s+test', r'pytest', r'python\s+-m\s+pytest',
        r'npm\s+(run\s+)?test', r'yarn\s+(run\s+)?test', r'vitest', r'jest',
        r'mvn\s+test', r'gradle\w*\s+test', r'cargo\s+test',
        r'tox\b', r'nox\b',
    ]

    for cf in ci_files:
        content = read_file_safe(cf)
        # Match both `pull_request:` (expanded) and `[push, pull_request]` (shorthand)
        file_has_pr = bool(re.search(r'\bpull_request\b(?!_target)', content))
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


def check_test_isolation(repo_path, *, all_files=None, rng=None):
    """Check if tests can run without external infrastructure."""
    test_files = [f for f in (all_files or [])
                  if f.is_file() and f.suffix.lower() in SOURCE_EXTS and _is_test_file(f)]

    if not test_files:
        return 0, ["No test files found"]

    sample = rng.sample(test_files, min(30, len(test_files))) if rng else test_files[:30]
    infra_patterns = [
        r'kubeconfig', r'kubectl', r'docker\.', r'http://localhost',
        r'127\.0\.0\.1', r'port.?forward', r'openshift',
        r'ClusterRole', r'ServiceAccount', r'Namespace\(',
    ]
    unit_patterns = [
        r'envtest', r'fake\.NewSimpleClientset', r'fake\.New', r'\bmock\b', r'\bMock\b',
        r'httptest\.NewServer', r'pytest', r'jest',
        r'//go:build\s+!e2e', r'//go:build\s+unit',
    ]
    e2e_tag_patterns = [
        r'//go:build\s+(test_)?e2e', r'//go:build\s+test_integration',
        r'//\s*\+build\s+(test_)?e2e', r'//\s*\+build\s+test_integration',
    ]

    infra_count = 0
    unit_count = 0

    for tf in sample:
        content = read_file_safe(tf, max_bytes=10000)
        has_infra = any(re.search(p, content) for p in infra_patterns)
        has_e2e_tag = any(re.search(p, content) for p in e2e_tag_patterns)
        has_unit = any(re.search(p, content) for p in unit_patterns)
        path_str = str(tf).lower()
        in_e2e_dir = '/e2e/' in path_str or '/integration/' in path_str

        if has_e2e_tag or (has_infra and not has_unit) or (in_e2e_dir and has_infra):
            infra_count += 1
        elif has_unit or (not has_infra and not in_e2e_dir):
            unit_count += 1

    makefile = Path(repo_path) / "Makefile"
    has_test_separation = False
    if makefile.exists():
        content = read_file_safe(makefile)
        if re.search(r'(unittest|unit-test|unit_test)\s*:', content) and re.search(r'(e2e|integration|functest)\s*:', content):
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
        evidence = [f"~{unit_pct:.0f}% unit tests, ~{100-unit_pct:.0f}% infra-dependent ({unit_count}/{total_classified} sampled)"]

    if has_test_separation:
        score = min(score + 15, 100)
        evidence.append("Makefile separates unit and integration test targets")

    return score, evidence


def check_pr_template(repo_path, *, all_files=None, rng=None):
    """Check if PR template exists with testing checklist."""
    pr_paths = [
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/pull_request_template.md",
        ".github/PULL_REQUEST_TEMPLATE/default.md",
    ]

    for pp in pr_paths:
        full_path = Path(repo_path) / pp
        if full_path.exists():
            content = read_file_safe(full_path).lower()
            score = 40
            evidence = [f"PR template found: {pp}"]

            if re.search(r'\btest', content):
                score += 30
                evidence.append("Mentions testing")
            if "- [ ]" in content or "- [x]" in content:
                score += 15
                evidence.append("Has checklist items")
            if re.search(r'\breview', content):
                score += 15
                evidence.append("Mentions review")

            return min(score, 100), evidence

    return 0, ["No PR template found"]


def check_linting_in_ci(repo_path, *, all_files=None, rng=None):
    """Check if linting/formatting runs in CI."""
    ci_dir = Path(repo_path) / ".github" / "workflows"
    if not ci_dir.exists():
        return 0, ["No CI workflows"]

    lint_patterns = [
        r'golangci-lint', r'make\s+lint', r'make\s+fmt', r'make\s+vet',
        r'make\s+precommit',
        r'\bblack\b', r'\bflake8\b', r'\bruff\b',
        r'\beslint\b', r'\bprettier\b',
        r'\bgofmt\b', r'\bgoimports\b', r'\trustfmt\b',
        r'\bpre-commit\b', r'\bisort\b',
        r'\byamllint\b', r'\bkube-linter\b', r'\bhelm\s+lint\b',
    ]

    found_in = []
    for cf in list(ci_dir.glob("*.yml")) + list(ci_dir.glob("*.yaml")):
        content = read_file_safe(cf)
        for lp in lint_patterns:
            if re.search(lp, content):
                found_in.append(cf.name)
                break

    if found_in:
        score = 80
        if len(found_in) >= 2:
            score = 100
        return score, [f"Linting in CI: {', '.join(found_in[:3])}"]

    makefile = Path(repo_path) / "Makefile"
    if makefile.exists():
        content = read_file_safe(makefile)
        if re.search(r'^(lint|fmt|format|vet)\s*:', content, re.MULTILINE):
            return 40, ["Lint targets in Makefile (but not confirmed in CI)"]

    return 0, ["No linting in CI detected"]


def check_contributing_guide(repo_path, *, all_files=None, rng=None):
    """Check for contributing guide or development documentation."""
    guide_files = [
        "CONTRIBUTING.md", "docs/CONTRIBUTING.md", "DEVELOPMENT.md",
        "docs/development.md", "docs/DEVELOPMENT.md", "HACKING.md",
        "docs/developer-guide.md",
    ]

    for gf in guide_files:
        if (Path(repo_path) / gf).exists():
            content = read_file_safe(Path(repo_path) / gf)
            score = 50
            evidence = [f"Found: {gf}"]

            dev_keywords = ["test", "build", "run", "setup", "install", "debug"]
            matches = sum(1 for kw in dev_keywords if re.search(rf'\b{kw}\b', content, re.IGNORECASE))
            score += min(matches * 10, 50)
            evidence.append(f"{matches}/{len(dev_keywords)} development keywords")
            return min(score, 100), evidence

    readme = Path(repo_path) / "README.md"
    if readme.exists():
        content = read_file_safe(readme)
        dev_sections = re.findall(r'^#+\s*(develop|contribut|getting started|setup|build)', content, re.MULTILINE | re.IGNORECASE)
        if dev_sections:
            return 40, [f"README has development sections: {', '.join(s.strip() for s in dev_sections[:3])}"]

    return 0, ["No contributing/development guide found"]


def check_architecture_docs(repo_path, *, all_files=None, rng=None):
    """Check for architecture documentation and module-level READMEs."""
    score = 0
    evidence = []

    arch_files = [
        "ARCHITECTURE.md", "docs/architecture.md", "docs/ARCHITECTURE.md",
        "docs/design.md", "docs/DESIGN.md",
    ]
    for af in arch_files:
        if (Path(repo_path) / af).exists():
            score += 40
            evidence.append(f"Architecture doc: {af}")
            break

    # ADR directory
    adr_dirs = ["docs/adr", "docs/ADR", "adr", "ADR", "docs/adrs"]
    for ad in adr_dirs:
        adr_path = Path(repo_path) / ad
        if adr_path.is_dir():
            adrs = [f for f in adr_path.iterdir() if f.is_file() and f.suffix.lower() == ".md"]
            if adrs:
                score += 30
                evidence.append(f"ADR directory: {ad} ({len(adrs)} records)")
                break

    # Module-level READMEs (subdirectories with their own README)
    module_readmes = 0
    for f in (all_files or []):
        if f.name.lower() == "readme.md" and f.parent != Path(repo_path):
            module_readmes += 1
    if module_readmes >= 3:
        score += 30
        evidence.append(f"{module_readmes} module-level READMEs")
    elif module_readmes >= 1:
        score += 15
        evidence.append(f"{module_readmes} module-level README(s)")

    if not evidence:
        evidence.append("No architecture documentation found")

    return min(score, 100), evidence


def check_fixture_data(repo_path, *, all_files=None, rng=None):
    """Check for test fixtures and sample data directories."""
    score = 0
    evidence = []

    fixture_dirs = [
        "testdata", "test/testdata", "tests/testdata",
        "fixtures", "test/fixtures", "tests/fixtures",
        "__fixtures__", "test/data", "tests/data",
        "samples", "examples",
    ]

    found_dirs = []
    total_files = 0
    for fd in fixture_dirs:
        fd_path = Path(repo_path) / fd
        if fd_path.is_dir():
            files = [f for f in fd_path.rglob("*") if f.is_file()]
            if files:
                found_dirs.append(fd)
                total_files += len(files)

    if found_dirs:
        score = 60
        if total_files >= 10:
            score = 90
        elif total_files >= 5:
            score = 80
        evidence.append(f"Fixture directories: {', '.join(found_dirs[:3])} ({total_files} files)")
    else:
        # Check for factory/fixture patterns in test files
        test_files = [f for f in (all_files or [])
                      if f.is_file() and f.suffix.lower() in SOURCE_EXTS and _is_test_file(f)]
        sample = (rng.sample(test_files, min(20, len(test_files))) if rng and test_files
                  else test_files[:20])
        factory_count = 0
        for tf in sample:
            content = read_file_safe(tf, max_bytes=5000)
            if re.search(r'\b(factory|fixture|mock_data|sample_data|test_data)\b', content, re.IGNORECASE):
                factory_count += 1
        if factory_count >= 3:
            score = 60
            evidence.append(f"Factory/fixture patterns in {factory_count}/{len(sample)} sampled test files")
        elif factory_count >= 1:
            score = 40
            evidence.append(f"Some fixture patterns in {factory_count}/{len(sample)} sampled test files")

    if not evidence:
        evidence.append("No test fixtures or sample data found")

    return min(score, 100), evidence


def check_build_setup(repo_path, *, all_files=None, rng=None):
    """Check for dependency lockfiles and build reproducibility."""
    score = 0
    evidence = []

    lockfiles = {
        "go.sum": "Go lockfile",
        "package-lock.json": "npm lockfile",
        "yarn.lock": "Yarn lockfile",
        "pnpm-lock.yaml": "pnpm lockfile",
        "poetry.lock": "Poetry lockfile",
        "Pipfile.lock": "Pipenv lockfile",
        "Cargo.lock": "Cargo lockfile",
        "Gemfile.lock": "Bundler lockfile",
        "uv.lock": "uv lockfile",
    }

    found_locks = []
    for lf, desc in lockfiles.items():
        if (Path(repo_path) / lf).exists():
            found_locks.append(desc)

    if found_locks:
        score = 60
        evidence.append(f"Lockfiles: {', '.join(found_locks[:3])}")

    # Check consistency: manifest without lockfile
    manifest_lock_pairs = [
        ("package.json", ["package-lock.json", "yarn.lock", "pnpm-lock.yaml"]),
        ("Gemfile", ["Gemfile.lock"]),
        ("Pipfile", ["Pipfile.lock"]),
        ("Cargo.toml", ["Cargo.lock"]),
    ]
    for manifest, locks in manifest_lock_pairs:
        if (Path(repo_path) / manifest).exists():
            if not any((Path(repo_path) / l).exists() for l in locks):
                evidence.append(f"{manifest} exists but no lockfile found")
                score = max(score - 10, 0)

    # Check for build targets in Makefile
    makefile = Path(repo_path) / "Makefile"
    if makefile.exists():
        content = read_file_safe(makefile)
        if re.search(r'^(build|install|deps|dependencies|setup)\s*:', content, re.MULTILINE):
            score += 20
            evidence.append("Build/install targets in Makefile")

    # Check for Dockerfile or devcontainer (reproducible environment)
    if (Path(repo_path) / "Dockerfile").exists() or (Path(repo_path) / "Containerfile").exists():
        score += 10
        evidence.append("Dockerfile/Containerfile for reproducible builds")
    if (Path(repo_path) / ".devcontainer" / "devcontainer.json").exists():
        score += 10
        evidence.append("Dev container configuration")

    if not evidence:
        evidence.append("No dependency lockfiles or build configuration found")

    return min(score, 100), evidence


def check_type_safety(repo_path, *, all_files=None, rng=None):
    """Check for type safety and static analysis configuration."""
    score = 0
    evidence = []

    langs = detect_languages(repo_path, all_files)

    # Statically typed languages get automatic credit
    typed_langs = {"Go", "Java", "Rust", "C++", "C"}
    typed_found = [l for l in langs if l in typed_langs]
    if typed_found:
        score = 80
        evidence.append(f"Statically typed language(s): {', '.join(typed_found)}")

    # Python type checking
    pyproject = Path(repo_path) / "pyproject.toml"
    if pyproject.exists():
        content = read_file_safe(pyproject)
        if "[tool.mypy]" in content or "[mypy]" in content:
            score = max(score, 80)
            evidence.append("mypy configured in pyproject.toml")
    if (Path(repo_path) / "mypy.ini").exists():
        score = max(score, 80)
        evidence.append("mypy.ini found")
    if (Path(repo_path) / "pyrightconfig.json").exists():
        score = max(score, 80)
        evidence.append("Pyright configured")
    if (Path(repo_path) / "py.typed").exists():
        score = max(score, 70)
        evidence.append("py.typed marker (PEP 561)")

    # TypeScript strict mode
    tsconfig = Path(repo_path) / "tsconfig.json"
    if tsconfig.exists():
        content = read_file_safe(tsconfig)
        if '"strict"' in content and "true" in content:
            score = max(score, 90)
            evidence.append("TypeScript strict mode enabled")
        else:
            score = max(score, 60)
            evidence.append("tsconfig.json found (strict mode not enabled)")

    # Python type annotation density (sample check)
    if "Python" in langs and score < 80:
        py_files = [f for f in (all_files or [])
                    if f.is_file() and f.suffix == ".py" and not is_generated_file(f) and not _is_test_file(f)]
        sample = rng.sample(py_files, min(20, len(py_files))) if rng and py_files else py_files[:20]
        annotated = 0
        for sf in sample:
            content = read_file_safe(sf, max_bytes=5000)
            if re.search(r'def\s+\w+\([^)]*:.*\)\s*(->\s*\w+)?:', content):
                annotated += 1
        if sample:
            ratio = annotated / len(sample)
            if ratio >= 0.5:
                score = max(score, 70)
                evidence.append(f"Type annotations in {annotated}/{len(sample)} sampled Python files")
            elif ratio >= 0.2:
                score = max(score, 50)
                evidence.append(f"Some type annotations ({annotated}/{len(sample)} sampled)")

    if not evidence:
        evidence.append("No type safety or static analysis configured")

    return min(score, 100), evidence


def check_dependency_complexity(repo_path, *, all_files=None, rng=None):
    """Check dependency count relative to codebase size."""
    score = 0
    evidence = []

    dep_count = 0

    # Go
    go_mod = Path(repo_path) / "go.mod"
    if go_mod.exists():
        content = read_file_safe(go_mod)
        # Count lines starting with tab inside require blocks
        in_require = False
        for line in content.splitlines():
            if line.strip().startswith("require"):
                in_require = True
            elif in_require and line.strip() == ")":
                in_require = False
            elif in_require and line.startswith("\t"):
                dep_count += 1

    # Python
    for req_file in ["requirements.txt", "requirements/base.txt"]:
        req_path = Path(repo_path) / req_file
        if req_path.exists():
            content = read_file_safe(req_path)
            dep_count += sum(1 for l in content.splitlines()
                           if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("-"))
            break

    pyproject = Path(repo_path) / "pyproject.toml"
    if pyproject.exists() and dep_count == 0:
        content = read_file_safe(pyproject)
        deps_match = re.search(r'dependencies\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if deps_match:
            dep_count += sum(1 for l in deps_match.group(1).splitlines() if l.strip().strip('",'))

    # Node
    pkg_json = Path(repo_path) / "package.json"
    if pkg_json.exists():
        content = read_file_safe(pkg_json)
        deps_match = re.search(r'"dependencies"\s*:\s*\{([^}]*)\}', content, re.DOTALL)
        if deps_match:
            dep_count += sum(1 for l in deps_match.group(1).splitlines() if ":" in l)

    source_files = _source_files_from(all_files or [])
    source_count = len(source_files)

    if source_count == 0:
        return 0, ["No source files found"]

    if dep_count == 0:
        return 80, ["No dependency manifest found or zero dependencies"]

    ratio = dep_count / source_count
    evidence.append(f"{dep_count} direct dependencies / {source_count} source files (ratio: {ratio:.2f})")

    if ratio <= 0.5:
        score = 90
    elif ratio <= 1.0:
        score = 70
    elif ratio <= 2.0:
        score = 50
    elif ratio <= 4.0:
        score = 30
    else:
        score = 10

    return score, evidence


def check_precommit_hooks(repo_path, *, all_files=None, rng=None):
    """Check for pre-commit hooks or local validation configuration."""
    score = 0
    evidence = []

    if (Path(repo_path) / ".pre-commit-config.yaml").exists():
        content = read_file_safe(Path(repo_path) / ".pre-commit-config.yaml")
        score = 70
        evidence.append(".pre-commit-config.yaml found")
        # Check for both linting and testing hooks
        has_lint = bool(re.search(r'\b(black|ruff|flake8|isort|prettier|eslint|gofmt|golangci)\b', content, re.IGNORECASE))
        has_test = bool(re.search(r'\b(pytest|test|mypy|pyright)\b', content, re.IGNORECASE))
        if has_lint and has_test:
            score = 100
            evidence.append("Includes both linting and type/test hooks")
        elif has_lint:
            score = 90
            evidence.append("Includes linting hooks")

    # Check for husky
    pkg_json = Path(repo_path) / "package.json"
    if pkg_json.exists():
        content = read_file_safe(pkg_json)
        if '"husky"' in content or '"prepare": "husky' in content:
            score = max(score, 70)
            evidence.append("Husky git hooks configured")

    if (Path(repo_path) / ".husky").is_dir():
        score = max(score, 70)
        evidence.append(".husky/ directory found")

    # Check for lefthook
    if (Path(repo_path) / "lefthook.yml").exists() or (Path(repo_path) / ".lefthook.yml").exists():
        score = max(score, 70)
        evidence.append("Lefthook configured")

    # Check for .githooks directory
    if (Path(repo_path) / ".githooks").is_dir():
        score = max(score, 60)
        evidence.append(".githooks/ directory found")

    if not evidence:
        evidence.append("No pre-commit hooks or local validation configured")

    return min(score, 100), evidence


# ---------------------------------------------------------------------------
# Check registry
# ---------------------------------------------------------------------------
CHECK_FUNCTIONS = {
    "agent_context": check_agent_context,
    "bug_template": check_bug_template,
    "structured_logging": check_structured_logging,
    "architecture_docs": check_architecture_docs,
    "fixture_data": check_fixture_data,
    "code_navigability": check_code_navigability,
    "generated_code": check_generated_code,
    "build_setup": check_build_setup,
    "type_safety": check_type_safety,
    "dependency_complexity": check_dependency_complexity,
    "codeowners": check_codeowners,
    "test_ratio": check_test_ratio,
    "test_execution": check_test_execution,
    "coverage_config": check_coverage_config,
    "ci_runs_tests": check_ci_runs_tests,
    "test_isolation": check_test_isolation,
    "precommit_hooks": check_precommit_hooks,
    "pr_template": check_pr_template,
    "linting_in_ci": check_linting_in_ci,
    "contributing_guide": check_contributing_guide,
}
