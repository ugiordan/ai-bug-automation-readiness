"""Submit phase checks: can the agent submit the fix following project conventions?"""

import random
import re
from pathlib import Path

from ..utils import read_file_safe


def check_codeowners(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for CODEOWNERS file."""
    paths = [".github/CODEOWNERS", "CODEOWNERS", "docs/CODEOWNERS"]
    for p in paths:
        full = Path(repo_path) / p
        if full.exists():
            content = read_file_safe(full)
            lines = [line.strip() for line in content.splitlines() if line.strip() and not line.strip().startswith("#")]
            if len(lines) >= 3:
                return 100, [f"CODEOWNERS found ({p}) with {len(lines)} rules"]
            elif lines:
                return 60, [f"CODEOWNERS found ({p}) with {len(lines)} rules (sparse)"]
            else:
                return 30, [f"CODEOWNERS found ({p}) but empty"]

    if (Path(repo_path) / "OWNERS").exists():
        content = read_file_safe(Path(repo_path) / "OWNERS")
        lines = [line.strip() for line in content.splitlines() if line.strip() and not line.strip().startswith("#")]
        has_aliases = (Path(repo_path) / "OWNERS_ALIASES").exists()
        if len(lines) >= 3 or has_aliases:
            return 100, [
                "OWNERS file found (OpenShift/Kubernetes-style)"
                + (", OWNERS_ALIASES present" if has_aliases else f", {len(lines)} entries")
            ]
        elif lines:
            return 70, [f"OWNERS file found (OpenShift/Kubernetes-style, {len(lines)} entries)"]
        else:
            return 30, ["OWNERS file found but empty"]

    return 0, ["No CODEOWNERS or OWNERS file"]


def check_pr_template(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
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

            if re.search(r"\btest", content):
                score += 30
                evidence.append("Mentions testing")
            if "- [ ]" in content or "- [x]" in content:
                score += 15
                evidence.append("Has checklist items")
            if re.search(r"\breview", content):
                score += 15
                evidence.append("Mentions review")

            return min(score, 100), evidence

    return 0, ["No PR template found"]


def check_linting_in_ci(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check if linting/formatting runs in CI."""
    ci_dir = Path(repo_path) / ".github" / "workflows"

    lint_patterns = [
        r"golangci-lint",
        r"make\s+lint",
        r"make\s+fmt",
        r"make\s+vet",
        r"make\s+precommit",
        r"\bblack\b",
        r"\bflake8\b",
        r"\bruff\b",
        r"\beslint\b",
        r"\bprettier\b",
        r"\bgofmt\b",
        r"\bgoimports\b",
        r"\brustfmt\b",
        r"\bpre-commit\b",
        r"\bisort\b",
        r"\byamllint\b",
        r"\bkube-linter\b",
        r"\bhelm\s+lint\b",
    ]

    found_in = []
    if ci_dir.exists():
        for cf in list(ci_dir.glob("*.yml")) + list(ci_dir.glob("*.yaml")):
            content = read_file_safe(cf)
            for pat in lint_patterns:
                if re.search(pat, content):
                    found_in.append(cf.name)
                    break

    if found_in:
        score = 80
        if len(found_in) >= 2:
            score = 100
        return score, [f"Linting in CI: {', '.join(found_in[:3])}"]

    precommit_cfg = Path(repo_path) / ".pre-commit-config.yaml"
    if precommit_cfg.exists():
        content = read_file_safe(precommit_cfg)
        precommit_lint_patterns = [
            r"\b(black|ruff|flake8|isort|prettier|eslint|gofmt|golangci|autopep8|pylint|mypy|pyright)\b",
        ]
        has_lint = any(re.search(p, content, re.IGNORECASE) for p in precommit_lint_patterns)
        if has_lint:
            has_ci_key = bool(re.search(r"^ci\s*:", content, re.MULTILINE))
            if has_ci_key:
                return 100, ["Linting via pre-commit.ci (ci: key in .pre-commit-config.yaml)"]
            return 80, ["Linting via .pre-commit-config.yaml (lint hooks configured)"]

    makefile = Path(repo_path) / "Makefile"
    if makefile.exists():
        content = read_file_safe(makefile)
        if re.search(r"^(lint|fmt|format|vet)\s*:", content, re.MULTILINE):
            return 40, ["Lint targets in Makefile (but not confirmed in CI)"]

    if not ci_dir.exists():
        return 0, ["No CI workflows"]

    return 0, ["No linting in CI detected"]


def check_contributing_guide(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for contributing guide or development documentation."""
    guide_files = [
        "CONTRIBUTING.md",
        "CONTRIBUTING.rst",
        "CONTRIBUTING.txt",
        "docs/CONTRIBUTING.md",
        ".github/CONTRIBUTING.md",
        "DEVELOPMENT.md",
        "docs/development.md",
        "docs/DEVELOPMENT.md",
        "HACKING.md",
        "docs/HACKING.md",
        "docs/developer-guide.md",
        "docs/DEVELOPER_GUIDE.md",
        "docs/developer_guide.md",
    ]

    dev_keywords = ["test", "build", "run", "setup", "install", "debug"]
    best_score = 0
    best_evidence: list[str] = []

    for gf in guide_files:
        if (Path(repo_path) / gf).exists():
            content = read_file_safe(Path(repo_path) / gf)
            score = 50
            evidence = [f"Found: {gf}"]

            matches = sum(1 for kw in dev_keywords if re.search(rf"\b{kw}\b", content, re.IGNORECASE))
            score += min(matches * 10, 50)
            evidence.append(f"{matches}/{len(dev_keywords)} development keywords")
            score = min(score, 100)
            if score > best_score:
                best_score = score
                best_evidence = evidence

    if best_score > 0:
        return best_score, best_evidence

    readme = Path(repo_path) / "README.md"
    if readme.exists():
        content = read_file_safe(readme)
        dev_sections = re.findall(
            r"^#+\s*(develop|contribut|getting started|setup|build)", content, re.MULTILINE | re.IGNORECASE
        )
        if dev_sections:
            return 40, [f"README has development sections: {', '.join(s.strip() for s in dev_sections[:3])}"]

    return 0, ["No contributing/development guide found"]
