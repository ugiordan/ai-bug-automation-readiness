# AI Bug Automation Readiness

Assess whether repositories are ready for AI agents to autonomously find, fix, and verify bugs.

Unlike general "AI readiness" tools that check if documentation exists, this tool evaluates what actually matters for autonomous bug fixing: can the agent understand the bug, navigate the code, run tests to verify a fix, and submit it properly?

## Installation

```bash
# Clone and run directly (zero dependencies for core formats)
git clone https://github.com/ugiordan/ai-bug-automation-readiness.git
cd ai-bug-automation-readiness
python assess.py /path/to/repo

# Optional: DOCX format support
pip install python-docx
```

Requires Python 3.10+.

## Usage

```bash
# Single repo
python assess.py /path/to/repo

# Single repo, JSON output
python assess.py /path/to/repo --format json

# Batch scan with HTML report
python assess.py --batch /path/to/repos --format html --org your-org -o report.html

# Batch scan with markdown report
python assess.py --batch /path/to/repos --format markdown --org your-org -o report.md

# CSV for spreadsheet import
python assess.py --batch /path/to/repos --format csv -o scores.csv

# DOCX for Google Docs (requires python-docx)
python assess.py --batch /path/to/repos --format docx --org your-org -o report.docx

# CI gating: exit 1 if any repo scores below 60
python assess.py --batch /path/to/repos --fail-under 60

# Pipe JSON without progress noise (progress goes to stderr)
python assess.py /path/to/repo --format json | jq .overall_score

# Exclude specific repos in batch mode
python assess.py --batch /path/to/repos --exclude archived-repo legacy-tool

# Quiet mode (suppress progress output)
python assess.py --batch /path/to/repos --format json -q -o results.json

# List all checks and weights
python assess.py --list-checks
```

## CLI Flags

| Flag | Description |
|---|---|
| `repo` | Path to a single repository (positional) |
| `--batch PATH` | Scan all git repos in a directory |
| `--format FORMAT` | Output format: text, json, html, markdown, csv, docx |
| `--output / -o PATH` | Write output to file instead of stdout |
| `--org NAME` | GitHub org for report links (e.g., `opendatahub-io`) |
| `--title TEXT` | Custom report title |
| `--fail-under N` | Exit 1 if any repo scores below N (0-100) |
| `--exclude REPO...` | Skip specific repos in batch mode |
| `--quiet / -q` | Suppress progress output |
| `--list-checks` | List all checks and weights, then exit |
| `--version` | Show version number |

### Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success (all repos above threshold if `--fail-under` set) |
| 1 | `--fail-under` threshold not met |
| 2 | Error (invalid args, no repos found, missing dependency) |

## What It Checks

The tool evaluates 14 checks across 4 phases of an AI bug-fixing workflow:

### Understand (22%)
Can the agent understand the bug from the report and codebase context?

| Check | Weight | What it measures |
|---|---|---|
| AI Context Files | 5% | CLAUDE.md, AGENTS.md with quality keywords (test, debug, build) |
| Bug Report Template Quality | 12% | Reproduction steps, expected/actual behavior, environment, logs. Validates frontmatter name/about fields to avoid false positives. |
| Structured Logging | 5% | Logging frameworks, error wrapping patterns |

### Navigate (13%)
Can the agent find the relevant code efficiently?

| Check | Weight | What it measures |
|---|---|---|
| Code Navigability | 8% | Average file size (excluding generated files), language-aware thresholds |
| Generated Code Ratio | 5% | Percentage of auto-generated files (zz_generated, .pb.go, etc.) |

### Verify (49%)
Can the agent run tests to verify the fix works?

| Check | Weight | What it measures |
|---|---|---|
| Test-to-Source Ratio | 17% | Ratio of test files to source files (excluding test helpers) |
| One-Command Test Execution | 12% | Makefile targets, npm scripts, pytest/tox/nox config, Gradle/Maven |
| CI Runs Tests on PRs | 10% | CI workflows triggered by pull_request (both expanded and shorthand syntax) |
| Coverage Configuration | 5% | Coverage flags (-coverprofile), codecov integration |
| Test Isolation | 5% | Unit vs integration test separation using mock/fake patterns, build tags, directory structure |

### Submit (16%)
Can the agent submit the fix following project conventions?

| Check | Weight | What it measures |
|---|---|---|
| Linting in CI | 5% | Lint/format steps in CI workflows |
| Contributing Guide | 5% | CONTRIBUTING.md with build/test/debug instructions |
| Code Ownership | 3% | CODEOWNERS or OWNERS file for review assignment |
| PR Template | 3% | Pull request template with testing checklist |

## Scoring

**Overall score** = weighted average of 14 checks, each scored 0-100. Weights are fixed to ensure consistent, comparable scores across repositories.

**Readiness levels:**

| Level | Score | Meaning |
|---|---|---|
| Ready | 80+ | Strong test infrastructure, good context, CI validates fixes |
| Partially Ready | 60-79 | Workable but has gaps that may cause AI agent failures |
| Needs Work | 40-59 | Missing key capabilities; fix gaps before AI bug bash |
| Not Ready | <40 | Fundamental gaps in test infrastructure or code structure |

### Verify Phase Gate

A repo without test infrastructure cannot support autonomous bug fixing, regardless of how good its documentation is. If the average Verify phase score is below 50, the overall score gets a smooth multiplier penalty that scales linearly from x0.4 (verify avg = 0) to x1.0 (verify avg = 50). This eliminates cliff effects from step thresholds.

## Key Design Decisions

- **Generated files are excluded** from navigability and test ratio analysis (zz_generated, .pb.go, openapi_generated, etc.)
- **Single filesystem traversal** per repo — all checks share the same file list for 3-5x faster scanning
- **Word-boundary matching** prevents false positives (e.g., "log" no longer matches "blog" or "catalog")
- **Only direct dependencies** are scanned for logging libraries (go.mod, not go.sum)
- **CI checks correlate PR trigger and test step** within the same workflow file to avoid false positives
- **Bug template frontmatter validation** checks name/about fields specifically, not just any occurrence of "bug" in labels
- **Subdirectory Makefile scanning** detects test targets in monorepo subdirectories (e.g., `ray-operator/Makefile`)
- **Test isolation uses mock/fake patterns** instead of generic framework markers (testing.T, testify) that appear in all Go tests
- **Test helper exclusion** avoids inflating test counts with infrastructure files (matchers, mocks, schemes, utils)
- **Deterministic results** via per-repo seeded local RNG ensures reproducible, thread-safe scores
- **Language-aware thresholds** for file size (Go/Java files are typically longer than Python/JS)
- **Per-check recommendations** tell you exactly what to fix, not just what's wrong
- **HTML output is XSS-safe** with all user-derived values escaped, Chart.js loaded with SRI integrity

## Output Formats

| Format | Dependencies | Description |
|---|---|---|
| text | none | Terminal-friendly summary with per-check details (single repo) |
| json | none | Machine-readable for trend tracking and CI integration |
| markdown | none | Tables for wikis, GitHub issues, or Google Docs import |
| csv | none | Spreadsheet-friendly (Google Sheets, Excel) |
| html | none | Visual report with charts, heatmap, per-repo details |
| docx | python-docx | Google Docs / Word with formatted tables and color coding |

## Related Tools

- **[AgentReady](https://github.com/ambient-code/agentready)** assesses general AI coding readiness across 25 broad attributes (type annotations, lock files, naming conventions, etc.). This tool focuses narrowly on bug-fixing workflow readiness with deeper checks on test infrastructure. They measure different things and serve different purposes.

## Examples

See the [`docs/`](docs/) folder for sample reports generated from an OpenDataHub ecosystem scan (128 repos): HTML, markdown, JSON, CSV, and DOCX.

The HTML report is also available via [GitHub Pages](https://ugiordan.github.io/ai-bug-automation-readiness/report.html).

## Requirements

- Python 3.10+
- No external dependencies for core formats (stdlib only)
- Optional: `python-docx` for DOCX format (`pip install python-docx`)
