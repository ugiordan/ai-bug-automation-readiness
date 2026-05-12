"""Navigate phase checks: can the agent find the relevant code efficiently?"""

import random
import re
from pathlib import Path

from ..config import SOURCE_EXTS
from ..utils import count_lines_fast, detect_languages, is_generated_file, read_file_safe
from ._shared import _is_test_file, _source_files_from


def check_code_navigability(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
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
        evidence.append(f"Largest: {', '.join(f'{fname} ({lc}L)' for fname, lc in top3)}")

    return score, evidence


def check_generated_code(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check what percentage of source code is auto-generated."""
    all_source = [f for f in (all_files or []) if f.is_file() and f.suffix.lower() in SOURCE_EXTS]

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


def check_build_setup(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
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

    manifest_lock_pairs = [
        ("package.json", ["package-lock.json", "yarn.lock", "pnpm-lock.yaml"]),
        ("Gemfile", ["Gemfile.lock"]),
        ("Pipfile", ["Pipfile.lock"]),
        ("Cargo.toml", ["Cargo.lock"]),
    ]
    for manifest, locks in manifest_lock_pairs:
        if (Path(repo_path) / manifest).exists():
            if not any((Path(repo_path) / lk).exists() for lk in locks):
                evidence.append(f"{manifest} exists but no lockfile found")
                score = max(score - 10, 0)

    makefile = Path(repo_path) / "Makefile"
    if makefile.exists():
        content = read_file_safe(makefile)
        if re.search(r"^(build|install|deps|dependencies|setup)\s*:", content, re.MULTILINE):
            score += 20
            evidence.append("Build/install targets in Makefile")

    if (Path(repo_path) / "Dockerfile").exists() or (Path(repo_path) / "Containerfile").exists():
        score += 10
        evidence.append("Dockerfile/Containerfile for reproducible builds")
    if (Path(repo_path) / ".devcontainer" / "devcontainer.json").exists():
        score += 10
        evidence.append("Dev container configuration")

    if not evidence:
        evidence.append("No dependency lockfiles or build configuration found")

    return min(score, 100), evidence


def check_type_safety(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check for type safety and static analysis configuration."""
    score = 0
    evidence = []

    langs = detect_languages(repo_path, all_files)

    typed_langs = {"Go", "Java", "Rust", "C++", "C"}
    typed_found = [lang for lang in langs if lang in typed_langs]
    if typed_found:
        score = 80
        evidence.append(f"Statically typed language(s): {', '.join(typed_found)}")

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

    tsconfig = Path(repo_path) / "tsconfig.json"
    if tsconfig.exists():
        content = read_file_safe(tsconfig)
        if '"strict"' in content and "true" in content:
            score = max(score, 90)
            evidence.append("TypeScript strict mode enabled")
        else:
            score = max(score, 60)
            evidence.append("tsconfig.json found (strict mode not enabled)")

    if "Python" in langs and score < 80:
        py_files = [
            f
            for f in (all_files or [])
            if f.is_file() and f.suffix == ".py" and not is_generated_file(f) and not _is_test_file(f)
        ]
        sample = rng.sample(py_files, min(20, len(py_files))) if rng and py_files else py_files[:20]
        annotated = 0
        for sf in sample:
            content = read_file_safe(sf, max_bytes=5000)
            if re.search(r"def\s+\w+\([^)]*:.*\)\s*(->\s*\w+)?:", content):
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


def check_dependency_complexity(repo_path: str | Path, *, all_files: list[Path] | None = None, rng: random.Random | None = None) -> tuple[int, list[str]]:
    """Check dependency count relative to codebase size."""
    score = 0
    evidence = []

    dep_count = 0

    go_mod = Path(repo_path) / "go.mod"
    if go_mod.exists():
        content = read_file_safe(go_mod)
        in_require = False
        for line in content.splitlines():
            if line.strip().startswith("require"):
                in_require = True
            elif in_require and line.strip() == ")":
                in_require = False
            elif in_require and line.startswith("\t"):
                dep_count += 1

    for req_file in ["requirements.txt", "requirements/base.txt"]:
        req_path = Path(repo_path) / req_file
        if req_path.exists():
            content = read_file_safe(req_path)
            dep_count += sum(
                1
                for line in content.splitlines()
                if line.strip() and not line.strip().startswith("#") and not line.strip().startswith("-")
            )
            break

    pyproject = Path(repo_path) / "pyproject.toml"
    if pyproject.exists() and dep_count == 0:
        content = read_file_safe(pyproject)
        deps_match = re.search(r"dependencies\s*=\s*\[(.*?)\n\]", content, re.DOTALL)
        if deps_match:
            dep_count += sum(1 for line in deps_match.group(1).splitlines() if line.strip().strip('",'))

    pkg_json = Path(repo_path) / "package.json"
    if pkg_json.exists():
        content = read_file_safe(pkg_json)
        deps_match = re.search(r'"dependencies"\s*:\s*\{([^}]*)\}', content, re.DOTALL)
        if deps_match:
            dep_count += sum(1 for line in deps_match.group(1).splitlines() if ":" in line)

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
