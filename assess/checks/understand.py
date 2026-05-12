"""Understand phase checks: can the agent understand the bug from the report and codebase?"""

import random
import re
from pathlib import Path

from ..config import SOURCE_EXTS
from ..utils import is_generated_file, read_file_safe
from ._shared import _is_test_file


def check_agent_context(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for CLAUDE.md, AGENTS.md, or similar AI context files."""
    score = 0
    evidence = []

    context_files = [
        "CLAUDE.md",
        "claude.md",
        "AGENTS.md",
        "Agents.md",
        "agents.md",
        "COPILOT.md",
        ".cursorrules",
        "CONTEXT.md",
    ]
    found = []
    for cf in context_files:
        if (Path(repo_path) / cf).exists():
            found.append(cf)
            content = read_file_safe(Path(repo_path) / cf)
            quality_keywords = ["test", "debug", "architecture", "structure", "run", "build", "make"]
            matches = sum(1 for kw in quality_keywords if re.search(rf"\b{kw}\b", content, re.IGNORECASE))
            score += 20 + min(matches * 12, 80)
            evidence.append(f"{cf} found ({matches}/{len(quality_keywords)} quality keywords)")

    if not found:
        evidence.append("No AI context files found (CLAUDE.md, AGENTS.md, etc.)")
        score = 0

    return min(score, 100), evidence


# ---------------------------------------------------------------------------
# Bug template checking (GitHub + Jira)
# ---------------------------------------------------------------------------

_JIRA_URL_RE = re.compile(
    r"https?://[^\s)\]]*(?:jira|issues\.redhat\.com|atlassian\.net)[^\s)\]]*",
    re.IGNORECASE,
)

_JIRA_BUG_INSTRUCTION_RE = re.compile(
    r"(?:bug|issue|defect|problem|report).{0,200}(?:jira|issues\.redhat\.com|atlassian\.net)"
    r"|(?:jira|issues\.redhat\.com|atlassian\.net).{0,200}(?:bug|issue|track|report)",
    re.IGNORECASE,
)

_NON_JIRA_PREFIXES = frozenset(
    {
        "UTF",
        "SHA",
        "ISO",
        "HTTP",
        "TLS",
        "RFC",
        "TCP",
        "UDP",
        "SSL",
        "AES",
        "RSA",
        "DSA",
        "ARM",
        "AMD",
        "PCI",
        "USB",
        "API",
        "SDK",
    }
)

_JIRA_PROJECT_KEY_RE = re.compile(r"\b([A-Z][A-Z0-9]{1,9})-\d+\b")


def _has_jira_project_keys(text: str) -> bool:
    """Check if text contains Jira project key references, filtering out
    common abbreviations like UTF-8, SHA-256, HTTP-200, etc."""
    for m in _JIRA_PROJECT_KEY_RE.finditer(text):
        if m.group(1) not in _NON_JIRA_PREFIXES:
            return True
    return False


def _check_github_bug_template(repo_path: str | Path) -> tuple[int, list[str]]:
    """Check for GitHub issue bug report templates. Returns (score, evidence)."""
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

    for tp in template_paths:
        full_path = Path(repo_path) / tp
        if full_path.exists():
            content = read_file_safe(full_path).lower()

            is_bug_template = True
            if tp.endswith(".md"):
                frontmatter = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
                if frontmatter:
                    fm_text = frontmatter.group(1)
                    name_match = re.search(r"^name\s*:.*\b(bug|defect|problem)\b", fm_text, re.MULTILINE)
                    about_match = re.search(r"^about\s*:.*\b(bug|issue|problem|defect)\b", fm_text, re.MULTILINE)
                    if not name_match and not about_match:
                        is_bug_template = False
                        evidence.append(f"Found {tp} but name/about fields don't indicate a bug template")

            if not is_bug_template:
                return 15, evidence

            score = 30

            if re.search(r"\b(reproduc|repro\b|steps to|steps did)", content):
                score += 25
                evidence.append("Has reproduction steps")

            if re.search(r"\bexpect(ed)?\b.*\bactual\b|\bactual\b.*\bexpect(ed)?\b|\bbehavior\b", content):
                score += 20
                evidence.append("Has expected/actual behavior fields")

            if re.search(r"\benvironment\b|\bversion\b|\bplatform\b", content):
                score += 15
                evidence.append("Has environment/version fields")

            if re.search(r"\blog(s|ging)?\b|\berror\b|\bstack.?trace\b|\boutput\b", content):
                score += 10
                evidence.append("Has log/error output fields")

            if tp.endswith((".yml", ".yaml")):
                if "required: true" in content or "required:true" in content:
                    score += 10
                    evidence.append("YAML template with required fields")

            evidence.insert(0, f"Found: {tp}")
            return min(score, 100), evidence

    template_dir = Path(repo_path) / ".github" / "ISSUE_TEMPLATE"
    if template_dir.exists():
        templates = [t for t in template_dir.iterdir() if t.is_file()]
        if templates:
            evidence.append(f"Issue templates exist ({len(templates)}) but no dedicated bug template")
            return 15, evidence
        evidence.append("Empty .github/ISSUE_TEMPLATE/ directory")
    else:
        evidence.append("No .github/ISSUE_TEMPLATE/ directory")

    return 0, evidence


def _check_jira_bug_tracking(repo_path: str | Path) -> tuple[int, list[str]]:
    """Check for Jira-based bug tracking references. Returns (score, evidence)."""
    score = 0
    evidence = []

    for config_name in ("config.yml", "config.yaml"):
        config_path = Path(repo_path) / ".github" / "ISSUE_TEMPLATE" / config_name
        if not config_path.exists():
            continue
        config_content = read_file_safe(config_path)
        if _JIRA_URL_RE.search(config_content):
            score = 30
            evidence.append(f"GitHub issue {config_name} redirects to Jira")
            if re.search(r"blank_issues_enabled\s*:\s*false", config_content, re.IGNORECASE):
                score += 10
                evidence.append("GitHub blank issues disabled (Jira-only)")
        break

    doc_files = ["CONTRIBUTING.md", "README.md"]
    for doc in doc_files:
        doc_path = Path(repo_path) / doc
        if not doc_path.exists():
            continue
        content = read_file_safe(doc_path)
        if not _JIRA_URL_RE.search(content):
            continue

        evidence.append(f"Jira link found in {doc}")

        if _JIRA_BUG_INSTRUCTION_RE.search(content):
            score = max(score, 50)
            evidence.append(f"Explicit bug/issue reporting via Jira in {doc}")

            if re.search(r"\b(reproduc|repro\b|steps to)", content, re.IGNORECASE):
                score += 10
                evidence.append("Jira instructions mention reproduction steps")

            if _has_jira_project_keys(content):
                score += 10
                evidence.append("References specific Jira project keys")

            break

        score = max(score, 20)
        evidence.append(f"Jira mentioned in {doc} without explicit bug reporting instructions")

        if _has_jira_project_keys(content):
            score += 5
            evidence.append("References specific Jira project keys")

    return min(score, 70), evidence


def check_bug_template(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check if bug report template or Jira-based tracking exists."""
    github_score, github_evidence = _check_github_bug_template(repo_path)
    jira_score, jira_evidence = _check_jira_bug_tracking(repo_path)

    if github_score == 0 and jira_score == 0:
        return 0, github_evidence + jira_evidence
    if github_score >= jira_score:
        return github_score, github_evidence
    return jira_score, jira_evidence


def check_structured_logging(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for structured logging patterns."""
    score = 0
    evidence = []

    dep_files = ["go.mod", "requirements.txt", "pyproject.toml", "package.json", "Cargo.toml"]
    logging_libs = {
        r"\bzap\b": "Go structured logging (zap)",
        r"\blogr\b": "Go structured logging (logr)",
        r"\bzerolog\b": "Go structured logging (zerolog)",
        r"\bstructlog\b": "Python structured logging",
        r"\bloguru\b": "Python structured logging",
        r"\bwinston\b": "Node structured logging",
        r"\bpino\b": "Node structured logging",
        r"log/slog": "Go structured logging (slog)",
        r"k8s\.io/klog": "Kubernetes-style logging (klog)",
        r"\bslf4j\b": "Java structured logging (SLF4J)",
        r"\blogback\b": "Java structured logging (Logback)",
        r"\blog4j": "Java structured logging (Log4j)",
        r'"@sentry/': "Frontend error tracking (Sentry)",
        r"\bsentry-sdk\b": "Frontend error tracking (Sentry)",
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
    source_files = [
        f
        for f in files
        if f.is_file() and f.suffix.lower() in {".go", ".py", ".ts", ".js", ".java", ".kt"} and not is_generated_file(f)
    ]
    sample = rng.sample(source_files, min(50, len(source_files))) if source_files and rng else source_files[:50]

    log_patterns = 0
    error_wrap_patterns = 0

    for sf in sample:
        content = read_file_safe(sf)
        if (
            re.search(r"\.(Info|Warn|Error|Debug)\(", content)
            or re.search(
                r"(?:log|logger|logging|_log|_logger)\.(info|warn(?:ing)?|error|debug)\(", content, re.IGNORECASE
            )
            or re.search(r"console\.(error|warn|info|debug)\(", content)
            or re.search(r"Sentry\.(captureException|captureMessage)", content)
        ):
            log_patterns += 1
        if re.search(
            r"(fmt\.Errorf|errors\.Wrap|errors\.New|raise \w+Error|throw new \w*Error|ErrorBoundary)", content
        ):
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


def check_architecture_docs(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for architecture documentation and module-level READMEs."""
    score = 0
    evidence = []

    arch_files = [
        "ARCHITECTURE.md",
        "docs/architecture.md",
        "docs/ARCHITECTURE.md",
        "docs/design.md",
        "docs/DESIGN.md",
    ]
    for af in arch_files:
        if (Path(repo_path) / af).exists():
            score += 40
            evidence.append(f"Architecture doc: {af}")
            break

    adr_dirs = ["docs/adr", "docs/ADR", "adr", "ADR", "docs/adrs"]
    for ad in adr_dirs:
        adr_path = Path(repo_path) / ad
        if adr_path.is_dir():
            adrs = [f for f in adr_path.iterdir() if f.is_file() and f.suffix.lower() == ".md"]
            if adrs:
                score += 30
                evidence.append(f"ADR directory: {ad} ({len(adrs)} records)")
                break

    module_readmes = 0
    for f in all_files or []:
        if f.name.lower() == "readme.md" and f.parent != Path(repo_path):
            module_readmes += 1
    if module_readmes >= 5:
        score += 40
        evidence.append(f"{module_readmes} module-level READMEs")
    elif module_readmes >= 3:
        score += 30
        evidence.append(f"{module_readmes} module-level READMEs")
    elif module_readmes >= 1:
        score += 15
        evidence.append(f"{module_readmes} module-level README(s)")

    if not evidence:
        evidence.append("No architecture documentation found")

    return min(score, 100), evidence


def check_fixture_data(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for test fixtures and sample data directories."""
    score = 0
    evidence = []

    fixture_dirs = [
        "testdata",
        "test/testdata",
        "tests/testdata",
        "fixtures",
        "test/fixtures",
        "tests/fixtures",
        "__fixtures__",
        "test/data",
        "tests/data",
        "samples",
        "examples",
        "config/samples",
        "config/examples",
        "test/resources",
        "tests/resources",
        "manifests/testdata",
        "manifests/test",
        "config/testdata",
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
        manifest_parents = {"manifests", "kustomize", "config", "deploy"}
        test_parents = {"e2e", "test", "testdata", "testing"}
        manifest_test_files = [
            f
            for f in (all_files or [])
            if f.is_file()
            and f.suffix.lower() in (".yaml", ".yml", ".json")
            and manifest_parents.intersection(p.lower() for p in f.parts)
            and test_parents.intersection(p.lower() for p in f.parts)
        ]
        if manifest_test_files:
            score = 50
            if len(manifest_test_files) >= 5:
                score = 70
            evidence.append(f"Test manifests in overlay/config dirs ({len(manifest_test_files)} files)")
        else:
            test_files = [
                f for f in (all_files or []) if f.is_file() and f.suffix.lower() in SOURCE_EXTS and _is_test_file(f)
            ]
            sample = rng.sample(test_files, min(20, len(test_files))) if rng and test_files else test_files[:20]
            factory_count = 0
            for tf in sample:
                content = read_file_safe(tf, max_bytes=5000)
                if re.search(r"\b(factory|fixture|mock_data|sample_data|test_data)\b", content, re.IGNORECASE):
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
