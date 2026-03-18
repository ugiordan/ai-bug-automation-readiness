# AI Bug Automation Readiness — Team Action Guide

## What This Is

This tool scores repositories on how ready they are for AI agents to autonomously fix bugs. It checks 20 things across 4 phases: **Understand → Navigate → Verify → Submit**. Each repo gets a score from 0-100.

| Level | Score | What it means |
|---|---|---|
| Ready | 80+ | AI agents can work effectively on this repo |
| Partially Ready | 60-79 | Workable but some fixes will fail due to gaps |
| Needs Work | 40-59 | Fix the gaps below before running AI bug fixing |
| Not Ready | <40 | Fundamental gaps — start with the basics |

Non-code repos (docs, config, governance) with fewer than 3 source files are automatically excluded from scoring.

---

## The 4 Phases and What Teams Need To Do

### Phase 1: Understand (24% of score)

*"Can the AI agent understand what the bug is and how the codebase works?"*

#### 1. AI Context File (8%)

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

#### 2. Bug Report Template (8%)

**What:** A structured GitHub issue template that ensures bug reports contain the information an AI agent needs.

**What to do:** Create `.github/ISSUE_TEMPLATE/bug_report.yml` with these required fields:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (version, platform)
- Error logs / stack trace

---

#### 3. Structured Logging (3%)

**What:** Using a logging library that produces parseable output, not bare `fmt.Println`.

**What to do:**
- **Go:** Use `logr`, `zap`, `zerolog`, or `klog`
- **Python:** Use `structlog` or `loguru`
- **Node.js:** Use `winston` or `pino`
- **Frontend:** Sentry, error boundaries, or structured console wrappers count
- Wrap errors with context (`fmt.Errorf("failed to reconcile: %w", err)`)

---

#### 4. Architecture Documentation (3%)

**What:** Documentation that helps AI agents understand how the codebase is structured.

**What to do:**
- Add `ARCHITECTURE.md` describing high-level design
- Consider ADR (Architecture Decision Records) in `docs/adr/`
- Add `README.md` files in key subdirectories explaining their purpose

---

#### 5. Test Fixtures / Sample Data (2%)

**What:** Sample inputs and expected outputs that help AI agents understand data formats.

**What to do:**
- Add `testdata/`, `fixtures/`, or `examples/` directories
- Include representative sample data for key features

---

### Phase 2: Navigate (17% of score)

*"Can the AI agent find the relevant code quickly?"*

#### 6. Code Navigability (5%)

**What:** Keeping files at a reasonable size so AI agents can understand them.

**What to do:**
- Keep source files under 500 lines
- Break large files into focused modules
- Go/Java repos get more lenient thresholds (700 lines)

---

#### 7. Generated Code Ratio (2%)

**What:** Making sure AI agents don't waste time reading auto-generated code.

**What to do:**
- Add `// Code generated` or `// DO NOT EDIT` headers to generated files
- Document in your `AGENTS.md` which directories contain generated code

---

#### 8. Build / Dependency Setup (5%)

**What:** Reproducible builds so AI agents can build and test locally.

**What to do:**
- Commit lockfiles (`go.sum`, `package-lock.json`, `poetry.lock`)
- Add `build` and `install` targets to Makefile
- Consider a Dockerfile or devcontainer for reproducible environments

---

#### 9. Type Safety / Static Analysis (3%)

**What:** Type information helps AI agents understand function contracts.

**What to do:**
- Go, Java, Rust, C++ get automatic credit (statically typed)
- **TypeScript:** Enable `"strict": true` in `tsconfig.json`
- **Python:** Configure `mypy` or `pyright`

---

#### 10. Dependency Complexity (2%)

**What:** Fewer dependencies means less surface area for AI agents to understand.

**What to do:** Keep direct dependency count reasonable relative to codebase size.

---

### Phase 3: Verify (46% of score)

*"Can the AI agent run tests to prove the fix actually works?"*

**This is nearly half the total score** because without tests, an AI agent has no way to confirm its fix is correct. Repos with poor Verify scores get an additional penalty (the "verify gate").

#### 11. Test-to-Source Ratio (15%)

**What:** Having enough test files relative to source files.

**What to do:**
- Aim for at least 1 test file per 2 source files (ratio >= 0.4 scores 70+)
- Focus on unit tests for business logic and controllers
- Frontend-heavy repos (TS/React) use relaxed thresholds since component files inflate source counts

---

#### 12. One-Command Test Execution (11%)

**What:** Tests must be runnable with a single command.

**What to do:** Add Makefile targets:
```makefile
test:          ## Run all tests
	go test ./...

unittest:      ## Run unit tests only (no cluster needed)
	go test ./... -tags=unit

e2e-test:      ## Run e2e tests
	go test ./... -tags=e2e
```

Also recognized: `npm test`, `pytest`, `tox`, `./gradlew test`, `mvn test`.

---

#### 13. CI Runs Tests on PRs (10%)

**What:** CI must run tests when a pull request is opened.

**What to do:** Ensure at least one GitHub Actions workflow:
- Triggers on `pull_request` (not `pull_request_target`)
- Contains a step that runs tests (e.g., `make test`, `go test`, `pytest`)

Both must be in the **same workflow file** to score 100.

---

#### 14. Coverage Configuration (3%)

**What:** Code coverage reporting helps identify untested code paths.

**What to do:**
- **Go:** Add `-coverprofile=cover.out` to your test commands
- **Python:** Add `pytest-cov` and configure in `pyproject.toml`
- Consider adding Codecov or Coveralls integration

---

#### 15. Test Isolation (4%)

**What:** Separating unit tests (fast, no dependencies) from integration/e2e tests.

**What to do:**
- Use Go build tags: `//go:build !e2e` for unit tests
- Use directory separation: `tests/unit/` vs `tests/e2e/`
- Add separate Makefile targets for unit and integration tests

---

#### 16. Pre-commit / Local Hooks (3%)

**What:** Fast local validation before pushing code.

**What to do:**
- Add `.pre-commit-config.yaml` with linting and formatting hooks
- Or use Husky (Node.js) or Lefthook for git hooks

---

### Phase 4: Submit (13% of score)

*"Can the AI agent submit a proper pull request?"*

#### 17. Linting in CI (5%)

**What:** Automated code style enforcement catches formatting issues in AI-generated code.

**What to do:** Add a linting step to CI:
- **Go:** `golangci-lint run`
- **Python:** `ruff check .` or `flake8`
- **JS/TS:** `eslint .`

---

#### 18. Contributing Guide (5%)

**What:** A document that explains how to contribute.

**What to do:** Create `CONTRIBUTING.md` covering:
- How to set up the dev environment
- How to build and run tests
- How to submit a PR
- Code style expectations

---

#### 19. Code Ownership (1%)

**What:** A CODEOWNERS or OWNERS file for automatic reviewer assignment on PRs.

**What to do:** Create `.github/CODEOWNERS` or use OpenShift-style `OWNERS`/`OWNERS_ALIASES` files (both are recognized).

---

#### 20. PR Template (2%)

**What:** A pull request template that reminds contributors (including AI) to include test evidence.

**What to do:** Create `.github/PULL_REQUEST_TEMPLATE.md` with a testing checklist.

---

## Quick Start: Biggest Impact Actions

If your repo scores low, focus on these first (ordered by score impact):

1. **Add unit tests** — 15% of score, and triggers the verify gate penalty if too low
2. **Add `make test` target** — 11%, easy win
3. **Ensure CI runs tests on PRs** — 10%, check your workflow triggers
4. **Add a bug report template** — 8%, copy a YAML template
5. **Create AGENTS.md** — 8%, takes 15 minutes
6. **Add CONTRIBUTING.md** — 5%, document what you already know
7. **Add lockfiles and build targets** — 5%, commit your lockfiles

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
