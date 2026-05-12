# AI Bug Automation Readiness Assessment

## Overview

CLI tool that evaluates whether Git repositories are ready for AI agents to autonomously find, fix, and verify bugs. Scores repos 0-100 across 20 checks in four phases: Understand, Navigate, Verify, Submit.

## Architecture

```
assess.py          # Entry point (thin wrapper)
assess/
  cli.py           # CLI argument parsing, report orchestration
  engine.py        # Core assessment: runs checks, computes weighted scores
  config.py        # Check definitions, weights (must sum to 100), recommendations
  checks.py        # 20 check functions, all with signature:
                    #   (repo_path, *, all_files=None, rng=None) -> (score, evidence)
  utils.py         # File discovery, language detection, caching
  profiles.py      # 3-layer profile resolution for check exclusions
  scan_config.py   # Multi-org scan config validation
  reports/
    __init__.py    # Shared report data preparation
    html.py        # HTML report with Chart.js visualizations
    markdown.py    # Markdown tables
    csv_report.py  # CSV export
    docx_report.py # DOCX generation (requires python-docx)
tests/             # pytest test suite
```

## Development

```bash
make setup     # Install all dependencies
make test      # Run test suite (pytest)
make lint      # Run ruff + mypy
make format    # Auto-format with ruff
make coverage  # Run tests with coverage report
```

## How to run

```bash
# Single repo
python assess.py /path/to/repo

# Batch scan
python assess.py --batch /path/to/repos --format html -o report.html

# CI gating
python assess.py --batch /repos --fail-under 60
```

## Key conventions

- Core modules use stdlib only. The only external dependency is python-docx (optional, for DOCX reports).
- All check functions share the same signature: `def check_name(repo_path, *, all_files=None, rng=None) -> tuple[int, list[str]]` returning (score 0-100, evidence list).
- Check weights are defined in `assess/config.py` and must sum to 100.
- A single filesystem traversal (`find_all_files_cached`) is shared across all checks for performance.
- The `rng` parameter uses a seeded `random.Random` per repo (MD5 of repo name) for deterministic sampling.
- Generated files are detected and excluded from navigability and test ratio analysis.

## Adding a new check

1. Write the check function in `assess/checks.py` following the standard signature
2. Add the check to `CHECK_FUNCTIONS` dict at the bottom of checks.py
3. Add weight and metadata to `CHECKS` dict in `assess/config.py` (adjust weights to sum to 100)
4. Add a recommendation string to `RECOMMENDATIONS` in config.py
5. Write tests in `tests/test_checks.py`

## Debugging

Run a single repo with text output to see per-check scores and recommendations:
```bash
python assess.py /path/to/repo
```

Use `--list-checks` to see all checks and weights:
```bash
python assess.py --list-checks
```

Use `--profile` or `--exclude-checks` to skip specific checks:
```bash
python assess.py /path/to/repo --exclude-checks coverage_config test_ratio
```
