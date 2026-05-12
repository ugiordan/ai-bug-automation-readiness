# AI Bug Automation Readiness

Assess whether repositories are ready for AI agents to autonomously find, fix, and verify bugs.

Unlike general "AI readiness" tools that check if documentation exists, this tool evaluates what actually matters for autonomous bug fixing.
The assessment focuses on four capabilities: can the agent understand the bug, navigate the code, run tests to verify a fix, and submit it properly?

## Getting Started

Install by cloning the repository. Core formats require zero dependencies (stdlib only).

```bash
git clone https://github.com/ugiordan/ai-bug-automation-readiness.git
cd ai-bug-automation-readiness
python assess.py /path/to/repo  # Requires Python 3.10+

pip install python-docx  # Optional: for DOCX output format
```

Common usage patterns:

```bash
python assess.py /path/to/repo                            # Single repo with text output
python assess.py /path/to/repo --format json              # JSON output for tooling
python assess.py --batch /path/to/repos --format html -o report.html --org your-org
python assess.py --batch /path/to/repos --fail-under 60   # CI gating
python assess.py --batch /path/to/repos --exclude archived-repo legacy-tool
python assess.py --list-checks                            # Show all checks and weights
```

Available CLI flags: `--batch PATH`, `--format FORMAT` (text/json/html/markdown/csv/docx), `--output / -o PATH`, `--org NAME`, `--title TEXT`, `--fail-under N`, `--exclude REPO...`, `--quiet / -q`, `--list-checks`, `--profile NAME`, `--exclude-checks CHECK...`, `--list-profiles`, `--version`.

Exit codes: 0 (success), 1 (--fail-under threshold not met), 2 (error: invalid args, no repos found, missing dependency).

Output formats: text (terminal), json (CI tooling), markdown (wikis), csv (spreadsheets), html (charts and heatmaps), docx (Google Docs/Word, requires python-docx).

Multi-org scanning: define `scan-config.json` with org names and modes, then run `python scripts/clone-repos.py scan-config.json /tmp/repos` followed by `python assess.py --batch /tmp/repos --format html -o report.html`. HTML reports show per-org tabs when multiple orgs are detected.

## Assessment Model

The tool evaluates 20 checks across 4 phases of an AI bug-fixing workflow:

- **Understand (24%)**: AI Context Files (8%), Bug Report Template Quality (8%), Structured Logging (3%), Architecture Documentation (3%), Test Fixtures (2%)
- **Navigate (17%)**: Code Navigability (5%), Generated Code Ratio (2%), Build/Dependency Setup (5%), Type Safety/Static Analysis (3%), Dependency Complexity (2%)
- **Verify (46%)**: Test-to-Source Ratio (15%), One-Command Test Execution (11%), CI Runs Tests on PRs (10%), Coverage Configuration (3%), Test Isolation (4%), Pre-commit/Local Hooks (3%)
- **Submit (13%)**: Linting in CI (5%), Contributing Guide (5%), Code Ownership (1%), PR Template (2%)

Scoring: overall score = weighted average of all checks (0-100 each). Readiness levels: Ready (80+), Partially Ready (60-79), Needs Work (40-59), Not Ready (<40). Repos with fewer than 3 source files are classified as "Not Applicable" and excluded from scoring.

Verify phase gate: if the average Verify score is below 50, the overall score receives a smooth multiplier penalty scaling linearly from x0.4 (verify avg = 0) to x1.0 (verify avg = 50). A repo without test infrastructure cannot support autonomous bug fixing, regardless of documentation quality.

Profiles allow excluding structurally inapplicable checks for specific repo types (e.g., E2E test repos don't need internal coverage). Configuration lives in `assess/profiles.json`. Maximum 5 checks excluded per repo, cannot exclude all checks in any category, weights cannot be overridden.

## Design Decisions

Key implementation choices:

- Non-code repos (<3 source files) excluded from scoring
- Generated files excluded from navigability and test ratio analysis
- Single filesystem traversal per repo for performance (3-5x faster)
- Deterministic results via per-repo seeded RNG (MD5 of repo name)
- Typed languages (Go, Java, Rust, C++) score high automatically on type safety
- Frontend-aware test ratio thresholds for TS/JS-heavy repos (relaxed: 1 test per 8 source files acceptable)
- CI checks exclude `pull_request_target` (only `pull_request` triggers count)
- Build tool validation requires actual test files, not just config presence
- Test helper exclusion prevents count inflation (conftest, helpers, fixtures, mocks)
- HTML output is XSS-safe with escaped values and SRI integrity
- OWNERS/OWNERS_ALIASES treated as equivalent to CODEOWNERS

This tool and [AgentReady](https://github.com/ambient-code/agentready) are complementary: this focuses on bug-fixing readiness (test infra weighted at 46%), while AgentReady assesses general AI-coding-friendliness with evenly distributed scoring.

The [OpenDataHub readiness report](https://ugiordan.github.io/ai-bug-automation-readiness/report.html) is regenerated automatically every Monday via GitHub Actions. For actionable improvement steps, see the [Team Action Guide](docs/TEAM_ACTION_GUIDE.md).
