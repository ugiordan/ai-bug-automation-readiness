# AI Bug Automation Readiness — Team Action Guide

## What This Is

This tool scores repositories on how ready they are for AI agents to autonomously fix bugs. It checks 14 things across 4 phases: **Understand → Navigate → Verify → Submit**. Each repo gets a score from 0-100.

| Level | Score | What it means |
|---|---|---|
| Ready | 80+ | AI agents can work effectively on this repo |
| Partially Ready | 60-79 | Workable but some fixes will fail due to gaps |
| Needs Work | 40-59 | Fix the gaps below before running AI bug fixing |
| Not Ready | <40 | Fundamental gaps — start with the basics |

---

## The 4 Phases and What Teams Need To Do

### Phase 1: Understand (22% of score)

*"Can the AI agent understand what the bug is and how the codebase works?"*

#### 1. AI Context File (5%)

**What:** A file at the repo root that tells AI agents how the project is structured.

**What to do:** Create an `AGENTS.md` (or `CLAUDE.md` for Claude users) containing:
- High-level architecture (what components exist, how they connect)
- How to build the project
- How to run tests
- How to debug common issues
- Key directories and what they contain

**Example:**
```markdown
# Architecture
This is a Kubernetes operator that manages DataSciencePipelines CRDs.

# Build
make build

# Test
make unittest        # unit tests (no cluster needed)
make e2e-test        # e2e tests (needs kind cluster)

# Key Directories
- /controllers/     - reconciliation logic
- /api/v1alpha1/    - CRD type definitions
- /config/          - Kustomize manifests
```

---

#### 2. Bug Report Template (12%)

**What:** A structured GitHub issue template that ensures bug reports contain the information an AI agent needs to reproduce and fix the bug.

**What to do:** Create `.github/ISSUE_TEMPLATE/bug_report.yml` with these required fields:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (version, platform)
- Error logs / stack trace

**Example:** (`.github/ISSUE_TEMPLATE/bug_report.yml`)
```yaml
name: Bug Report
description: Report a bug
labels: [bug]
body:
  - type: textarea
    attributes:
      label: Steps to reproduce
    validations:
      required: true
  - type: textarea
    attributes:
      label: Expected behavior
    validations:
      required: true
  - type: textarea
    attributes:
      label: Actual behavior
    validations:
      required: true
  - type: textarea
    attributes:
      label: Environment
      description: Version, OS, cluster version, etc.
    validations:
      required: true
  - type: textarea
    attributes:
      label: Logs / Error output
```

---

#### 3. Structured Logging (5%)

**What:** Using a logging library that produces parseable output, not bare `fmt.Println`.

**What to do:**
- **Go:** Use `logr`, `zap`, `zerolog`, or `klog`
- **Python:** Use `structlog` or `loguru`
- **Node.js:** Use `winston` or `pino`
- Wrap errors with context (`fmt.Errorf("failed to reconcile: %w", err)`)

---

### Phase 2: Navigate (13% of score)

*"Can the AI agent find the relevant code quickly?"*

#### 4. Code Navigability (8%)

**What:** Keeping files at a reasonable size so AI agents can understand them within their context window.

**What to do:**
- Keep source files under 500 lines
- Break large files into focused modules (one responsibility per file)
- Go/Java repos get more lenient thresholds (700 lines) since those languages tend toward longer files

---

#### 5. Generated Code Ratio (5%)

**What:** Making sure AI agents don't waste time reading auto-generated code.

**What to do:**
- Add `// Code generated` or `// DO NOT EDIT` headers to generated files
- Document in your `AGENTS.md` which directories contain generated code
- Common examples: `zz_generated.deepcopy.go`, `*.pb.go`, `openapi_generated.go`

---

### Phase 3: Verify (49% of score)

*"Can the AI agent run tests to prove the fix actually works?"*

**This is nearly half the total score** because without tests, an AI agent has no way to confirm its fix is correct. Repos with poor Verify scores get an additional penalty (the "verify gate").

#### 6. Test-to-Source Ratio (17%)

**What:** Having enough test files relative to source files.

**What to do:**
- Aim for at least 1 test file per 2 source files (ratio ≥ 0.4 scores 70+)
- Focus on unit tests for business logic and controllers
- Don't count test helpers/utilities — the tool already excludes those

| Ratio | Score |
|---|---|
| ≥ 1.0 | 100 |
| ≥ 0.6 | 85 |
| ≥ 0.4 | 70 |
| ≥ 0.2 | 50 |
| < 0.2 | 25 or less |

---

#### 7. One-Command Test Execution (12%)

**What:** Tests must be runnable with a single command. AI agents cannot follow multi-step setup instructions.

**What to do:** Add Makefile targets:
```makefile
test:          ## Run all tests
	go test ./...

unittest:      ## Run unit tests only (no cluster needed)
	go test ./... -tags=unit

e2e-test:      ## Run e2e tests
	go test ./... -tags=e2e
```

Having multiple test targets (unit, e2e, integration) scores higher.

Also recognized: `npm test`, `pytest`, `tox`, `./gradlew test`, `mvn test`.

---

#### 8. CI Runs Tests on PRs (10%)

**What:** CI must run tests when a pull request is opened, so the AI agent's fix gets validated automatically.

**What to do:** Ensure at least one GitHub Actions workflow:
- Triggers on `pull_request`
- Contains a step that runs tests (e.g., `make test`, `go test`, `pytest`)

Both must be in the **same workflow file** to score 100.

---

#### 9. Coverage Configuration (5%)

**What:** Code coverage reporting helps identify untested code paths.

**What to do:**
- **Go:** Add `-coverprofile=cover.out` to your test commands
- **Python:** Add `pytest-cov` and configure in `pyproject.toml`
- Consider adding Codecov or Coveralls integration

---

#### 10. Test Isolation (5%)

**What:** Separating unit tests (fast, no dependencies) from integration/e2e tests (need cluster, database, etc.).

**What to do:**
- Use Go build tags: `//go:build !e2e` for unit tests
- Use directory separation: `tests/unit/` vs `tests/e2e/`
- Add separate Makefile targets for unit and integration tests
- Use mocks/fakes for external dependencies in unit tests

---

### Phase 4: Submit (16% of score)

*"Can the AI agent submit a proper pull request?"*

#### 11. Linting in CI (5%)

**What:** Automated code style enforcement catches formatting issues in AI-generated code.

**What to do:** Add a linting step to CI:
- **Go:** `golangci-lint run`
- **Python:** `ruff check .` or `flake8`
- **JS/TS:** `eslint .`

---

#### 12. Contributing Guide (5%)

**What:** A document that explains how to contribute — AI agents use this to understand conventions.

**What to do:** Create `CONTRIBUTING.md` covering:
- How to set up the dev environment
- How to build
- How to run tests
- How to submit a PR
- Code style expectations

---

#### 13. Code Ownership (3%)

**What:** A CODEOWNERS file for automatic reviewer assignment on PRs.

**What to do:** Create `.github/CODEOWNERS`:
```
# Default owners
*                    @your-team

# Specific paths
/controllers/        @controllers-team
/api/                @api-team
```

---

#### 14. PR Template (3%)

**What:** A pull request template that reminds contributors (including AI) to include test evidence.

**What to do:** Create `.github/PULL_REQUEST_TEMPLATE.md`:
```markdown
## What this PR does

## How to test
- [ ] Unit tests pass (`make unittest`)
- [ ] No linting errors (`make lint`)
- [ ] Manually verified (if applicable)

## Related issue
Fixes #
```

---

## Quick Start: Biggest Impact Actions

If your repo scores low, focus on these first (ordered by score impact):

1. **Add unit tests** — 17% of score, and triggers the verify gate penalty if too low
2. **Add `make test` target** — 12%, easy win
3. **Add a bug report template** — 12%, copy the YAML example above
4. **Ensure CI runs tests on PRs** — 10%, check your workflow triggers
5. **Create AGENTS.md** — 5%, takes 15 minutes
6. **Add CONTRIBUTING.md** — 5%, document what you already know

## Running the Tool

```bash
# Check a single repo
python assess.py /path/to/your-repo

# Scan all repos in a directory
python assess.py --batch /path/to/repos --format html -o report.html

# CI gating: fail if score drops below 60
python assess.py /path/to/repo --fail-under 60
```

Full report for all OpenDataHub repos: https://ugiordan.github.io/ai-bug-automation-readiness/report.html
