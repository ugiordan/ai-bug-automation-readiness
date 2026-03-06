# AI Bug Automation Readiness Report

*14 repositories assessed -- 2026-03-06 18:05*

> 8 of 14 repositories are partially ready or above for AI-assisted bug fixing. The ecosystem averages 52/100. The biggest gap is "AI Context Files" (avg 7/100).

## How Scoring Works

**Overall score** = weighted average of 14 checks, each scored 0-100.

**Phases**: Understand (22%), Navigate (13%), Verify (49%), Submit (16%).

**Verify phase gate:** If the average Verify score is below 15, the overall score is multiplied by 0.4. If below 30, multiplied by 0.7.

| Level | Score | Meaning |
|---|---|---|
| Ready | 80+ | Strong test infrastructure, good context, CI validates fixes |
| Partially Ready | 60-79 | Workable but has gaps that may cause AI agent failures |
| Needs Work | 40-59 | Missing key capabilities; fix gaps before AI bug bash |
| Not Ready | <40 | Fundamental gaps in test infrastructure or code structure |

## Summary

| Metric | Value |
|---|---|
| Average Score | 52/100 |
| Ready (80+) | 1 |
| Partially Ready (60-79) | 7 |
| Needs Work (40-59) | 2 |
| Not Ready (<40) | 4 |

## Phase Scores (Ecosystem Average)

| Phase | Weight | Average |
|---|---|---|
| Understand | 22% | 38/100 |
| Navigate | 13% | 81/100 |
| Verify | 49% | 55/100 |
| Submit | 16% | 45/100 |

## Bug Bash Shortlist

### Ready (80+) -- 1 repos

- data-science-pipelines-operator (80)

### Partially Ready (60-79) -- 7 repos

- kube-auth-proxy (78) -- top gap: CI Runs Tests on PRs
- odh-dashboard (75) -- top gap: Test-to-Source Ratio
- kuberay (74) -- top gap: AI Context Files
- agentready-audit (72) -- top gap: Test-to-Source Ratio
- opendatahub-operator (72) -- top gap: Bug Report Template Quality
- odh-model-controller (64) -- top gap: Bug Report Template Quality
- odh-platform-chaos (60) -- top gap: Bug Report Template Quality

### Needs Work (40-59) -- 2 repos

- trustyai-service-operator (55) -- top gap: Bug Report Template Quality
- operator-security-runtime (41) -- top gap: Bug Report Template Quality

### Not Ready (<40) -- 4 repos

- ai-code-analyst (39)
- opendatahub-community (8)
- ai-bug-automation-readiness (4)
- architecture-decision-records (3)

## Repository Scores

| Repository | Score | Level | Languages |
|---|---|---|---|
| data-science-pipelines-operator | 80/100 | Ready | Go, Python |
| kube-auth-proxy | 78/100 | Partially Ready | Go, JavaScript |
| odh-dashboard | 75/100 | Partially Ready | TypeScript, JavaScript, Go |
| kuberay | 74/100 | Partially Ready | Go, Python, TypeScript |
| agentready-audit | 72/100 | Partially Ready | Python |
| opendatahub-operator | 72/100 | Partially Ready | Go, Python, JavaScript |
| odh-model-controller | 64/100 | Partially Ready | Go |
| odh-platform-chaos | 60/100 | Partially Ready | Go |
| trustyai-service-operator | 55/100 | Needs Work | Go |
| operator-security-runtime (verify gate) | 41/100 | Needs Work | Go |
| ai-code-analyst | 39/100 | Not Ready | Python, TypeScript |
| opendatahub-community (verify gate) | 8/100 | Not Ready | Unknown |
| ai-bug-automation-readiness (verify gate) | 4/100 | Not Ready | Python |
| architecture-decision-records (verify gate) | 3/100 | Not Ready | Unknown |

## Quick Wins (Highest Impact Actions)

| Action | Repos Below 40 | Weight | How to Fix |
|---|---|---|---|
| Bug Report Template Quality | 7 repos | 12% | Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs. |
| AI Context Files | 13 repos | 5% | Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug. |
| Coverage Configuration | 7 repos | 5% | Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration. |
| Contributing / Dev Guide | 4 repos | 5% | Add CONTRIBUTING.md with build, test, and debug instructions. |
| Code Ownership (CODEOWNERS) | 7 repos | 3% | Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment. |
| PR Template | 7 repos | 3% | Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist. |

## All Checks Ranked by Average Score

| Check | Avg Score | Weight |
|---|---|---|
| AI Context Files | 7/100 | 5% |
| Coverage Configuration | 34/100 | 5% |
| Code Ownership (CODEOWNERS) | 36/100 | 3% |
| Contributing / Dev Guide | 43/100 | 5% |
| Bug Report Template Quality | 44/100 | 12% |
| PR Template | 46/100 | 3% |
| Test-to-Source Ratio | 52/100 | 17% |
| Linting / Formatting in CI | 57/100 | 5% |
| One-Command Test Execution | 62/100 | 12% |
| Test Isolation (unit vs e2e) | 63/100 | 5% |
| Structured Logging / Errors | 64/100 | 5% |
| Code Navigability | 64/100 | 8% |
| CI Runs Tests on PRs | 64/100 | 10% |
| Generated Code Ratio | 97/100 | 5% |

## Per-Repository Details

### data-science-pipelines-operator -- 80/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (20/50 sampled files); Error wrapping patterns (10 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 197 lines (53 source files, generated excluded); Files >500 lines: 3 (6%); Largest: dspipeline_params.go (907L), dspipeline_controller.go (819L), storage_test.go (562L) |
| Generated Code Ratio | Navigate | 5% | 100 | 1/54 files are generated (2%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 26 test files / 27 source files (ratio: 0.96) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, unittest, functest; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): functests.yml, nightly_tests.yml, unittests.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: precommit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 85 | ~60% unit tests, ~40% infra-dependent (12/20 sampled); Makefile separates unit and integration test targets |

### kube-auth-proxy -- 78/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug-report.yml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (logr) found in go.mod; Some logging (7/50 sampled files); Error wrapping patterns (18 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 183 lines (255 source files, generated excluded); Files >500 lines: 17 (7%); Largest: oauthproxy_test.go (3583L), oauthproxy.go (1570L), server_test.go (1321L) |
| Generated Code Ratio | Navigate | 5% | 100 | 6/261 files are generated (2%); Examples: mock_openshift_oauth.go, mock_oidc_test.go, mock_openshift_oauth_test.go, mock_oidc.go, mock_lock.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 9 rules |
| Test-to-Source Ratio | Verify | 17% | 100 | 128 test files / 127 source files (ratio: 1.01) |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, kube-rbac-proxy/test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~73% unit tests, ~27% infra-dependent (22/30 sampled) |

### odh-dashboard -- 75/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (2 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 91 lines (5003 source files, generated excluded); Files >500 lines: 98 (2%); Largest: mockPipelineSpec.ts (5220L), workbench.cy.ts (1951L), modelTraining.cy.ts (1806L) |
| Generated Code Ratio | Navigate | 5% | 100 | 17/5021 files are generated (0%); Examples: model_catalog_settings_mock.go, static_data_mock.go, model_registry_client_mock.go, model_catalog_client_mock.go, http_mock.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 852 test files / 4152 source files (ratio: 0.21) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: node_modules/fileset/test, node_modules/obj-case/test, node_modules/stack-trace/test, node_modules/throttleit/test, node_modules/batch/test, node_modules/delayed-stream/test, node_modules/new-date/test, node_modules/delegates/test, node_modules/json-stringify-safe/test; Multiple test types available; npm test script defined |
| Coverage Configuration | Verify | 5% | 60 | Codecov configured; Coverage in CI workflow: test.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, gen-ai-frontend-build.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: gen-ai-bff-build.yml, modular-arch-quality-gates.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (25/25 sampled) |

### kuberay -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 95 | Found: .github/ISSUE_TEMPLATE/bug-report.yml; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Go structured logging (zerolog) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (10/50 sampled files); Error wrapping patterns (9 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 227 lines (346 source files, generated excluded); Files >500 lines: 38 (11%); Largest: raycluster_controller_unit_test.go (3811L), raycluster_controller.go (2053L), pod_test.go (1954L) |
| Generated Code Ratio | Navigate | 5% | 60 | 78/425 files are generated (18%); Examples: config_grpc.pb.go, job_submission.pb.gw.go, serve.pb.gw.go, config.pb.gw.go, cluster.pb.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 85 | 154 test files / 193 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: ray-operator/test, ray-operator/test, ray-operator/test, apiserver/test, apiserver/e2e-test, apiserversdk/test, apiserversdk/test, apiserversdk/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): odh-release.yml, image-release.yaml, e2e-tests.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: helm.yaml, test-job.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 50 | ~41% unit tests, ~59% infra-dependent (11/27 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### agentready-audit -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (4/7 quality keywords); claude.md found (4/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 75 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields |
| Structured Logging / Errors | Understand | 5% | 90 | Python structured logging found in requirements.txt; Error wrapping patterns (1 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 256 lines (7 source files, generated excluded); Files >500 lines: 1 (14%); Largest: bug_automation_readiness.py (979L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/12 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 3 test files / 9 source files (ratio: 0.33) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test; pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: ci.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |

### opendatahub-operator -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 45 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has environment/version fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (15/50 sampled files); Error wrapping patterns (16 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 203 lines (457 source files, generated excluded); Files >500 lines: 44 (10%); Largest: mutating_test.go (2480L), monitoring_test.go (2171L), test_context_test.go (2083L) |
| Generated Code Ratio | Navigate | 5% | 100 | 12/469 files are generated (3%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 154 test files / 303 source files (ratio: 0.51) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, unit-test, e2e-test, e2e-test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Codecov configured; Go coverage flags in Makefile; Coverage in CI workflow: security-full-scan.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test-unit.yaml, test-unit-cli.yaml, test-prometheus-unit.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: security-full-scan.yml, test-linter.yaml |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 50 | ~46% unit tests, ~54% infra-dependent (12/26 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-model-controller -- 64/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (20/50 sampled files); Error wrapping patterns (13 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 218 lines (138 source files, generated excluded); Files >500 lines: 11 (8%); Largest: llm_inferenceservice_controller_test.go (1258L), rbac-analyzer.py (1148L), generate-security-report.py (1092L) |
| Generated Code Ratio | Navigate | 5% | 100 | 1/139 files are generated (1%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 44 test files / 94 source files (ratio: 0.47) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile; Coverage in CI workflow: security-full-scan.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, test-e2e.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml, security-full-scan.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started, Develop, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~70% unit tests, ~30% infra-dependent (21/30 sampled) |

### odh-platform-chaos -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (20/50 sampled files); Error wrapping patterns (14 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 153 lines (98 source files, generated excluded); Files >500 lines: 3 (3%); Largest: clean_test.go (1941L), clean.go (825L), lifecycle_test.go (616L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/98 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 44 test files / 54 source files (ratio: 0.81) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yaml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |

### trustyai-service-operator -- 55/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (17/50 sampled files); Error wrapping patterns (8 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 229 lines (128 source files, generated excluded); Files >500 lines: 13 (10%); Largest: lmevaljob_controller_test.go (4373L), lmevaljob_controller_validation_test.go (1798L), lmevaljob_controller.go (1679L) |
| Generated Code Ratio | Navigate | 5% | 100 | 6/134 files are generated (4%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 31 test files / 97 source files (ratio: 0.32) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, tests/test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): controller-tests.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint-yaml.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~67% unit tests, ~33% infra-dependent (20/30 sampled) |

### operator-security-runtime -- 41/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (13/27 sampled files); Error wrapping patterns (11 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 320 lines (27 source files, generated excluded); Files >500 lines: 4 (15%); Largest: rbac_scoper_test.go (2803L), cluster_rbac_scoper_test.go (912L), impersonation_guard_test.go (570L) |
| Generated Code Ratio | Navigate | 5% | 100 | 1/28 files are generated (4%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 70 | 10 test files / 17 source files (ratio: 0.59) |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, examples/operator/test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~78% unit tests, ~22% infra-dependent (7/9 sampled) |

### ai-code-analyst -- 39/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (19 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 337 lines (1521 source files, generated excluded); Files >500 lines: 287 (19%); Largest: uts46data.py (8841L), uts46data.py (8681L), _lasso_builtins.py (5326L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 8/1561 files are generated (1%); Examples: _mapping.py, _mapping.py, _mapping.py, _mapping.py, _mapping.py |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 10 | 29 test files / 1524 source files (ratio: 0.02) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (22/22 sampled) |

### opendatahub-community -- 8/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### ai-bug-automation-readiness -- 4/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 164 lines (11 source files, generated excluded); Files >500 lines: 2 (18%); Largest: checks.py (698L), html.py (514L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/11 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 11 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### architecture-decision-records -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 11 rules |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

---
*AI Bug Automation Readiness Report -- Generated 2026-03-06 18:05*

