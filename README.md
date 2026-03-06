# AI Bug Automation Readiness

Assess whether repositories are ready for AI agents to autonomously find, fix, and verify bugs.

Unlike general "AI readiness" tools that check if documentation exists, this tool evaluates what actually matters for autonomous bug fixing: can the agent understand the bug, navigate the code, run tests to verify a fix, and submit it properly?

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

# With AgentReady comparison
python assess.py --batch /path/to/repos --format html --agentready-results /path/to/results

# CI gating: exit 1 if any repo scores below 60
python assess.py --batch /path/to/repos --fail-under 60

# Pipe JSON without progress noise (progress goes to stderr)
python assess.py /path/to/repo --format json | jq .overall_score
```

## What It Checks

The tool evaluates 14 checks across 4 phases of an AI bug-fixing workflow:

### Understand (22%)
Can the agent understand the bug from the report and codebase context?

| Check | Weight | What it measures |
|---|---|---|
| AI Context Files | 5% | CLAUDE.md, AGENTS.md with quality keywords (test, debug, build) |
| Bug Report Template Quality | 12% | Reproduction steps, expected/actual behavior, environment, logs. Validates YAML frontmatter to avoid false positives. Supports .md, .yml, .yaml templates. |
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
| Test-to-Source Ratio | 17% | Ratio of test files to source files |
| One-Command Test Execution | 12% | Makefile test targets (root and subdirectory), npm scripts, pytest config |
| CI Runs Tests on PRs | 10% | CI workflows triggered by pull_request with test steps in the same workflow |
| Coverage Configuration | 5% | Coverage flags, codecov integration |
| Test Isolation | 5% | Unit vs integration test separation using mock/fake patterns, build tags, and directory structure |

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
- **Word-boundary matching** prevents false positives (e.g., "log" no longer matches "blog" or "catalog")
- **Only direct dependencies** are scanned for logging libraries (go.mod, not go.sum)
- **CI checks correlate PR trigger and test step** within the same workflow file to avoid false positives
- **Bug template frontmatter validation** ensures files named `bug_report.md` are actually bug templates, not repurposed files
- **Subdirectory Makefile scanning** detects test targets in monorepo subdirectories (e.g., `ray-operator/Makefile`)
- **Test isolation uses mock/fake patterns** instead of generic framework markers (testing.T, testify) that appear in all Go tests
- **Deterministic results** via seeded RNG per-repo ensures reproducible scores across runs
- **Language-aware thresholds** for file size (Go/Java files are typically longer than Python/JS)
- **Per-check recommendations** tell you exactly what to fix, not just what's wrong
- **HTML output is XSS-safe** with all user-derived values escaped

## Output Formats

- **text**: Terminal-friendly summary with per-check details and recommendations (single repo)
- **json**: Machine-readable for trend tracking and CI integration
- **markdown**: Portable report with tables, suitable for wikis, GitHub issues, or Google Docs import
- **csv**: Spreadsheet-friendly with per-repo scores for all checks (importable into Google Sheets, Excel)
- **html**: Visual report with executive summary, bug bash shortlist, quick wins, score distribution histogram, gaps bar chart, bottleneck phases, heatmap, and per-repo details

## Examples

See the [`docs/`](docs/) folder for sample reports generated from an OpenDataHub ecosystem scan (18 repos): HTML, markdown, JSON, and CSV.

The HTML report is also available via [GitHub Pages](https://ugiordan.github.io/ai-bug-automation-readiness/report.html).

## Requirements

- Python 3.10+
- No external dependencies (stdlib only)
