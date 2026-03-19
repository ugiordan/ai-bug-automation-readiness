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

The tool evaluates 20 checks across 4 phases of an AI bug-fixing workflow:

### Understand (24%)
Can the agent understand the bug from the report and codebase context?

| Check | Weight | What it measures |
|---|---|---|
| AI Context Files | 8% | AGENTS.md, CLAUDE.md with quality keywords (test, debug, build) |
| Bug Report Template Quality | 8% | Reproduction steps, expected/actual behavior, environment, logs |
| Structured Logging | 3% | Logging frameworks (zap, logr, SLF4J, structlog, Sentry), error wrapping |
| Architecture Documentation | 3% | ARCHITECTURE.md, ADRs, module-level READMEs |
| Test Fixtures / Sample Data | 2% | testdata/, fixtures/, examples/ directories |

### Navigate (17%)
Can the agent find the relevant code efficiently?

| Check | Weight | What it measures |
|---|---|---|
| Code Navigability | 5% | Average file size (excluding generated files), language-aware thresholds |
| Generated Code Ratio | 2% | Percentage of auto-generated files (zz_generated, .pb.go, etc.) |
| Build / Dependency Setup | 5% | Lockfiles, build targets, reproducible environment |
| Type Safety / Static Analysis | 3% | mypy, tsconfig strict, typed languages (Go, Java, Rust) |
| Dependency Complexity | 2% | Direct dependency count relative to codebase size |

### Verify (46%)
Can the agent run tests to verify the fix works?

| Check | Weight | What it measures |
|---|---|---|
| Test-to-Source Ratio | 15% | Ratio of test files to source files (excluding test helpers), frontend-aware thresholds |
| One-Command Test Execution | 11% | Makefile targets, npm scripts, pytest/tox/nox config, Gradle/Maven |
| CI Runs Tests on PRs | 10% | CI workflows triggered by pull_request with test steps |
| Coverage Configuration | 3% | Coverage flags (-coverprofile), codecov integration |
| Test Isolation | 4% | Unit vs integration test separation using mock/fake patterns, build tags |
| Pre-commit / Local Hooks | 3% | .pre-commit-config.yaml, husky, lefthook for fast local feedback |

### Submit (13%)
Can the agent submit the fix following project conventions?

| Check | Weight | What it measures |
|---|---|---|
| Linting in CI | 5% | Lint/format steps in CI workflows |
| Contributing Guide | 5% | CONTRIBUTING.md with build/test/debug instructions |
| Code Ownership | 1% | CODEOWNERS or OWNERS/OWNERS_ALIASES file for review assignment |
| PR Template | 2% | Pull request template with testing checklist |

### Non-Code Repos

Repos with fewer than 3 source files (docs, config, governance repos) are automatically classified as "Not Applicable" and excluded from scoring. They appear in a separate section of the report.

## Scoring

**Overall score** = weighted average of 20 checks, each scored 0-100. Weights are fixed to ensure consistent, comparable scores across repositories.

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

- **Non-code repos excluded** — repos with <3 source files (docs, config) are marked "Not Applicable" and excluded from scoring
- **Generated files are excluded** from navigability and test ratio analysis (zz_generated, .pb.go, openapi_generated, etc.)
- **Single filesystem traversal** per repo — all checks share the same file list for 3-5x faster scanning
- **Java test naming** supported — `FooTest.java` and `FooTests.java` patterns detected alongside `_test.go`, `test_*.py`
- **CI checks exclude pull_request_target** — only `pull_request` triggers count for PR test validation
- **Build tool validation** — Gradle/Maven only score high if test files actually exist (not just `pom.xml` presence)
- **package.json scoped** — test detection limited to `"scripts"` block to avoid matching config keys
- **Typed language detection** — Go, Java, Rust, C++ automatically score high on type safety; Python/JS scored on tooling
- **Subdirectory Makefile scanning** detects test targets in monorepo subdirectories
- **Test helper exclusion** avoids inflating test counts with infrastructure files (matchers, mocks, schemes, utils)
- **Deterministic results** via per-repo seeded local RNG ensures reproducible, thread-safe scores
- **Per-check recommendations** tell you exactly what to fix, not just what's wrong
- **OWNERS/OWNERS_ALIASES** treated as equivalent to CODEOWNERS (common in OpenShift/Kubernetes projects)
- **Frontend-aware test ratio** — TS/JS-heavy repos (>60% of source) use relaxed thresholds since component files inflate source counts
- **Frontend logging detection** — recognizes Sentry, console.error/warn patterns, ErrorBoundary alongside backend logging frameworks
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

**[AgentReady](https://github.com/ambient-code/agentready)** and this tool solve different problems:

| | This tool | AgentReady |
|---|---|---|
| **Focus** | Can AI agents fix bugs in this repo? | Is this repo AI-coding-friendly? |
| **Checks** | 20 — test infra, CI, bug templates, build setup, type safety | 25 — type annotations, lock files, naming conventions |
| **Scoring emphasis** | Testing = 46% of score | Evenly distributed |
| **Key question** | Can an agent run tests to verify a fix? | Is the code well-structured for AI to read? |
| **Use when** | Planning an AI bug bash | Assessing overall AI-friendliness |

They're complementary — a repo can score well on AgentReady (clean code, good types) but poorly here (no tests, no CI). Use both if you want the full picture.

## Examples

See the [`docs/`](docs/) folder for sample reports generated from an OpenDataHub ecosystem scan (135 repos): HTML, markdown, JSON, CSV, and DOCX.

For actionable steps to improve your repo's score, see the [Team Action Guide](docs/TEAM_ACTION_GUIDE.md).

The HTML report is also available via [GitHub Pages](https://ugiordan.github.io/ai-bug-automation-readiness/report.html).

## Requirements

- Python 3.10+
- No external dependencies for core formats (stdlib only)
- Optional: `python-docx` for DOCX format (`pip install python-docx`)
