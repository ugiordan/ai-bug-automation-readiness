# AI Bug Automation Readiness Report

*130 repositories assessed -- 2026-03-09 16:38*

> 43 of 130 repositories are partially ready or above for AI-assisted bug fixing. The ecosystem averages 38/100. The biggest gap is "AI Context Files" (avg 14/100).

## How Scoring Works

**Overall score** = weighted average of 14 checks, each scored 0-100.

**Phases**: Understand (22%), Navigate (13%), Verify (49%), Submit (16%).

**Verify phase gate:** If the average Verify score is below 50, the overall score receives a smooth penalty multiplier that scales linearly from x0.4 (verify avg = 0) to x1.0 (verify avg = 50).

| Level | Score | Meaning |
|---|---|---|
| Ready | 80+ | Strong test infrastructure, good context, CI validates fixes |
| Partially Ready | 60-79 | Workable but has gaps that may cause AI agent failures |
| Needs Work | 40-59 | Missing key capabilities; fix gaps before AI bug bash |
| Not Ready | <40 | Fundamental gaps in test infrastructure or code structure |

## Summary

| Metric | Value |
|---|---|
| Average Score | 38/100 |
| Ready (80+) | 1 |
| Partially Ready (60-79) | 42 |
| Needs Work (40-59) | 27 |
| Not Ready (<40) | 60 |

## Phase Scores (Ecosystem Average)

| Phase | Weight | Average |
|---|---|---|
| Understand | 22% | 24/100 |
| Navigate | 13% | 76/100 |
| Verify | 49% | 42/100 |
| Submit | 16% | 36/100 |

## Bug Bash Shortlist

### Ready (80+) -- 1 repos

- [data-science-pipelines-operator](https://github.com/opendatahub-io/data-science-pipelines-operator) (80)

### Partially Ready (60-79) -- 42 repos

- [feast](https://github.com/opendatahub-io/feast) (79) -- top gap: Test-to-Source Ratio
- [kube-auth-proxy](https://github.com/opendatahub-io/kube-auth-proxy) (78) -- top gap: CI Runs Tests on PRs
- [modelmesh-serving](https://github.com/opendatahub-io/modelmesh-serving) (78) -- top gap: Test-to-Source Ratio
- [odh-dashboard](https://github.com/opendatahub-io/odh-dashboard) (78) -- top gap: Test-to-Source Ratio
- [eval-hub](https://github.com/opendatahub-io/eval-hub) (78) -- top gap: CI Runs Tests on PRs
- [kserve](https://github.com/opendatahub-io/kserve) (77) -- top gap: AI Context Files
- [spark-operator](https://github.com/opendatahub-io/spark-operator) (76) -- top gap: Test-to-Source Ratio
- [kuberay](https://github.com/opendatahub-io/kuberay) (74) -- top gap: AI Context Files
- [model-registry](https://github.com/opendatahub-io/model-registry) (74) -- top gap: Test-to-Source Ratio
- [argo-workflows](https://github.com/opendatahub-io/argo-workflows) (74) -- top gap: Test-to-Source Ratio
- [litellm](https://github.com/opendatahub-io/litellm) (74) -- top gap: Coverage Configuration
- [llm-d-inference-scheduler](https://github.com/opendatahub-io/llm-d-inference-scheduler) (74) -- top gap: AI Context Files
- [NeMo-Guardrails](https://github.com/opendatahub-io/NeMo-Guardrails) (74) -- top gap: AI Context Files
- [data-science-pipelines](https://github.com/opendatahub-io/data-science-pipelines) (73) -- top gap: Test-to-Source Ratio
- [workload-variant-autoscaler](https://github.com/opendatahub-io/workload-variant-autoscaler) (72) -- top gap: Bug Report Template Quality
- [opendatahub-tests](https://github.com/opendatahub-io/opendatahub-tests) (71) -- top gap: Coverage Configuration
- [model-registry-bf4-kf](https://github.com/opendatahub-io/model-registry-bf4-kf) (70) -- top gap: Test-to-Source Ratio
- [models-as-a-service](https://github.com/opendatahub-io/models-as-a-service) (70) -- top gap: Bug Report Template Quality
- [opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) (69) -- top gap: Bug Report Template Quality
- [notebooks](https://github.com/opendatahub-io/notebooks) (69) -- top gap: Test-to-Source Ratio
- [mlflow-operator](https://github.com/opendatahub-io/mlflow-operator) (69) -- top gap: Bug Report Template Quality
- [model-registry-operator](https://github.com/opendatahub-io/model-registry-operator) (69) -- top gap: Test-to-Source Ratio
- [training-operator](https://github.com/opendatahub-io/training-operator) (69) -- top gap: Test-to-Source Ratio
- [llama-stack-k8s-operator](https://github.com/opendatahub-io/llama-stack-k8s-operator) (68) -- top gap: Bug Report Template Quality
- [trustyai-explainability](https://github.com/opendatahub-io/trustyai-explainability) (68) -- top gap: Test-to-Source Ratio
- [caikit-nlp](https://github.com/opendatahub-io/caikit-nlp) (66) -- top gap: Test-to-Source Ratio
- [base-containers](https://github.com/opendatahub-io/base-containers) (66) -- top gap: Bug Report Template Quality
- [trainer](https://github.com/opendatahub-io/trainer) (66) -- top gap: Test-to-Source Ratio
- [trainer-sdk](https://github.com/opendatahub-io/trainer-sdk) (66) -- top gap: Test-to-Source Ratio
- [kubeflow](https://github.com/opendatahub-io/kubeflow) (65) -- top gap: Bug Report Template Quality
- [odh-model-controller](https://github.com/opendatahub-io/odh-model-controller) (64) -- top gap: Bug Report Template Quality
- [training-notebooks](https://github.com/opendatahub-io/training-notebooks) (64) -- top gap: Test-to-Source Ratio
- [rhoai-mcp](https://github.com/opendatahub-io/rhoai-mcp) (63) -- top gap: Bug Report Template Quality
- [odh-cli](https://github.com/opendatahub-io/odh-cli) (63) -- top gap: Bug Report Template Quality
- [model-metadata-collection](https://github.com/opendatahub-io/model-metadata-collection) (62) -- top gap: Bug Report Template Quality
- [modelmesh-runtime-adapter](https://github.com/opendatahub-io/modelmesh-runtime-adapter) (62) -- top gap: Bug Report Template Quality
- [kube-authkit](https://github.com/opendatahub-io/kube-authkit) (62) -- top gap: Bug Report Template Quality
- [mlflow](https://github.com/opendatahub-io/mlflow) (61) -- top gap: Bug Report Template Quality
- [mcp-server-operator](https://github.com/opendatahub-io/mcp-server-operator) (61) -- top gap: Bug Report Template Quality
- [llm-d-kv-cache](https://github.com/opendatahub-io/llm-d-kv-cache) (60) -- top gap: Bug Report Template Quality
- [MLServer](https://github.com/opendatahub-io/MLServer) (60) -- top gap: Bug Report Template Quality
- [llama-stack](https://github.com/opendatahub-io/llama-stack) (60) -- top gap: Bug Report Template Quality

### Needs Work (40-59) -- 27 repos

- [caikit-nlp-client](https://github.com/opendatahub-io/caikit-nlp-client) (59) -- top gap: Bug Report Template Quality
- [rest-proxy](https://github.com/opendatahub-io/rest-proxy) (59) -- top gap: Bug Report Template Quality
- [trustyai-service-operator](https://github.com/opendatahub-io/trustyai-service-operator) (59) -- top gap: Bug Report Template Quality
- [elyra](https://github.com/opendatahub-io/elyra) (57) -- top gap: Bug Report Template Quality
- [mod-arch-library](https://github.com/opendatahub-io/mod-arch-library) (56) -- top gap: Test-to-Source Ratio
- [codeflare-operator](https://github.com/opendatahub-io/codeflare-operator) (55) -- top gap: Bug Report Template Quality
- [kubeflow-sdk](https://github.com/opendatahub-io/kubeflow-sdk) (55) -- top gap: One-Command Test Execution
- [vllm-tgis-adapter](https://github.com/opendatahub-io/vllm-tgis-adapter) (54) -- top gap: Bug Report Template Quality
- [codeflare-operator-poc](https://github.com/opendatahub-io/codeflare-operator-poc) (54) -- top gap: Bug Report Template Quality
- [openvino_model_server](https://github.com/opendatahub-io/openvino_model_server) (51) -- top gap: One-Command Test Execution
- [kueue](https://github.com/opendatahub-io/kueue) (51) -- top gap: One-Command Test Execution
- [elyra-pipeline-editor](https://github.com/opendatahub-io/elyra-pipeline-editor) (50) -- top gap: Bug Report Template Quality
- [batch-gateway](https://github.com/opendatahub-io/batch-gateway) (50) -- top gap: Bug Report Template Quality
- [guardrails-detectors](https://github.com/opendatahub-io/guardrails-detectors) (50) -- top gap: Bug Report Template Quality
- [vllm-gaudi](https://github.com/opendatahub-io/vllm-gaudi) (50) -- top gap: Bug Report Template Quality
- [llama-stack-provider-ragas](https://github.com/opendatahub-io/llama-stack-provider-ragas) (48) -- top gap: Bug Report Template Quality
- [elyra-examples](https://github.com/opendatahub-io/elyra-examples) (47) -- top gap: Test-to-Source Ratio
- [openvino_contrib](https://github.com/opendatahub-io/openvino_contrib) (47) -- top gap: One-Command Test Execution
- [fms-guardrails-orchestrator](https://github.com/opendatahub-io/fms-guardrails-orchestrator) (47) -- top gap: One-Command Test Execution
- [odh-ide-extensions](https://github.com/opendatahub-io/odh-ide-extensions) (46) -- top gap: Bug Report Template Quality
- [distributed-workloads](https://github.com/opendatahub-io/distributed-workloads) (45) -- top gap: Bug Report Template Quality
- [llama-stack-provider-trustyai-garak](https://github.com/opendatahub-io/llama-stack-provider-trustyai-garak) (45) -- top gap: Bug Report Template Quality
- [mlflow-go](https://github.com/opendatahub-io/mlflow-go) (44) -- top gap: Bug Report Template Quality
- [lm-evaluation-harness](https://github.com/opendatahub-io/lm-evaluation-harness) (44) -- top gap: Test-to-Source Ratio
- [modelmesh](https://github.com/opendatahub-io/modelmesh) (44) -- top gap: Bug Report Template Quality
- [modelcar-base-image](https://github.com/opendatahub-io/modelcar-base-image) (44) -- top gap: Bug Report Template Quality
- [data-processing](https://github.com/opendatahub-io/data-processing) (43) -- top gap: Test-to-Source Ratio

### Not Ready (<40) -- 60 repos

- [llama-stack-provider-kfp-trainer](https://github.com/opendatahub-io/llama-stack-provider-kfp-trainer) (39)
- [llama-stack-client-python](https://github.com/opendatahub-io/llama-stack-client-python) (38)
- [perf_analyzer](https://github.com/opendatahub-io/perf_analyzer) (35)
- [fips-compliance-checker-claude-code-plugin](https://github.com/opendatahub-io/fips-compliance-checker-claude-code-plugin) (34)
- [caikit-tgis-serving](https://github.com/opendatahub-io/caikit-tgis-serving) (32)
- [openvino_tokenizers](https://github.com/opendatahub-io/openvino_tokenizers) (31)
- [odh-s2i-project-cds](https://github.com/opendatahub-io/odh-s2i-project-cds) (26)
- [rag](https://github.com/opendatahub-io/rag) (25)
- [llama-stack-demos](https://github.com/opendatahub-io/llama-stack-demos) (24)
- [openvino.genai](https://github.com/opendatahub-io/openvino.genai) (22)
- [ml-metadata](https://github.com/opendatahub-io/ml-metadata) (22)
- [openvino](https://github.com/opendatahub-io/openvino) (21)
- [llama-stack-distribution](https://github.com/opendatahub-io/llama-stack-distribution) (20)
- [rhaii-on-xks](https://github.com/opendatahub-io/rhaii-on-xks) (20)
- [client](https://github.com/opendatahub-io/client) (19)
- [odh-s2i-project-cookiecutter](https://github.com/opendatahub-io/odh-s2i-project-cookiecutter) (18)
- [ai-helpers](https://github.com/opendatahub-io/ai-helpers) (14)
- [vllm-orchestrator-gateway](https://github.com/opendatahub-io/vllm-orchestrator-gateway) (13)
- [agents](https://github.com/opendatahub-io/agents) (12)
- [llama-stack-provider-instructlab-train](https://github.com/opendatahub-io/llama-stack-provider-instructlab-train) (10)
- [llama-stack-provider-kft](https://github.com/opendatahub-io/llama-stack-provider-kft) (10)
- [odh-gitops](https://github.com/opendatahub-io/odh-gitops) (9)
- [opendatahub.io](https://github.com/opendatahub-io/opendatahub.io) (9)
- [opendatahub-community](https://github.com/opendatahub-io/opendatahub-community) (8)
- [opendatahub-documentation](https://github.com/opendatahub-io/opendatahub-documentation) (6)
- [odh-konflux-central](https://github.com/opendatahub-io/odh-konflux-central) (6)
- [odh-s2i-project-simple](https://github.com/opendatahub-io/odh-s2i-project-simple) (6)
- [model-runtimes-agent](https://github.com/opendatahub-io/model-runtimes-agent) (5)
- [dsp-dev-tools](https://github.com/opendatahub-io/dsp-dev-tools) (5)
- [guardrails-regex-detector](https://github.com/opendatahub-io/guardrails-regex-detector) (5)
- [odh-build-metadata](https://github.com/opendatahub-io/odh-build-metadata) (5)
- [ODH-Build-Config](https://github.com/opendatahub-io/ODH-Build-Config) (5)
- [architecture-decision-records](https://github.com/opendatahub-io/architecture-decision-records) (3)
- [community-operators-prod](https://github.com/opendatahub-io/community-operators-prod) (3)
- [opendatahub.io-redirects](https://github.com/opendatahub-io/opendatahub.io-redirects) (3)
- [openvino-repo-syncher](https://github.com/opendatahub-io/openvino-repo-syncher) (3)
- [kserve-raw-migration](https://github.com/opendatahub-io/kserve-raw-migration) (3)
- [odh-template-sig](https://github.com/opendatahub-io/odh-template-sig) (3)
- [runbooks](https://github.com/opendatahub-io/runbooks) (3)
- [security-config](https://github.com/opendatahub-io/security-config) (3)
- [sig-ml-developer-experience](https://github.com/opendatahub-io/sig-ml-developer-experience) (3)
- [sig-platform](https://github.com/opendatahub-io/sig-platform) (3)
- [workload-orchestration](https://github.com/opendatahub-io/workload-orchestration) (3)
- [.github](https://github.com/opendatahub-io/.github) (2)
- [aaet-devtools](https://github.com/opendatahub-io/aaet-devtools) (2)
- [ai-engineering-process-docs](https://github.com/opendatahub-io/ai-engineering-process-docs) (2)
- [coderabbit](https://github.com/opendatahub-io/coderabbit) (2)
- [feast-demo](https://github.com/opendatahub-io/feast-demo) (2)
- [feast-labs](https://github.com/opendatahub-io/feast-labs) (2)
- [guides-vllm-llm-d](https://github.com/opendatahub-io/guides-vllm-llm-d) (2)
- [kc-rep](https://github.com/opendatahub-io/kc-rep) (2)
- [kserve-migration](https://github.com/opendatahub-io/kserve-migration) (2)
- [llm-d-playbooks](https://github.com/opendatahub-io/llm-d-playbooks) (2)
- [odh-automation-serving](https://github.com/opendatahub-io/odh-automation-serving) (2)
- [odh-doc-examples](https://github.com/opendatahub-io/odh-doc-examples) (2)
- [odh-observability](https://github.com/opendatahub-io/odh-observability) (2)
- [rhaii-cluster-validation](https://github.com/opendatahub-io/rhaii-cluster-validation) (2)
- [sample-gam-trigger-workflow](https://github.com/opendatahub-io/sample-gam-trigger-workflow) (2)
- [sdg-hub](https://github.com/opendatahub-io/sdg-hub) (2)
- [test-repo](https://github.com/opendatahub-io/test-repo) (2)

## Repository Scores

| Repository | Score | Level | Languages |
|---|---|---|---|
| [data-science-pipelines-operator](https://github.com/opendatahub-io/data-science-pipelines-operator) | 80/100 | Ready | Go, Python |
| [feast](https://github.com/opendatahub-io/feast) | 79/100 | Partially Ready | Python, TypeScript, Go |
| [kube-auth-proxy](https://github.com/opendatahub-io/kube-auth-proxy) | 78/100 | Partially Ready | Go, JavaScript |
| [modelmesh-serving](https://github.com/opendatahub-io/modelmesh-serving) | 78/100 | Partially Ready | Go, Python |
| [odh-dashboard](https://github.com/opendatahub-io/odh-dashboard) | 78/100 | Partially Ready | TypeScript, Go, JavaScript |
| [eval-hub](https://github.com/opendatahub-io/eval-hub) | 78/100 | Partially Ready | Go, Python |
| [kserve](https://github.com/opendatahub-io/kserve) | 77/100 | Partially Ready | Python, Go |
| [spark-operator](https://github.com/opendatahub-io/spark-operator) | 76/100 | Partially Ready | Go, Python |
| [kuberay](https://github.com/opendatahub-io/kuberay) | 74/100 | Partially Ready | Go, Python, TypeScript |
| [model-registry](https://github.com/opendatahub-io/model-registry) | 74/100 | Partially Ready | TypeScript, Go, Python |
| [argo-workflows](https://github.com/opendatahub-io/argo-workflows) | 74/100 | Partially Ready | Go, Python, TypeScript |
| [litellm](https://github.com/opendatahub-io/litellm) | 74/100 | Partially Ready | Python, TypeScript, JavaScript |
| [llm-d-inference-scheduler](https://github.com/opendatahub-io/llm-d-inference-scheduler) | 74/100 | Partially Ready | Go |
| [NeMo-Guardrails](https://github.com/opendatahub-io/NeMo-Guardrails) | 74/100 | Partially Ready | Python, JavaScript |
| [data-science-pipelines](https://github.com/opendatahub-io/data-science-pipelines) | 73/100 | Partially Ready | Python, TypeScript, Go |
| [workload-variant-autoscaler](https://github.com/opendatahub-io/workload-variant-autoscaler) | 72/100 | Partially Ready | Go |
| [opendatahub-tests](https://github.com/opendatahub-io/opendatahub-tests) | 71/100 | Partially Ready | Python |
| [model-registry-bf4-kf](https://github.com/opendatahub-io/model-registry-bf4-kf) | 70/100 | Partially Ready | Go, Python |
| [models-as-a-service](https://github.com/opendatahub-io/models-as-a-service) | 70/100 | Partially Ready | Go, Python |
| [opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) | 69/100 | Partially Ready | Go, JavaScript, Python |
| [notebooks](https://github.com/opendatahub-io/notebooks) | 69/100 | Partially Ready | Python |
| [mlflow-operator](https://github.com/opendatahub-io/mlflow-operator) | 69/100 | Partially Ready | Python, Go |
| [model-registry-operator](https://github.com/opendatahub-io/model-registry-operator) | 69/100 | Partially Ready | Go |
| [training-operator](https://github.com/opendatahub-io/training-operator) | 69/100 | Partially Ready | Go, Python |
| [llama-stack-k8s-operator](https://github.com/opendatahub-io/llama-stack-k8s-operator) | 68/100 | Partially Ready | Go |
| [trustyai-explainability](https://github.com/opendatahub-io/trustyai-explainability) | 68/100 | Partially Ready | Java, Python |
| [caikit-nlp](https://github.com/opendatahub-io/caikit-nlp) | 66/100 | Partially Ready | Python |
| [base-containers](https://github.com/opendatahub-io/base-containers) | 66/100 | Partially Ready | Python |
| [trainer](https://github.com/opendatahub-io/trainer) | 66/100 | Partially Ready | Python, Go, Rust |
| [trainer-sdk](https://github.com/opendatahub-io/trainer-sdk) | 66/100 | Partially Ready | Python, Go |
| [kubeflow](https://github.com/opendatahub-io/kubeflow) | 65/100 | Partially Ready | Go |
| [odh-model-controller](https://github.com/opendatahub-io/odh-model-controller) | 64/100 | Partially Ready | Go |
| [training-notebooks](https://github.com/opendatahub-io/training-notebooks) | 64/100 | Partially Ready | Python, TypeScript, Go |
| [rhoai-mcp](https://github.com/opendatahub-io/rhoai-mcp) | 63/100 | Partially Ready | Python |
| [odh-cli](https://github.com/opendatahub-io/odh-cli) | 63/100 | Partially Ready | Go |
| [model-metadata-collection](https://github.com/opendatahub-io/model-metadata-collection) | 62/100 | Partially Ready | Go |
| [modelmesh-runtime-adapter](https://github.com/opendatahub-io/modelmesh-runtime-adapter) | 62/100 | Partially Ready | Go |
| [kube-authkit](https://github.com/opendatahub-io/kube-authkit) | 62/100 | Partially Ready | Python |
| [mlflow](https://github.com/opendatahub-io/mlflow) | 61/100 | Partially Ready | Python, TypeScript, JavaScript |
| [mcp-server-operator](https://github.com/opendatahub-io/mcp-server-operator) | 61/100 | Partially Ready | Go |
| [llm-d-kv-cache](https://github.com/opendatahub-io/llm-d-kv-cache) | 60/100 | Partially Ready | Go, Python, C++ |
| [MLServer](https://github.com/opendatahub-io/MLServer) | 60/100 | Partially Ready | Python, JavaScript |
| [llama-stack](https://github.com/opendatahub-io/llama-stack) | 60/100 | Partially Ready | Python, TypeScript, JavaScript |
| [caikit-nlp-client](https://github.com/opendatahub-io/caikit-nlp-client) | 59/100 | Needs Work | Python |
| [rest-proxy](https://github.com/opendatahub-io/rest-proxy) | 59/100 | Needs Work | Go |
| [trustyai-service-operator](https://github.com/opendatahub-io/trustyai-service-operator) | 59/100 | Needs Work | Go |
| [elyra](https://github.com/opendatahub-io/elyra) | 57/100 | Needs Work | Python, TypeScript, JavaScript |
| [mod-arch-library](https://github.com/opendatahub-io/mod-arch-library) | 56/100 | Needs Work | TypeScript, Go, JavaScript |
| [codeflare-operator](https://github.com/opendatahub-io/codeflare-operator) | 55/100 | Needs Work | Go |
| [kubeflow-sdk](https://github.com/opendatahub-io/kubeflow-sdk) | 55/100 | Needs Work | Python |
| [vllm-tgis-adapter](https://github.com/opendatahub-io/vllm-tgis-adapter) | 54/100 | Needs Work | Python |
| [codeflare-operator-poc](https://github.com/opendatahub-io/codeflare-operator-poc) | 54/100 | Needs Work | Go |
| [openvino_model_server](https://github.com/opendatahub-io/openvino_model_server) | 51/100 | Needs Work | C++, Python, Go |
| [kueue](https://github.com/opendatahub-io/kueue) (verify gate) | 51/100 | Needs Work | Go, JavaScript, Python |
| [elyra-pipeline-editor](https://github.com/opendatahub-io/elyra-pipeline-editor) | 50/100 | Needs Work | TypeScript, JavaScript |
| [batch-gateway](https://github.com/opendatahub-io/batch-gateway) | 50/100 | Needs Work | Go |
| [guardrails-detectors](https://github.com/opendatahub-io/guardrails-detectors) | 50/100 | Needs Work | Python |
| [vllm-gaudi](https://github.com/opendatahub-io/vllm-gaudi) | 50/100 | Needs Work | Python, C++ |
| [llama-stack-provider-ragas](https://github.com/opendatahub-io/llama-stack-provider-ragas) | 48/100 | Needs Work | Python |
| [elyra-examples](https://github.com/opendatahub-io/elyra-examples) (verify gate) | 47/100 | Needs Work | Python |
| [openvino_contrib](https://github.com/opendatahub-io/openvino_contrib) (verify gate) | 47/100 | Needs Work | C++, TypeScript, Python |
| [fms-guardrails-orchestrator](https://github.com/opendatahub-io/fms-guardrails-orchestrator) (verify gate) | 47/100 | Needs Work | Rust |
| [odh-ide-extensions](https://github.com/opendatahub-io/odh-ide-extensions) | 46/100 | Needs Work | Python, TypeScript, JavaScript |
| [distributed-workloads](https://github.com/opendatahub-io/distributed-workloads) (verify gate) | 45/100 | Needs Work | Go, Python |
| [llama-stack-provider-trustyai-garak](https://github.com/opendatahub-io/llama-stack-provider-trustyai-garak) | 45/100 | Needs Work | Python |
| [mlflow-go](https://github.com/opendatahub-io/mlflow-go) | 44/100 | Needs Work | Go |
| [lm-evaluation-harness](https://github.com/opendatahub-io/lm-evaluation-harness) | 44/100 | Needs Work | Python |
| [modelmesh](https://github.com/opendatahub-io/modelmesh) | 44/100 | Needs Work | Java |
| [modelcar-base-image](https://github.com/opendatahub-io/modelcar-base-image) | 44/100 | Needs Work | Python |
| [data-processing](https://github.com/opendatahub-io/data-processing) | 43/100 | Needs Work | Python |
| [llama-stack-provider-kfp-trainer](https://github.com/opendatahub-io/llama-stack-provider-kfp-trainer) | 39/100 | Not Ready | Python |
| [llama-stack-client-python](https://github.com/opendatahub-io/llama-stack-client-python) (verify gate) | 38/100 | Not Ready | Python |
| [perf_analyzer](https://github.com/opendatahub-io/perf_analyzer) (verify gate) | 35/100 | Not Ready | Python |
| [fips-compliance-checker-claude-code-plugin](https://github.com/opendatahub-io/fips-compliance-checker-claude-code-plugin) (verify gate) | 34/100 | Not Ready | Python |
| [caikit-tgis-serving](https://github.com/opendatahub-io/caikit-tgis-serving) (verify gate) | 32/100 | Not Ready | Unknown |
| [openvino_tokenizers](https://github.com/opendatahub-io/openvino_tokenizers) (verify gate) | 31/100 | Not Ready | C++, Python, JavaScript |
| [odh-s2i-project-cds](https://github.com/opendatahub-io/odh-s2i-project-cds) (verify gate) | 26/100 | Not Ready | Python |
| [rag](https://github.com/opendatahub-io/rag) (verify gate) | 25/100 | Not Ready | Python, Go |
| [llama-stack-demos](https://github.com/opendatahub-io/llama-stack-demos) (verify gate) | 24/100 | Not Ready | Python |
| [openvino.genai](https://github.com/opendatahub-io/openvino.genai) (verify gate) | 22/100 | Not Ready | C |
| [ml-metadata](https://github.com/opendatahub-io/ml-metadata) (verify gate) | 22/100 | Not Ready | Python, Go |
| [openvino](https://github.com/opendatahub-io/openvino) (verify gate) | 21/100 | Not Ready | Python, JavaScript |
| [llama-stack-distribution](https://github.com/opendatahub-io/llama-stack-distribution) (verify gate) | 20/100 | Not Ready | Unknown |
| [rhaii-on-xks](https://github.com/opendatahub-io/rhaii-on-xks) (verify gate) | 20/100 | Not Ready | Unknown |
| [client](https://github.com/opendatahub-io/client) (verify gate) | 19/100 | Not Ready | Python, Java |
| [odh-s2i-project-cookiecutter](https://github.com/opendatahub-io/odh-s2i-project-cookiecutter) (verify gate) | 18/100 | Not Ready | Python |
| [ai-helpers](https://github.com/opendatahub-io/ai-helpers) (verify gate) | 14/100 | Not Ready | Python |
| [vllm-orchestrator-gateway](https://github.com/opendatahub-io/vllm-orchestrator-gateway) (verify gate) | 13/100 | Not Ready | Rust |
| [agents](https://github.com/opendatahub-io/agents) (verify gate) | 12/100 | Not Ready | Python, Go |
| [llama-stack-provider-instructlab-train](https://github.com/opendatahub-io/llama-stack-provider-instructlab-train) (verify gate) | 10/100 | Not Ready | Python |
| [llama-stack-provider-kft](https://github.com/opendatahub-io/llama-stack-provider-kft) (verify gate) | 10/100 | Not Ready | Python |
| [odh-gitops](https://github.com/opendatahub-io/odh-gitops) (verify gate) | 9/100 | Not Ready | Unknown |
| [opendatahub.io](https://github.com/opendatahub-io/opendatahub.io) (verify gate) | 9/100 | Not Ready | TypeScript |
| [opendatahub-community](https://github.com/opendatahub-io/opendatahub-community) (verify gate) | 8/100 | Not Ready | Unknown |
| [opendatahub-documentation](https://github.com/opendatahub-io/opendatahub-documentation) (verify gate) | 6/100 | Not Ready | Unknown |
| [odh-konflux-central](https://github.com/opendatahub-io/odh-konflux-central) (verify gate) | 6/100 | Not Ready | Unknown |
| [odh-s2i-project-simple](https://github.com/opendatahub-io/odh-s2i-project-simple) (verify gate) | 6/100 | Not Ready | Python |
| [model-runtimes-agent](https://github.com/opendatahub-io/model-runtimes-agent) (verify gate) | 5/100 | Not Ready | Python |
| [dsp-dev-tools](https://github.com/opendatahub-io/dsp-dev-tools) (verify gate) | 5/100 | Not Ready | Python |
| [guardrails-regex-detector](https://github.com/opendatahub-io/guardrails-regex-detector) (verify gate) | 5/100 | Not Ready | Unknown |
| [odh-build-metadata](https://github.com/opendatahub-io/odh-build-metadata) (verify gate) | 5/100 | Not Ready | Python |
| [ODH-Build-Config](https://github.com/opendatahub-io/ODH-Build-Config) (verify gate) | 5/100 | Not Ready | Unknown |
| [architecture-decision-records](https://github.com/opendatahub-io/architecture-decision-records) (verify gate) | 3/100 | Not Ready | Unknown |
| [community-operators-prod](https://github.com/opendatahub-io/community-operators-prod) (verify gate) | 3/100 | Not Ready | Unknown |
| [opendatahub.io-redirects](https://github.com/opendatahub-io/opendatahub.io-redirects) (verify gate) | 3/100 | Not Ready | Unknown |
| [openvino-repo-syncher](https://github.com/opendatahub-io/openvino-repo-syncher) (verify gate) | 3/100 | Not Ready | Unknown |
| [kserve-raw-migration](https://github.com/opendatahub-io/kserve-raw-migration) (verify gate) | 3/100 | Not Ready | Unknown |
| [odh-template-sig](https://github.com/opendatahub-io/odh-template-sig) (verify gate) | 3/100 | Not Ready | Unknown |
| [runbooks](https://github.com/opendatahub-io/runbooks) (verify gate) | 3/100 | Not Ready | Unknown |
| [security-config](https://github.com/opendatahub-io/security-config) (verify gate) | 3/100 | Not Ready | Unknown |
| [sig-ml-developer-experience](https://github.com/opendatahub-io/sig-ml-developer-experience) (verify gate) | 3/100 | Not Ready | Unknown |
| [sig-platform](https://github.com/opendatahub-io/sig-platform) (verify gate) | 3/100 | Not Ready | Unknown |
| [workload-orchestration](https://github.com/opendatahub-io/workload-orchestration) (verify gate) | 3/100 | Not Ready | Unknown |
| [.github](https://github.com/opendatahub-io/.github) (verify gate) | 2/100 | Not Ready | Unknown |
| [aaet-devtools](https://github.com/opendatahub-io/aaet-devtools) (verify gate) | 2/100 | Not Ready | Unknown |
| [ai-engineering-process-docs](https://github.com/opendatahub-io/ai-engineering-process-docs) (verify gate) | 2/100 | Not Ready | Unknown |
| [coderabbit](https://github.com/opendatahub-io/coderabbit) (verify gate) | 2/100 | Not Ready | Unknown |
| [feast-demo](https://github.com/opendatahub-io/feast-demo) (verify gate) | 2/100 | Not Ready | Unknown |
| [feast-labs](https://github.com/opendatahub-io/feast-labs) (verify gate) | 2/100 | Not Ready | Unknown |
| [guides-vllm-llm-d](https://github.com/opendatahub-io/guides-vllm-llm-d) (verify gate) | 2/100 | Not Ready | Unknown |
| [kc-rep](https://github.com/opendatahub-io/kc-rep) (verify gate) | 2/100 | Not Ready | Unknown |
| [kserve-migration](https://github.com/opendatahub-io/kserve-migration) (verify gate) | 2/100 | Not Ready | Unknown |
| [llm-d-playbooks](https://github.com/opendatahub-io/llm-d-playbooks) (verify gate) | 2/100 | Not Ready | Unknown |
| [odh-automation-serving](https://github.com/opendatahub-io/odh-automation-serving) (verify gate) | 2/100 | Not Ready | Unknown |
| [odh-doc-examples](https://github.com/opendatahub-io/odh-doc-examples) (verify gate) | 2/100 | Not Ready | Unknown |
| [odh-observability](https://github.com/opendatahub-io/odh-observability) (verify gate) | 2/100 | Not Ready | Unknown |
| [rhaii-cluster-validation](https://github.com/opendatahub-io/rhaii-cluster-validation) (verify gate) | 2/100 | Not Ready | Unknown |
| [sample-gam-trigger-workflow](https://github.com/opendatahub-io/sample-gam-trigger-workflow) (verify gate) | 2/100 | Not Ready | Unknown |
| [sdg-hub](https://github.com/opendatahub-io/sdg-hub) (verify gate) | 2/100 | Not Ready | Unknown |
| [test-repo](https://github.com/opendatahub-io/test-repo) (verify gate) | 2/100 | Not Ready | Unknown |

## Quick Wins (Highest Impact Actions)

| Action | Repos Below 40 | Weight | How to Fix |
|---|---|---|---|
| Bug Report Template Quality | 101 repos | 12% | Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs. |
| Test-to-Source Ratio | 61 repos | 17% | Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files. |
| One-Command Test Execution | 66 repos | 12% | Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies. |
| AI Context Files | 111 repos | 5% | Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md. |
| Coverage Configuration | 87 repos | 5% | Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration. |
| Structured Logging / Errors | 86 repos | 5% | Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context. |
| PR Template | 93 repos | 3% | Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist. |

## All Checks Ranked by Average Score

| Check | Avg Score | Weight |
|---|---|---|
| AI Context Files | 14/100 | 5% |
| Bug Report Template Quality | 20/100 | 12% |
| Coverage Configuration | 22/100 | 5% |
| PR Template | 23/100 | 3% |
| Code Ownership (CODEOWNERS) | 33/100 | 3% |
| One-Command Test Execution | 35/100 | 12% |
| Structured Logging / Errors | 36/100 | 5% |
| Test-to-Source Ratio | 41/100 | 17% |
| Linting / Formatting in CI | 42/100 | 5% |
| Contributing / Dev Guide | 44/100 | 5% |
| Test Isolation (unit vs e2e) | 55/100 | 5% |
| Code Navigability | 56/100 | 8% |
| CI Runs Tests on PRs | 57/100 | 10% |
| Generated Code Ratio | 95/100 | 5% |

## Per-Repository Details

### data-science-pipelines-operator -- 80/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (20/50 sampled files); Error wrapping patterns (11 files) |
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
| Test Isolation (unit vs e2e) | Verify | 5% | 85 | ~58% unit tests, ~42% infra-dependent (15/26 sampled); Makefile separates unit and integration test targets |

### feast -- 79/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (logr) found in go.mod; Go structured logging (zerolog) found in go.mod; Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 197 lines (1041 source files, generated excluded); Files >500 lines: 98 (9%); Largest: feature_store.py (3288L), ray.py (2370L), test_search_api.py (2290L) |
| Generated Code Ratio | Navigate | 5% | 100 | 2/1191 files are generated (0%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (CODEOWNERS) with 18 rules |
| Test-to-Source Ratio | Verify | 17% | 50 | 337 test files / 852 source files (ratio: 0.40) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, infra/feast-operator/test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 13 CI workflow(s): release.yml, pr_registration_integration_tests.yml, pr_local_integration_tests.yml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: linter.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (28/29 sampled) |

### kube-auth-proxy -- 78/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
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
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~72% unit tests, ~28% infra-dependent (21/29 sampled) |

### modelmesh-serving -- 78/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (18/50 sampled files); Error wrapping patterns (17 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 213 lines (84 source files, generated excluded); Files >500 lines: 7 (8%); Largest: predictor_test.go (1286L), fvtclient.go (1019L), servingruntime_controller.go (801L) |
| Generated Code Ratio | Navigate | 5% | 80 | 14/98 files are generated (14%); Examples: model-mesh-external_grpc.pb.go, model-mesh-external.pb.go, zz_generated.deepcopy.go, kfs_inference_v2.pb.go, predict.pb.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 31 test files / 53 source files (ratio: 0.58) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, e2e-test, tests/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, build.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml, build.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~77% unit tests, ~23% infra-dependent (23/30 sampled) |

### odh-dashboard -- 78/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (4/7 quality keywords); claude.md found (4/7 quality keywords); AGENTS.md found (4/7 quality keywords); Agents.md found (4/7 quality keywords); agents.md found (4/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (7 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 117 lines (5518 source files, generated excluded); Files >500 lines: 166 (3%); Largest: mockPipelineSpec.ts (5220L), modelServingDeploy.cy.ts (2747L), workbench.cy.ts (2568L) |
| Generated Code Ratio | Navigate | 5% | 100 | 46/5573 files are generated (1%); Examples: maas_models_mock.go, http_mock.go, token_k8s_client_mock.go, internal_k8s_client_mock.go, mock_factory.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 1072 test files / 4455 source files (ratio: 0.24) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: packages/maas/test; npm test script defined |
| Coverage Configuration | Verify | 5% | 60 | Codecov configured; Coverage in CI workflow: test.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test.yml, gen-ai-frontend-build.yml, maas-bff-tests.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: autorag-bff-tests.yml, gen-ai-bff-build.yml, maas-bff-tests.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~93% unit tests, ~7% infra-dependent (25/27 sampled) |

### eval-hub -- 78/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (6/7 quality keywords); claude.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has reproduction steps; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (17/50 sampled files); Error wrapping patterns (18 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 185 lines (121 source files, generated excluded); Files >500 lines: 11 (9%); Largest: step_definitions_test.go (2330L), step_definitions_test.go (1066L), local_runtime_test.go (840L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/121 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 36 test files / 85 source files (ratio: 0.42) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Codecov configured; Go coverage flags in Makefile; Coverage in CI workflow: ci.yml |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~87% unit tests, ~13% infra-dependent (26/30 sampled) |

### kserve -- 77/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (12 files) |
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
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |

### spark-operator -- 76/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (14/50 sampled files); Error wrapping patterns (14 files) |
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
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 95 | Found: .github/ISSUE_TEMPLATE/bug-report.yml; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Go structured logging (zerolog) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (9/50 sampled files); Error wrapping patterns (12 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 227 lines (346 source files, generated excluded); Files >500 lines: 38 (11%); Largest: raycluster_controller_unit_test.go (3811L), raycluster_controller.go (2053L), pod_test.go (1954L) |
| Generated Code Ratio | Navigate | 5% | 60 | 78/425 files are generated (18%); Examples: config_grpc.pb.go, job_submission.pb.gw.go, serve.pb.gw.go, config.pb.gw.go, cluster.pb.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 85 | 145 test files / 202 source files (ratio: 0.72) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: ray-operator/test, ray-operator/test, ray-operator/test, apiserver/test, apiserver/e2e-test, apiserversdk/test, apiserversdk/test, apiserversdk/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): odh-release.yml, image-release.yaml, e2e-tests.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: helm.yaml, test-job.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 50 | ~48% unit tests, ~52% infra-dependent (11/23 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### model-registry -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (6/50 sampled files); Error wrapping patterns (14 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 216 lines (1023 source files, generated excluded); Files >500 lines: 100 (10%); Largest: model_registry_service_api.py (15724L), artifact_test.go (3474L), model_catalog_service_api.py (2654L) |
| Generated Code Ratio | Navigate | 5% | 60 | 182/1207 files are generated (15%); Examples: static_data_mock.go, model_registry_client_mock.go, model_catalog_client_mock.go, http_mock.go, types_mock.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 279 test files / 746 source files (ratio: 0.37) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, clients/python/test, catalog/test, jobs/async-upload/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile; Coverage in CI workflow: python-tests.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): ui-frontend-build.yml, python-tests.yml, async-upload-test.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ui-bff-build.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |

### argo-workflows -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (6/50 sampled files); Error wrapping patterns (25 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 200 lines (1381 source files, generated excluded); Files >500 lines: 56 (4%); Largest: operator_test.go (11613L), operator.go (4259L), util_test.go (4178L) |
| Generated Code Ratio | Navigate | 5% | 80 | 81/1462 files are generated (6%); Examples: MockWriter.go, Gatekeeper.go, Interface.go, ContainerRuntimeExecutor.go, Interface.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 50 | 271 test files / 1110 source files (ratio: 0.24) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, sdks/python/test, sdks/java/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 60 | Codecov configured; Coverage-related target in Makefile; Coverage in CI workflow: ci-build.yaml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci-build.yaml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-build.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~92% unit tests, ~8% infra-dependent (24/26 sampled) |

### litellm -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords); AGENTS.md found (2/7 quality keywords); Agents.md found (2/7 quality keywords); agents.md found (2/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 65 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (10 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 282 lines (2128 source files, generated excluded); Files >500 lines: 285 (13%); Largest: proxy_server.py (9467L), utils.py (7739L), networking.tsx (7525L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/2149 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 826 test files / 1323 source files (ratio: 0.62) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test-litellm.yml, llm-translation-testing.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test-linting.yml, ghcr_helm_deploy.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 100 | ~97% unit tests, ~3% infra-dependent (29/30 sampled); Makefile separates unit and integration test targets |

### llm-d-inference-scheduler -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 70 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (21/50 sampled files); Error wrapping patterns (12 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 157 lines (72 source files, generated excluded); Files >500 lines: 4 (6%); Largest: e2e_test.go (937L), no_hit_lru_test.go (586L), precise_prefix_cache_test.go (578L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/72 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 32 test files / 40 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci-pr-checks.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-pr-checks.yaml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: DEVELOPMENT.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~89% unit tests, ~11% infra-dependent (24/27 sampled) |

### NeMo-Guardrails -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 5% | 90 | Python structured logging found in requirements.txt; Error wrapping patterns (4 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 224 lines (663 source files, generated excluded); Files >500 lines: 64 (10%); Largest: test_flow_mechanics.py (2429L), statemachine.py (2174L), config.py (2068L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/663 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 295 test files / 368 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test; pytest configured in pyproject.toml; tox.ini found; pytest configuration found |
| Coverage Configuration | Verify | 5% | 60 | Coverage-related target in Makefile; Coverage in CI workflow: _test.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): _test.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### data-science-pipelines -- 73/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | AGENTS.md found (6/7 quality keywords); Agents.md found (6/7 quality keywords); agents.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (8 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 208 lines (2185 source files, generated excluded); Files >500 lines: 174 (8%); Largest: pipeline_spec_pb.js (15776L), large-graph-runtime.ts (12660L), pipeline_spec.ts (10579L) |
| Generated Code Ratio | Navigate | 5% | 60 | 391/2600 files are generated (15%); Examples: kubernetes_executor_config.pb.go, protobuf_any.go, googlerpc_status.go, v2beta1_get_healthz_response.go, protobuf_any.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 620 test files / 1589 source files (ratio: 0.39) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: manifests/kustomize/test; pytest configuration found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 12 CI workflow(s): kfp-sdk-client-tests.yml, legacy-v2-api-integration-tests.yml, integration-tests-v1.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml, sdk-isort.yml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (29/29 sampled) |

### workload-variant-autoscaler -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (0/7 quality keywords); claude.md found (0/7 quality keywords); AGENTS.md found (6/7 quality keywords); Agents.md found (6/7 quality keywords); agents.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (19/50 sampled files); Error wrapping patterns (13 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 272 lines (172 source files, generated excluded); Files >500 lines: 28 (16%); Largest: greedy_test.go (1696L), system_test.go (1675L), e2eutils.go (1247L) |
| Generated Code Ratio | Navigate | 5% | 100 | 1/173 files are generated (1%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 74 test files / 98 source files (ratio: 0.76) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): ci-pr-checks.yaml, ci-e2e-openshift.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-pr-checks.yaml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~83% unit tests, ~17% infra-dependent (25/30 sampled) |

### opendatahub-tests -- 71/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | AGENTS.md found (4/7 quality keywords); Agents.md found (4/7 quality keywords); agents.md found (4/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 65 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (9 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 162 lines (342 source files, generated excluded); Files >500 lines: 23 (7%); Largest: infra.py (1198L), conftest.py (971L), utils.py (961L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/410 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 6 rules |
| Test-to-Source Ratio | Verify | 17% | 100 | 248 test files / 162 source files (ratio: 1.53) |
| One-Command Test Execution | Verify | 12% | 60 | tox.ini found; pytest configuration found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): tox-tests.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: docs/CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |

### model-registry-bf4-kf -- 70/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (8/50 sampled files); Error wrapping patterns (11 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 248 lines (56 source files, generated excluded); Files >500 lines: 7 (12%); Largest: core_test.go (3381L), core.go (1466L), api_model_registry_service.go (952L) |
| Generated Code Ratio | Navigate | 5% | 20 | 63/119 files are generated (53%); Examples: openapi_converter.gen.go, mlmd_openapi_converter.gen.go, openapi_mlmd_converter.gen.go, metadata_store.pb.go, metadata_store_service.pb.go *Rec: Add '// Code generated' headers to generated files and document which files are auto-generated in CLAUDE.md.* |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 16 test files / 40 source files (ratio: 0.40) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile; Coverage in CI workflow: python-tests.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): python-tests.yml, build.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~94% unit tests, ~6% infra-dependent (15/16 sampled) |

### models-as-a-service -- 70/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Good logging coverage (22/50 sampled files); Error wrapping patterns (23 files) |
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
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~93% unit tests, ~7% infra-dependent (26/28 sampled) |

### opendatahub-operator -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Found .github/ISSUE_TEMPLATE/bug_report.md but name/about fields don't indicate a bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (10/50 sampled files); Error wrapping patterns (15 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 207 lines (535 source files, generated excluded); Files >500 lines: 54 (10%); Largest: mutating_test.go (2768L), monitoring_test.go (2278L), test_context_test.go (2099L) |
| Generated Code Ratio | Navigate | 5% | 100 | 15/550 files are generated (3%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 186 test files / 349 source files (ratio: 0.53) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, unit-test, e2e-test, e2e-test, unit-test-cli; Multiple test types available |
| Coverage Configuration | Verify | 5% | 70 | Codecov configured; Go coverage flags in Makefile; Coverage in CI workflow: security-full-scan.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): test-gateway-integration.yaml, test-unit.yaml, test-unit-cli.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: security-full-scan.yml, test-linter.yaml |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~50% unit tests, ~50% infra-dependent (13/26 sampled) |

### notebooks -- 69/100 (Partially Ready)

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
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pr-merge-image-delete.yml, auto-add-issue-to-project.yml, sec-scan.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~67% unit tests, ~33% infra-dependent (2/3 sampled) |

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
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~96% unit tests, ~4% infra-dependent (22/23 sampled) |

### model-registry-operator -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (16/38 sampled files); Error wrapping patterns (15 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 316 lines (38 source files, generated excluded); Files >500 lines: 6 (16%); Largest: modelcatalog_controller_test.go (1436L), modelregistry_controller_test.go (1332L), modelcatalog_controller.go (1293L) |
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

### training-operator -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (7/50 sampled files); Error wrapping patterns (13 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 187 lines (254 source files, generated excluded); Files >500 lines: 18 (7%); Largest: training_client_test.py (1995L), training_client.py (1558L), mpijob_controller.go (1400L) |
| Generated Code Ratio | Navigate | 5% | 60 | 69/326 files are generated (21%); Examples: zz_generated.defaults.go, openapi_generated.go, zz_generated.deepcopy.go, factory.go, generic.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 67 test files / 190 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): unittests.yaml, test-python.yaml, integration-tests.yaml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test-go.yaml, pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~83% unit tests, ~17% infra-dependent (24/29 sampled) |

### llama-stack-k8s-operator -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
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

### trustyai-explainability -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 146 lines (707 source files, generated excluded); Files >500 lines: 30 (4%); Largest: ModelInferRequest.java (5632L), ModelInferResponse.java (4037L), ModelMetadataResponse.java (3177L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/708 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 70 | 237 test files / 471 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: tests/test; Maven build found (mvn test) |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yaml |
| PR Template | Submit | 3% | 55 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |

### caikit-nlp -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (6/50 sampled files); Error wrapping patterns (9 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 241 lines (66 source files, generated excluded); Files >500 lines: 9 (14%); Largest: peft_prompt_tuning.py (1241L), embedding.py (1226L), test_embedding.py (1145L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/74 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 70 | 27 test files / 47 source files (ratio: 0.57) |
| One-Command Test Execution | Verify | 12% | 60 | tox.ini found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): publish-library.yml, build-library.yml, lint-code.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (27/27 sampled) |

### base-containers -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 127 lines (5 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/5 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 100 | 4 test files / 1 source files (ratio: 4.00) |
| One-Command Test Execution | Verify | 12% | 60 | tox.ini found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: docs/development.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (4/4 sampled) |

### trainer -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (6 files) |
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
| Test Isolation (unit vs e2e) | Verify | 5% | 100 | ~89% unit tests, ~11% infra-dependent (25/28 sampled); Makefile separates unit and integration test targets |

### trainer-sdk -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 120 lines (470 source files, generated excluded); Files >500 lines: 9 (2%); Largest: torch_test.go (1350L), wrapper.go (1191L), framework_test.go (1176L) |
| Generated Code Ratio | Navigate | 5% | 80 | 32/509 files are generated (6%); Examples: zz_generated.openapi.go, zz_generated.defaults.go, zz_generated.deepcopy.go, factory.go, generic.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 25 | 45 test files / 432 source files (ratio: 0.10) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test-go.yaml, test-e2e.yaml, test-python.yaml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test-go.yaml, test-python.yaml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~85% unit tests, ~15% infra-dependent (22/26 sampled) |

### kubeflow -- 65/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
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
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (19/50 sampled files); Error wrapping patterns (11 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 205 lines (126 source files, generated excluded); Files >500 lines: 10 (8%); Largest: configmap_handler_test.go (999L), inferenceservice_controller_test.go (947L), llm_inferenceservice_controller_test.go (941L) |
| Generated Code Ratio | Navigate | 5% | 100 | 1/127 files are generated (1%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 42 test files / 84 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, test-e2e.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started, Develop, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~73% unit tests, ~27% infra-dependent (22/30 sampled) |

### training-notebooks -- 64/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (15 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 250 lines (75 source files, generated excluded); Files >500 lines: 16 (21%); Largest: konflux_generate_component_build_pipelines.py (863L), bootstrapper.py (769L), bootstrapper.py (769L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/78 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 28 test files / 50 source files (ratio: 0.56) |
| One-Command Test Execution | Verify | 12% | 60 | pytest configuration found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): build-notebooks-TEMPLATE.yaml, code-quality.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pr-merge-image-delete.yml, auto-add-issue-to-project.yml, sec-scan.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~82% unit tests, ~18% infra-dependent (23/28 sampled) |

### rhoai-mcp -- 63/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (7/7 quality keywords); claude.md found (7/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (4 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 190 lines (168 source files, generated excluded); Files >500 lines: 13 (8%); Largest: tools.py (1147L), test_tools.py (1048L), tools.py (1021L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/174 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 70 | 56 test files / 118 source files (ratio: 0.47) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test; pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: ci.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): ci.yml, eval.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### odh-cli -- 63/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 64 | CLAUDE.md found (1/7 quality keywords); claude.md found (1/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (21 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 187 lines (239 source files, generated excluded); Files >500 lines: 12 (5%); Largest: impacted.go (1463L), impacted_test.go (1328L), impacted_test.go (1058L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/239 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 70 | 85 test files / 154 source files (ratio: 0.55) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: docs/development.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~77% unit tests, ~23% infra-dependent (23/30 sampled) |

### model-metadata-collection -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (6/7 quality keywords); claude.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (7/28 sampled files); Error wrapping patterns (12 files) |
| Code Navigability | Navigate | 8% | 50 | Average file: 392 lines (28 source files, generated excluded); Files >500 lines: 8 (29%); Largest: catalog_test.go (1396L), main.go (853L), registry_test.go (848L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/28 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 11 test files / 17 source files (ratio: 0.65) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build-and-push-static-model-catalog-data.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Build, Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~91% unit tests, ~9% infra-dependent (10/11 sampled) |

### modelmesh-runtime-adapter -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (33/50 sampled files); Error wrapping patterns (21 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 175 lines (78 source files, generated excluded); Files >500 lines: 6 (8%); Largest: adaptmodellayout_test.go (1246L), adaptmodellayout_test.go (652L), puller_test.go (637L) |
| Generated Code Ratio | Navigate | 5% | 60 | 26/104 files are generated (25%); Examples: model_runtime_client_mock.go, pullman_mock.go, mock_inference.go, mock_management.go, mock_torchserve_server.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 27 test files / 51 source files (ratio: 0.53) |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, model-serving-puller/test, model-mesh-mlserver-adapter/test, model-mesh-triton-adapter/test, model-mesh-ovms-adapter/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 3% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (29/29 sampled) |

### kube-authkit -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (8 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 280 lines (26 source files, generated excluded); Files >500 lines: 3 (12%); Largest: test_oidc.py (1181L), oidc.py (643L), test_factory.py (518L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/26 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 100 | 14 test files / 12 source files (ratio: 1.17) |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: test.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): publish.yml, test.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~71% unit tests, ~29% infra-dependent (10/14 sampled) |

### mlflow -- 61/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (6) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (5 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 322 lines (4160 source files, generated excluded); Files >500 lines: 409 (10%); Largest: Service.java (274253L), ModelRegistry.java (53284L), DatabricksArtifacts.java (23030L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/4351 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 1417 test files / 2934 source files (ratio: 0.48) |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 13 CI workflow(s): typescript.yml, lint.yml, uc-oss.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml, docs.yml, copilot-setup-steps.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### mcp-server-operator -- 61/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (3/13 sampled files); Error wrapping patterns (2 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 227 lines (13 source files, generated excluded); Files >500 lines: 1 (8%); Largest: mcpserver_test.go (1132L) |
| Generated Code Ratio | Navigate | 5% | 80 | 1/14 files are generated (7%); Examples: zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 5 test files / 8 source files (ratio: 0.62) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~75% unit tests, ~25% infra-dependent (3/4 sampled) |

### llm-d-kv-cache -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (16/50 sampled files); Error wrapping patterns (13 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 181 lines (107 source files, generated excluded); Files >500 lines: 4 (4%); Largest: e2e_test.go (915L), cgo_functions_test.go (810L), cgo_functions.c (591L) |
| Generated Code Ratio | Navigate | 5% | 100 | 4/111 files are generated (4%); Examples: tokenizer_grpc.pb.go, tokenizer.pb.go, indexer_grpc.pb.go, indexer.pb.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (CODEOWNERS) with 4 rules |
| Test-to-Source Ratio | Verify | 17% | 50 | 28 test files / 79 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, unit-test, e2e-test, kv_connectors/llmd_fs_backend/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci-pr-checks.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-pr-checks.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~92% unit tests, ~8% infra-dependent (24/26 sampled) |

### MLServer -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (2 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 111 lines (335 source files, generated excluded); Files >500 lines: 6 (2%); Largest: generate-pinned-requirements.py (1053L), test_pandas.py (744L), test_base.py (673L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/362 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 143 test files / 219 source files (ratio: 0.65) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test; pytest configured in pyproject.toml; tox.ini found; pytest configuration found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): tests.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: tests.yml |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### llama-stack -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (5) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (15 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 157 lines (1049 source files, generated excluded); Files >500 lines: 63 (6%); Largest: test_openai_vector_stores.py (5523L), ifeval_utils.py (3319L), test_openai_responses.py (3184L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/1049 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 50 | 238 test files / 811 source files (ratio: 0.29) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Python coverage config; Coverage in CI workflow: codeql.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 7 CI workflow(s): release-branch-scheduled-ci.yml, record-integration-tests.yml, integration-vector-io-tests.yml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (26/26 sampled) |

### caikit-nlp-client -- 59/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (2/19 sampled files); Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 151 lines (18 source files, generated excluded); Files >500 lines: 1 (6%); Largest: http_client.py (541L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/19 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 9 test files / 10 source files (ratio: 0.90) |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml; noxfile.py found |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: tests-docker.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): release.yml, tests-docker.yml, tests.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: tests.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (9/9 sampled) |

### rest-proxy -- 59/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (5/6 sampled files); Error wrapping patterns (3 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 208 lines (6 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 40 | 3/9 files are generated (33%); Examples: grpc_predict_v2.pb.gw.go, grpc_predict_v2_grpc.pb.go, grpc_predict_v2.pb.go *Rec: Add '// Code generated' headers to generated files and document which files are auto-generated in CLAUDE.md.* |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 2 test files / 4 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |

### trustyai-service-operator -- 59/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (13/50 sampled files); Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 242 lines (131 source files, generated excluded); Files >500 lines: 15 (11%); Largest: lmevaljob_controller_test.go (4373L), lmevaljob_controller_validation_test.go (1798L), unit_test.go (1680L) |
| Generated Code Ratio | Navigate | 5% | 100 | 6/137 files are generated (4%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 33 test files / 98 source files (ratio: 0.34) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 80 | Makefile targets: test, tests/test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): controller-tests.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint-yaml.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~70% unit tests, ~30% infra-dependent (21/30 sampled) |

### elyra -- 57/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (3) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (7/50 sampled files); Error wrapping patterns (7 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 213 lines (255 source files, generated excluded); Files >500 lines: 29 (11%); Largest: test_processor_kfp.py (1883L), test_metadata_app.py (1785L), test_pipeline_app.py (1401L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/268 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 71 test files / 197 source files (ratio: 0.36) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test; npm test script defined; pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Coverage-related target in Makefile; Coverage in CI workflow: build.yml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: build.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### mod-arch-library -- 56/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (0/7 quality keywords); claude.md found (0/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 64 lines (303 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 4/308 files are generated (1%); Examples: http_mock.go, token_k8s_client_mock.go, internal_k8s_client_mock.go, mock_factory.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 47 test files / 257 source files (ratio: 0.18) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: mod-arch-starter/bff/test; npm test script defined |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: test.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): release.yml, publish.yml, test.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~93% unit tests, ~7% infra-dependent (28/30 sampled) |

### codeflare-operator -- 55/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (4/18 sampled files); Error wrapping patterns (2 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 262 lines (18 source files, generated excluded); Files >500 lines: 3 (17%); Largest: raycluster_webhook_test.go (880L), raycluster_controller.go (713L), mnist_rayjob_raycluster_test.go (559L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/18 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 8 test files / 10 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): unit_tests.yml, odh-release.yml, component_tests.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: precommit.yml, unit_tests.yml, tag-and-build.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 30 | ~14% unit tests, ~86% infra-dependent (1/7 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### kubeflow-sdk -- 55/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (19 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 30 | Average file: 346 lines (66 source files, generated excluded); Files >500 lines: 17 (26%); Largest: transformers_test.py (3647L), transformers.py (1739L), backend_test.py (1413L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/73 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 13 test files / 60 source files (ratio: 0.22) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile; Coverage in CI workflow: test-python.yaml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test-e2e.yaml, test-python.yaml, odh-release.yaml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (13/13 sampled) |

### vllm-tgis-adapter -- 54/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (13 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 146 lines (30 source files, generated excluded); Files >500 lines: 1 (3%); Largest: grpc_server.py (994L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/32 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 8 test files / 24 source files (ratio: 0.33) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml; noxfile.py found |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: tests.yaml; Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): tests.yaml, release.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit-autoupdate.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (8/8 sampled) |

### codeflare-operator-poc -- 54/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (4/18 sampled files); Error wrapping patterns (2 files) |
| Code Navigability | Navigate | 8% | 50 | Average file: 264 lines (18 source files, generated excluded); Files >500 lines: 4 (22%); Largest: raycluster_webhook_test.go (880L), raycluster_controller.go (713L), mnist_rayjob_raycluster_test.go (559L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/18 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 8 test files / 10 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): unit_tests.yml, odh-release.yml, component_tests.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: precommit.yml, unit_tests.yml, tag-and-build.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 30 | ~14% unit tests, ~86% infra-dependent (1/7 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### openvino_model_server -- 51/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (4 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 277 lines (582 source files, generated excluded); Files >500 lines: 72 (12%); Largest: ensemble_tests.cpp (6409L), ensemble_flow_custom_node_tests.cpp (5967L), llmnode_test.cpp (4131L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/582 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 70 | 214 test files / 368 source files (ratio: 0.58) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 50 | Coverage-related target in Makefile *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): integration-tests-konflux.yml, integration-tests.yml, fast-checks.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: docs/CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### kueue -- 51/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 70 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (9/50 sampled files); Error wrapping patterns (11 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 300 lines (614 source files, generated excluded); Files >500 lines: 88 (14%); Largest: scheduler_test.go (7541L), pod_controller_test.go (5833L), cache_test.go (3920L) |
| Generated Code Ratio | Navigate | 5% | 80 | 88/702 files are generated (13%); Examples: zz_generated.openapi.go, zz_generated.defaults.go, zz_generated.conversion.go, zz_generated.deepcopy.go, zz_generated.defaults.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 238 test files / 376 source files (ratio: 0.63) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 60 | CI runs tests (but may not trigger on PRs); Tests found in 1 CI workflow(s): odh-release.yml |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~50% unit tests, ~50% infra-dependent (13/26 sampled) |

### elyra-pipeline-editor -- 50/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 220 lines (102 source files, generated excluded); Files >500 lines: 7 (7%); Largest: index.ts (5335L), common-canvas.d.ts (3011L), index.test.ts (1395L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/102 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 22 test files / 80 source files (ratio: 0.28) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | npm test script defined |
| Coverage Configuration | Verify | 5% | 60 | Coverage in CI workflow: build.yaml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (22/22 sampled) |

### batch-gateway -- 50/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (21/50 sampled files); Error wrapping patterns (19 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 186 lines (57 source files, generated excluded); Files >500 lines: 3 (5%); Largest: client_test.go (1103L), file_handler_test.go (701L), file_handler.go (653L) |
| Generated Code Ratio | Navigate | 5% | 80 | 5/62 files are generated (8%); Examples: mock_event_client.go, mock_status_client.go, mock_db_client.go, mock_queue_client.go, mock_files_client.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 12 test files / 45 source files (ratio: 0.27) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: test |
| Coverage Configuration | Verify | 5% | 70 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~92% unit tests, ~8% infra-dependent (11/12 sampled) |

### guardrails-detectors -- 50/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 154 lines (29 source files, generated excluded); Files >500 lines: 1 (3%); Largest: test_llm_judge_detector.py (588L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/34 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 15 test files / 19 source files (ratio: 0.79) |
| One-Command Test Execution | Verify | 12% | 60 | tox.ini found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test-llm-judge.yaml, test-huggingface-runtime.yaml, test-builtin-detectors.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (15/15 sampled) |

### vllm-gaudi -- 50/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (10) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (16 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 263 lines (909 source files, generated excluded); Files >500 lines: 130 (14%); Largest: config.py (2413L), hpu_model_runner.py (2213L), llm_engine.py (2091L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/991 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 70 | 341 test files / 650 source files (ratio: 0.52) |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ruff.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### llama-stack-provider-ragas -- 48/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (4 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 105 lines (22 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/24 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 4 test files / 20 source files (ratio: 0.20) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (4/4 sampled) |

### elyra-examples -- 47/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Good logging coverage (14/46 sampled files); Error wrapping patterns (8 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 85 lines (46 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/46 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 3 test files / 43 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: component-catalog-connectors/artifactory-connector/test, component-catalog-connectors/kfp-example-components-connector/test, component-catalog-connectors/mlx-connector/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: build.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (3/3 sampled) |

### openvino_contrib -- 47/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 117 lines (423 source files, generated excluded); Files >500 lines: 8 (2%); Largest: convolution.cpp (8897L), group_convolution.cpp (822L), bidirectional_lstm_sequence_composition.cpp (755L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/425 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 7 rules |
| Test-to-Source Ratio | Verify | 17% | 50 | 107 test files / 318 source files (ratio: 0.34) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): windows.yml, token_merging.yml, linux.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: openvino_code.yml |
| Contributing / Dev Guide | Submit | 5% | 60 | Found: CONTRIBUTING.md; 1/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### fms-guardrails-orchestrator -- 47/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 30 | Average file: 486 lines (74 source files, generated excluded); Files >500 lines: 16 (22%); Largest: chat_completions_streaming.rs (5653L), completions_streaming.rs (4701L), streaming_classification_with_gen.rs (1833L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/74 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 50 | 19 test files / 55 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (19/19 sampled) |

### odh-ide-extensions -- 46/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 27 lines (23 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/23 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 50 | 6 test files / 17 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 70 | npm test script defined |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): build_extension.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop, Getting Started, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (6/6 sampled) |

### distributed-workloads -- 45/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (4 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 167 lines (116 source files, generated excluded); Files >500 lines: 7 (6%); Largest: rhai_features_tests.go (1059L), prestage_models_datasets.py (852L), ray_finetune_llm_deepspeed.py (743L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/116 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 100 | 95 test files / 21 source files (ratio: 4.52) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): odh-release.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~53% unit tests, ~47% infra-dependent (16/30 sampled) |

### llama-stack-provider-trustyai-garak -- 45/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 218 lines (28 source files, generated excluded); Files >500 lines: 3 (11%); Largest: test_remote_provider.py (853L), base_eval.py (684L), garak_eval.py (505L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/29 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 6 test files / 23 source files (ratio: 0.26) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 60 | Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): run-tests.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (6/6 sampled) |

### mlflow-go -- 44/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 100 | Good logging coverage (11/25 sampled files); Error wrapping patterns (6 files) |
| Code Navigability | Navigate | 8% | 50 | Average file: 342 lines (25 source files, generated excluded); Files >500 lines: 7 (28%); Largest: client_test.go (1175L), client_test.go (1148L), client.go (767L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 60 | 6/31 files are generated (19%); Examples: databricks.pb.go, model_registry.pb.go, service.pb.go, assessments.pb.go, datasets.pb.go |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 70 | 9 test files / 16 source files (ratio: 0.56) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): go.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: go.yaml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~86% unit tests, ~14% infra-dependent (6/7 sampled) |

### lm-evaluation-harness -- 44/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (9 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 155 lines (244 source files, generated excluded); Files >500 lines: 18 (7%); Largest: task.py (1721L), instructions_util.py (1696L), instructions_util.py (1696L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/250 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 25 | 17 test files / 233 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 60 | Python coverage config |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): unit_tests.yml, new_tasks.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: unit_tests.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: docs/CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (17/17 sampled) |

### modelmesh -- 44/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 451 lines (117 source files, generated excluded); Files >500 lines: 23 (20%); Largest: ModelMesh.java (7365L), LegacyModelMeshService.java (5330L), TasRuntimeOuterClass.java (4876L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/117 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 85 | 52 test files / 65 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 12% | 60 | Maven build found (mvn test) |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~93% unit tests, ~7% infra-dependent (28/30 sampled) |

### modelcar-base-image -- 44/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 27 lines (7 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/8 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 85 | 3 test files / 5 source files (ratio: 0.60) |
| One-Command Test Execution | Verify | 12% | 70 | Makefile targets: python/test |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (3/3 sampled) |

### data-processing -- 43/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (8 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 156 lines (19 source files, generated excluded); Files >500 lines: 1 (5%); Largest: subset_selection.py (931L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/19 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 2 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 25 | 2 test files / 17 source files (ratio: 0.12) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): validate-notebooks.yml, execute-all-notebooks.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: validate-python.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |

### llama-stack-provider-kfp-trainer -- 39/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 103 lines (10 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/10 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 1 test files / 9 source files (ratio: 0.11) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | tox.ini found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): lint.yml, test.yml, mypy.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (1/1 sampled) |

### llama-stack-client-python -- 38/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (5 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 149 lines (421 source files, generated excluded); Files >500 lines: 31 (7%); Largest: _base_client.py (1999L), test_client.py (1692L), response_object_stream.py (1550L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/422 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 25 | 67 test files / 355 source files (ratio: 0.19) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |

### perf_analyzer -- 35/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 94 lines (763 source files, generated excluded); Files >500 lines: 17 (2%); Largest: doctest.h (7824L), test_llm_profile_data_parser.py (1587L), test_cli.py (1579L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/764 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 69 test files / 695 source files (ratio: 0.10) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): python-package-genai.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |

### fips-compliance-checker-claude-code-plugin -- 34/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 88 | CLAUDE.md found (2/7 quality keywords); claude.md found (2/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 42 lines (7 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/7 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 100 | 6 test files / 1 source files (ratio: 6.00) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Build, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (6/6 sampled) |

### caikit-tgis-serving -- 32/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 48 lines (2 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/2 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 100 | 1 test files / 1 source files (ratio: 1.00) |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 30 | ~0% unit tests, ~100% infra-dependent (0/1 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### openvino_tokenizers -- 31/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (7 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 225 lines (54 source files, generated excluded); Files >500 lines: 7 (13%); Largest: tokenizer_pipeline.py (1623L), tokenizers_test.py (1114L), hf_parser.py (1088L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/55 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 6 test files / 49 source files (ratio: 0.12) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): windows.yml, linux.yml, mac.yml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (6/6 sampled) |

### odh-s2i-project-cds -- 26/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 50 lines (7 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/15 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 1 test files / 14 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 60 | tox.ini found |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (1/1 sampled) |

### rag -- 25/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (10 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 232 lines (37 source files, generated excluded); Files >500 lines: 3 (8%); Largest: client.go (1581L), evaluation_utilities.py (900L), beir_benchmarks.py (619L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/37 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 25 | 2 test files / 35 source files (ratio: 0.06) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |

### llama-stack-demos -- 24/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (10 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 149 lines (58 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/60 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 10 test files / 50 source files (ratio: 0.20) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 70 | ~50% unit tests, ~50% infra-dependent (5/10 sampled) |

### openvino.genai -- 22/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 126 lines (11 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/11 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 25 rules |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 11 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): windows.yml, manylinux_2_28.yml, sdl.yml |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml, sdl.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### ml-metadata -- 22/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (9 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 30 | Average file: 346 lines (61 source files, generated excluded); Files >500 lines: 14 (23%); Largest: metadata_store_test.py (2631L), metadata_store.py (2012L), types.py (1578L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/61 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 13 test files / 48 source files (ratio: 0.27) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (13/13 sampled) |

### openvino -- 21/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (7) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (3/28 sampled files); Error wrapping patterns (6 files) |
| Code Navigability | Navigate | 8% | 90 | Average file: 131 lines (35 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/38 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 91 rules |
| Test-to-Source Ratio | Verify | 17% | 25 | 5 test files / 33 source files (ratio: 0.15) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (5/5 sampled) |

### llama-stack-distribution -- 20/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 294 lines (2 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/2 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 3 rules |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 2 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): redhat-distro-container.yml |
| PR Template | Submit | 3% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### rhaii-on-xks -- 20/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 479 lines (1 source files, generated excluded); Files >500 lines: 0 (0%) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/1 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 1 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 90 | Makefile targets: test, charts/cert-manager-operator/test, charts/sail-operator/test, charts/lws-operator/test; Multiple test types available |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: kserve-update-chart.yaml, kserve-ci.yaml, kserve-release.yaml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### client -- 19/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 210 lines (106 source files, generated excluded); Files >500 lines: 9 (8%); Largest: _client.py (1936L), _client.py (1659L), __init__.py (810L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/106 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 10 | 5 test files / 101 source files (ratio: 0.05) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: contribut, CONTRIBUT, Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (5/5 sampled) |

### odh-s2i-project-cookiecutter -- 18/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 40 lines (5 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/5 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 50 | 1 test files / 4 source files (ratio: 0.25) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 90 | ~100% unit tests, ~0% infra-dependent (1/1 sampled) |

### ai-helpers -- 14/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (3/7 quality keywords); claude.md found (3/7 quality keywords); AGENTS.md found (3/7 quality keywords); Agents.md found (3/7 quality keywords); agents.md found (3/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 15 | Issue templates exist (7) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (5 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 336 lines (14 source files, generated excluded); Files >500 lines: 2 (14%); Largest: compare_reqs.py (523L), env_finder.py (515L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/14 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 14 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Setup *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### vllm-orchestrator-gateway -- 13/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 50 | Average file: 298 lines (3 source files, generated excluded); Files >500 lines: 1 (33%); Largest: main.rs (547L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | 0/3 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 3 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): tests.yaml |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### agents -- 12/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 70 | Some logging (4/37 sampled files); Error wrapping patterns (10 files) |
| Code Navigability | Navigate | 8% | 70 | Average file: 152 lines (36 source files, generated excluded); Files >500 lines: 1 (3%); Largest: nps_mcp_server.py (757L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/37 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 25 | 3 test files / 34 source files (ratio: 0.09) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 50 | ~33% unit tests, ~67% infra-dependent (1/3 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### llama-stack-provider-instructlab-train -- 10/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 56 lines (4 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/4 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 4 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### llama-stack-provider-kft -- 10/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 94 lines (8 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/9 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 9 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-gitops -- 9/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
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

### opendatahub.io -- 9/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 97 lines (45 source files, generated excluded); Files >500 lines: 1 (2%); Largest: const.ts (845L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/45 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 45 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### opendatahub-community -- 8/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
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

### opendatahub-documentation -- 6/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-konflux-central -- 6/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: yaml-lint.yaml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-s2i-project-simple -- 6/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 15 lines (3 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/3 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 3 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### model-runtimes-agent -- 5/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 20 | Error wrapping patterns (2 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 70 | Average file: 274 lines (13 source files, generated excluded); Files >500 lines: 2 (15%); Largest: app.py (1245L), accelerator_validator.py (566L) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/17 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 17 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### dsp-dev-tools -- 5/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 45 lines (14 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/14 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 14 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### guardrails-regex-detector -- 5/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 106 lines (2 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/2 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 2 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-build-metadata -- 5/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 90 | Average file: 102 lines (7816 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 5% | 100 | 0/7816 files are generated (0%) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | 0 test files / 7816 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### ODH-Build-Config -- 5/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### architecture-decision-records -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 12 rules |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### community-operators-prod -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### opendatahub.io-redirects -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### openvino-repo-syncher -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### kserve-raw-migration -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-template-sig -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### runbooks -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### security-config -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### sig-ml-developer-experience -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### sig-platform -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### workload-orchestration -- 3/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 60 | OWNERS file found (Kubernetes-style) |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### .github -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### aaet-devtools -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### ai-engineering-process-docs -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### coderabbit -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### feast-demo -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### feast-labs -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### guides-vllm-llm-d -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### kc-rep -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### kserve-migration -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### llm-d-playbooks -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-automation-serving -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-doc-examples -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### odh-observability -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### rhaii-cluster-validation -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### sample-gam-trigger-workflow -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 5% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.* |
| Code Navigability | Navigate | 8% | 0 | No source files found (config-only repo?) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 5% | 100 | No source files (not applicable) |
| Code Ownership (CODEOWNERS) | Submit | 3% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 17% | 0 | No source files found (config-only repo?) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 12% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 5% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | CI exists but no PR trigger or test steps found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 3% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### sdg-hub -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

### test-repo -- 2/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 5% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 12% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
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
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 5% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |

---
*AI Bug Automation Readiness Report -- Generated 2026-03-09 16:38*
