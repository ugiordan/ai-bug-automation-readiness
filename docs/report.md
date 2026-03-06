# AI Bug Automation Readiness Report

*18 repositories assessed -- 2026-03-06 17:59*

> 16 of 18 repositories are partially ready or above for AI-assisted bug fixing. The ecosystem averages 67/100. The biggest gap is "AI Context Files" (avg 22/100).

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
| Average Score | 67/100 |
| Ready (80+) | 2 |
| Partially Ready (60-79) | 14 |
| Needs Work (40-59) | 1 |
| Not Ready (<40) | 1 |

## Phase Scores (Ecosystem Average)

| Phase | Weight | Average |
|---|---|---|
| Understand | 22% | 51/100 |
| Navigate | 13% | 79/100 |
| Verify | 49% | 73/100 |
| Submit | 16% | 65/100 |

## Bug Bash Shortlist

### Ready (80+) -- 2 repos

- [data-science-pipelines-operator](https://github.com/opendatahub-io/data-science-pipelines-operator) (80)
- [odh-dashboard](https://github.com/opendatahub-io/odh-dashboard) (80)

### Partially Ready (60-79) -- 14 repos

- [feast](https://github.com/opendatahub-io/feast) (79) -- top gap: Test-to-Source Ratio
- [kserve](https://github.com/opendatahub-io/kserve) (77) -- top gap: AI Context Files
- [spark-operator](https://github.com/opendatahub-io/spark-operator) (76) -- top gap: Test-to-Source Ratio
- [kuberay](https://github.com/opendatahub-io/kuberay) (74) -- top gap: AI Context Files
- [opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) (72) -- top gap: Bug Report Template Quality
- [notebooks](https://github.com/opendatahub-io/notebooks) (70) -- top gap: Test-to-Source Ratio
- [mlflow-operator](https://github.com/opendatahub-io/mlflow-operator) (69) -- top gap: Bug Report Template Quality
- [model-registry-operator](https://github.com/opendatahub-io/model-registry-operator) (69) -- top gap: Test-to-Source Ratio
- [llama-stack-k8s-operator](https://github.com/opendatahub-io/llama-stack-k8s-operator) (68) -- top gap: Bug Report Template Quality
- [maas-billing](https://github.com/opendatahub-io/maas-billing) (68) -- top gap: Bug Report Template Quality
- [trainer](https://github.com/opendatahub-io/trainer) (66) -- top gap: Test-to-Source Ratio
- [training-operator](https://github.com/opendatahub-io/training-operator) (66) -- top gap: Test-to-Source Ratio
- [kubeflow](https://github.com/opendatahub-io/kubeflow) (65) -- top gap: Bug Report Template Quality
- [odh-model-controller](https://github.com/opendatahub-io/odh-model-controller) (64) -- top gap: Bug Report Template Quality

### Needs Work (40-59) -- 1 repos

- [trustyai-service-operator](https://github.com/opendatahub-io/trustyai-service-operator) (56) -- top gap: Bug Report Template Quality

### Not Ready (<40) -- 1 repos

- [odh-gitops](https://github.com/opendatahub-io/odh-gitops) (9)

## Repository Scores

| Repository | Score | Level | Languages |
|---|---|---|---|
| [data-science-pipelines-operator](https://github.com/opendatahub-io/data-science-pipelines-operator) | 80/100 | Ready | Go, Python |
| [odh-dashboard](https://github.com/opendatahub-io/odh-dashboard) | 80/100 | Ready | TypeScript, Go, JavaScript |
| [feast](https://github.com/opendatahub-io/feast) | 79/100 | Partially Ready | Python, TypeScript, Go |
| [kserve](https://github.com/opendatahub-io/kserve) | 77/100 | Partially Ready | Python, Go |
| [spark-operator](https://github.com/opendatahub-io/spark-operator) | 76/100 | Partially Ready | Go, Python |
| [kuberay](https://github.com/opendatahub-io/kuberay) | 74/100 | Partially Ready | Go, Python, TypeScript |
| [opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) | 72/100 | Partially Ready | Go, JavaScript, Python |
| [notebooks](https://github.com/opendatahub-io/notebooks) | 70/100 | Partially Ready | Python |
| [mlflow-operator](https://github.com/opendatahub-io/mlflow-operator) | 69/100 | Partially Ready | Python, Go |
| [model-registry-operator](https://github.com/opendatahub-io/model-registry-operator) | 69/100 | Partially Ready | Go |
| [llama-stack-k8s-operator](https://github.com/opendatahub-io/llama-stack-k8s-operator) | 68/100 | Partially Ready | Go |
| [maas-billing](https://github.com/opendatahub-io/maas-billing) | 68/100 | Partially Ready | Go, Python |
| [trainer](https://github.com/opendatahub-io/trainer) | 66/100 | Partially Ready | Python, Go, Rust |
| [training-operator](https://github.com/opendatahub-io/training-operator) | 66/100 | Partially Ready | Go, Python |
| [kubeflow](https://github.com/opendatahub-io/kubeflow) | 65/100 | Partially Ready | Go |
| [odh-model-controller](https://github.com/opendatahub-io/odh-model-controller) | 64/100 | Partially Ready | Go |
| [trustyai-service-operator](https://github.com/opendatahub-io/trustyai-service-operator) | 56/100 | Needs Work | Go |
| [odh-gitops](https://github.com/opendatahub-io/odh-gitops) (verify gate) | 9/100 | Not Ready | Unknown |

## Quick Wins (Highest Impact Actions)

| Action | Repos Below 40 | Weight | How to Fix |
|---|---|---|---|
| AI Context Files | 14 repos | 5% | Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug. |

## All Checks Ranked by Average Score

| Check | Avg Score | Weight |
|---|---|---|
| AI Context Files | 22/100 | 5% |
| Bug Report Template Quality | 51/100 | 12% |
| Code Ownership (CODEOWNERS) | 52/100 | 3% |
| Coverage Configuration | 57/100 | 5% |
| Test-to-Source Ratio | 65/100 | 17% |
| PR Template | 65/100 | 3% |
| Contributing / Dev Guide | 67/100 | 5% |
| Code Navigability | 69/100 | 8% |
| One-Command Test Execution | 74/100 | 12% |
| Linting / Formatting in CI | 76/100 | 5% |
| Test Isolation (unit vs e2e) | 76/100 | 5% |
| Structured Logging / Errors | 81/100 | 5% |
| Generated Code Ratio | 89/100 | 5% |
| CI Runs Tests on PRs | 93/100 | 10% |

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

### odh-dashboard -- 80/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (4/7 quality keywords); claude.md found (4/7 quality keywords); AGENTS.md found (4/7 quality keywords); Agents.md found (4/7 quality keywords); agents.md found (4/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (7/50 sampled files); Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 117 lines (5474 source files, generated excluded); Files >500 lines: 166 (3%); Largest: mockPipelineSpec.ts (5220L), modelServingDeploy.cy.ts (2747L), workbench.cy.ts (2568L) |
| Generated Code Ratio | Navigate | 5% | 100 | 46/5529 files are generated (1%); Examples: maas_models_mock.go, http_mock.go, token_k8s_client_mock.go, internal_k8s_client_mock.go, mock_factory.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 1076 test files / 4407 source files (ratio: 0.24) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: packages/maas/test; npm test script defined |
| Coverage Configuration | Verify | 5% | 60 | Codecov configured; Coverage in CI workflow: test.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test.yml, gen-ai-frontend-build.yml, maas-bff-tests.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: gen-ai-bff-build.yml, maas-bff-tests.yml, modular-arch-quality-gates.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~89% unit tests, ~11% infra-dependent (24/27 sampled) |

### feast -- 79/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (logr) found in go.mod; Go structured logging (zerolog) found in go.mod; Error wrapping patterns (8 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 198 lines (1040 source files, generated excluded); Files >500 lines: 98 (9%); Largest: feature_store.py (3288L), ray.py (2370L), test_search_api.py (2290L) |
| Generated Code Ratio | Navigate | 5% | 100 | 2/1190 files are generated (0%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (CODEOWNERS) with 18 rules |
| Test-to-Source Ratio | Verify | 17% | 50 | 339 test files / 849 source files (ratio: 0.40) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, infra/feast-operator/test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 13 CI workflow(s): release.yml, pr_registration_integration_tests.yml, pr_local_integration_tests.yml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: linter.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### kserve -- 77/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 292 lines (877 source files, generated excluded); Files >500 lines: 124 (14%); Largest: rawkube_controller_test.go (10372L), storage_initializer_injector_test.go (5443L), controller_test.go (5032L) |
| Generated Code Ratio | Navigate | 5% | 80 | 111/1005 files are generated (11%); Examples: api_def.pb.go, graph.pb.go, step_stats.pb.go, function.pb.go, tensor_shape.pb.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 411 test files / 483 source files (ratio: 0.85) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, tools/tf2openapi/test, python/xgbserver/test, python/aiffairness/test, python/lgbserver/test, python/paddleserver/test, python/kserve/test, python/huggingfaceserver/test, python/custom_model/test, python/predictiveserver/test, python/custom_transformer/test, python/pmmlserver/test, python/artexplainer/test, python/sklearnserver/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile; Coverage in CI workflow: go.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): go.yml, python-test.yml, e2e-test-llmisvc.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 60 | Found: CONTRIBUTING.md; 1/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~90% unit tests, ~10% infra-dependent (27/30 sampled) |

### spark-operator -- 76/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (13/50 sampled files); Error wrapping patterns (15 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 215 lines (128 source files, generated excluded); Files >500 lines: 10 (8%); Largest: sparkpod_defaulter_test.go (2351L), controller.go (1472L), controller_test.go (1440L) |
| Generated Code Ratio | Navigate | 5% | 60 | 27/155 files are generated (17%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, factory.go, generic.go, factory_interfaces.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 37 test files / 91 source files (ratio: 0.41) |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: unit-test, e2e-test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): openshift-docling-e2e.yaml, integration.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: integration.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~90% unit tests, ~10% infra-dependent (26/29 sampled) |

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

### opendatahub-operator -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 45 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has environment/version fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (9/50 sampled files); Error wrapping patterns (14 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 201 lines (526 source files, generated excluded); Files >500 lines: 50 (10%); Largest: mutating_test.go (2768L), monitoring_test.go (2278L), test_context_test.go (2099L) |
| Generated Code Ratio | Navigate | 5% | 100 | 15/541 files are generated (3%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 186 test files / 340 source files (ratio: 0.55) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, unit-test, e2e-test, e2e-test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Codecov configured; Go coverage flags in Makefile; Coverage in CI workflow: security-full-scan.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): test-gateway-integration.yaml, test-unit.yaml, test-unit-cli.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: security-full-scan.yml, test-linter.yaml |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 50 | ~48% unit tests, ~52% infra-dependent (12/25 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### notebooks -- 70/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | AGENTS.md found (6/7 quality keywords); Agents.md found (6/7 quality keywords); agents.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 197 lines (15 source files, generated excluded); Files >500 lines: 1 (7%); Largest: konflux_generate_component_build_pipelines.py (866L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/17 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 3 test files / 14 source files (ratio: 0.21) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): build-notebooks-TEMPLATE.yaml, code-quality.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: software-versions.yaml, notebooks-digest-updater.yaml, pr-merge-image-delete.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |

### mlflow-operator -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (6/50 sampled files); Error wrapping patterns (16 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 197 lines (50 source files, generated excluded); Files >500 lines: 5 (10%); Largest: helm_test.go (1735L), deploy.py (1010L), mlflow_controller.go (532L) |
| Generated Code Ratio | Navigate | 5% | 100 | 2/52 files are generated (4%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 24 test files / 26 source files (ratio: 0.92) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test.yml, integration-tests.yml, test-e2e.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~89% unit tests, ~11% infra-dependent (8/9 sampled) |

### model-registry-operator -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (16/38 sampled files); Error wrapping patterns (14 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 308 lines (38 source files, generated excluded); Files >500 lines: 6 (16%); Largest: modelcatalog_controller_test.go (1379L), modelregistry_controller_test.go (1236L), modelcatalog_controller.go (1159L) |
| Generated Code Ratio | Navigate | 5% | 80 | 3/41 files are generated (7%); Examples: zz_generated.deepcopy.go, zz_generated.conversion.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 70 | 13 test files / 25 source files (ratio: 0.52) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started, Build, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~54% unit tests, ~46% infra-dependent (7/13 sampled) |

### llama-stack-k8s-operator -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (4) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (19/44 sampled files); Error wrapping patterns (17 files) |
| Code Navigability | Navigate | 8% | 50 | Average file: 284 lines (44 source files, generated excluded); Files >500 lines: 10 (23%); Largest: llamastackdistribution_controller.go (1927L), resource_helper_test.go (1056L), llamastackdistribution_controller_test.go (990L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 1/45 files are generated (2%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 100 | 23 test files / 21 source files (ratio: 1.10) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile; Coverage in CI workflow: code-coverage.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): run-e2e-test.yml, generate-release.yml, code-coverage.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml, generate-release.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 50 | ~45% unit tests, ~55% infra-dependent (9/20 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### maas-billing -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (15/50 sampled files); Error wrapping patterns (16 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 183 lines (83 source files, generated excluded); Files >500 lines: 9 (11%); Largest: handler_test.go (1149L), test_subscription.py (697L), maasauthpolicy_controller.go (680L) |
| Generated Code Ratio | Navigate | 5% | 100 | 2/85 files are generated (2%); Examples: zz_generated.deepcopy.go, store_mock.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 32 test files / 51 source files (ratio: 0.63) |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: maas-controller/test, maas-api/test |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: maas-api-ci.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): maas-api-ci.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: maas-api-ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~96% unit tests, ~4% infra-dependent (25/26 sampled) |

### trainer -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (8 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 142 lines (528 source files, generated excluded); Files >500 lines: 16 (3%); Largest: framework_test.go (2625L), trainingruntime_test.go (1865L), progression_test.go (1764L) |
| Generated Code Ratio | Navigate | 5% | 80 | 34/566 files are generated (6%); Examples: zz_generated.defaults.go, zz_generated.deepcopy.go, zz_generated.openapi.go, zz_generated.defaults.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 25 | 66 test files / 466 source files (ratio: 0.14) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): test-rust.yaml, test-go.yaml, test-e2e.yaml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test-go.yaml, test-python.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 100 | ~96% unit tests, ~4% infra-dependent (26/27 sampled); Makefile separates unit and integration test targets |

### training-operator -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (12 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 187 lines (254 source files, generated excluded); Files >500 lines: 18 (7%); Largest: training_client_test.py (1995L), training_client.py (1558L), mpijob_controller.go (1400L) |
| Generated Code Ratio | Navigate | 5% | 60 | 69/326 files are generated (21%); Examples: zz_generated.defaults.go, openapi_generated.go, zz_generated.deepcopy.go, factory.go, generic.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 67 test files / 190 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 4 CI workflow(s): unittests.yaml, test-python.yaml, integration-tests.yaml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test-go.yaml, pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~87% unit tests, ~13% infra-dependent (26/30 sampled) |

### kubeflow -- 65/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Good logging coverage (22/50 sampled files); Error wrapping patterns (15 files) |
| Code Navigability | Navigate | 8% | 50 | Average file: 320 lines (50 source files, generated excluded); Files >500 lines: 11 (22%); Largest: notebook_controller_test.go (1971L), notebook_webhook.go (894L), notebook_dspa_secret_test.go (888L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 80 | 3/53 files are generated (6%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 20 test files / 30 source files (ratio: 0.67) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: components/odh-notebook-controller/test, components/odh-notebook-controller/e2e-test, components/notebook-controller/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: notebook_controller_unit_test.yaml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): notebook_controller_unit_test.yaml, odh_notebook_controller_unit_test.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: code-quality.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~69% unit tests, ~31% infra-dependent (11/16 sampled) |

### odh-model-controller -- 64/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (24/50 sampled files); Error wrapping patterns (14 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 209 lines (138 source files, generated excluded); Files >500 lines: 12 (9%); Largest: llm_inferenceservice_controller_test.go (1526L), configmap_handler_test.go (999L), inferenceservice_controller_test.go (947L) |
| Generated Code Ratio | Navigate | 5% | 100 | 1/139 files are generated (1%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 45 test files / 93 source files (ratio: 0.48) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, test-e2e.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started, Develop, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~70% unit tests, ~30% infra-dependent (21/30 sampled) |

### trustyai-service-operator -- 56/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (15/50 sampled files); Error wrapping patterns (5 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 242 lines (131 source files, generated excluded); Files >500 lines: 15 (11%); Largest: lmevaljob_controller_test.go (4373L), lmevaljob_controller_validation_test.go (1798L), unit_test.go (1680L) |
| Generated Code Ratio | Navigate | 5% | 100 | 6/137 files are generated (4%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 33 test files / 98 source files (ratio: 0.34) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, tests/test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): controller-tests.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint-yaml.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~70% unit tests, ~30% infra-dependent (21/30 sampled) |

### odh-gitops -- 9/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create a CLAUDE.md or AGENTS.md at the repo root describing architecture, how to build, test, and debug.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: helm.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

---
*AI Bug Automation Readiness Report -- Generated 2026-03-06 17:59*
