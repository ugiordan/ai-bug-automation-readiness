# AI Bug Automation Readiness Report

*102 repositories assessed -- 2026-03-17 16:37*

> 48 of 102 repositories are partially ready or above for AI-assisted bug fixing. The ecosystem averages 51/100. The biggest gap is "AI Context Files" (avg 21/100).

## How Scoring Works

**Overall score** = weighted average of 20 checks, each scored 0-100.

**Phases**: Understand (24%), Navigate (17%), Verify (46%), Submit (13%).

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
| Average Score | 51/100 |
| Ready (80+) | 4 |
| Partially Ready (60-79) | 44 |
| Needs Work (40-59) | 25 |
| Not Ready (<40) | 29 |

## Phase Scores (Ecosystem Average)

| Phase | Weight | Average |
|---|---|---|
| Understand | 24% | 32/100 |
| Navigate | 17% | 72/100 |
| Verify | 46% | 58/100 |
| Submit | 13% | 50/100 |

## Bug Bash Shortlist

### Ready (80+) -- 4 repos

- [odh-dashboard](https://github.com/opendatahub-io/odh-dashboard) (86)
- [litellm](https://github.com/opendatahub-io/litellm) (82)
- [data-science-pipelines](https://github.com/opendatahub-io/data-science-pipelines) (81)
- [feast](https://github.com/opendatahub-io/feast) (80)

### Partially Ready (60-79) -- 44 repos

- [eval-hub](https://github.com/opendatahub-io/eval-hub) (78) -- top gap: CI Runs Tests on PRs
- [notebooks](https://github.com/opendatahub-io/notebooks) (76) -- top gap: Test-to-Source Ratio
- [opendatahub-tests](https://github.com/opendatahub-io/opendatahub-tests) (76) -- top gap: Linting / Formatting in CI
- [data-science-pipelines-operator](https://github.com/opendatahub-io/data-science-pipelines-operator) (75) -- top gap: AI Context Files
- [workload-variant-autoscaler](https://github.com/opendatahub-io/workload-variant-autoscaler) (75) -- top gap: Bug Report Template Quality
- [model-registry](https://github.com/opendatahub-io/model-registry) (75) -- top gap: AI Context Files
- [modelmesh-serving](https://github.com/opendatahub-io/modelmesh-serving) (74) -- top gap: AI Context Files
- [kuberay](https://github.com/opendatahub-io/kuberay) (74) -- top gap: AI Context Files
- [NeMo-Guardrails](https://github.com/opendatahub-io/NeMo-Guardrails) (73) -- top gap: AI Context Files
- [kube-auth-proxy](https://github.com/opendatahub-io/kube-auth-proxy) (73) -- top gap: AI Context Files
- [kserve](https://github.com/opendatahub-io/kserve) (73) -- top gap: AI Context Files
- [argo-workflows](https://github.com/opendatahub-io/argo-workflows) (72) -- top gap: AI Context Files
- [llm-d-inference-scheduler](https://github.com/opendatahub-io/llm-d-inference-scheduler) (72) -- top gap: AI Context Files
- [rhoai-mcp](https://github.com/opendatahub-io/rhoai-mcp) (72) -- top gap: Bug Report Template Quality
- [mlflow-operator](https://github.com/opendatahub-io/mlflow-operator) (71) -- top gap: Bug Report Template Quality
- [training-operator](https://github.com/opendatahub-io/training-operator) (71) -- top gap: AI Context Files
- [semantic-router](https://github.com/opendatahub-io/semantic-router) (70) -- top gap: Test-to-Source Ratio
- [spark-operator](https://github.com/opendatahub-io/spark-operator) (70) -- top gap: AI Context Files
- [mod-arch-library](https://github.com/opendatahub-io/mod-arch-library) (69) -- top gap: Bug Report Template Quality
- [opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) (69) -- top gap: AI Context Files
- [mlflow](https://github.com/opendatahub-io/mlflow) (69) -- top gap: Bug Report Template Quality
- [trainer](https://github.com/opendatahub-io/trainer) (69) -- top gap: Test-to-Source Ratio
- [trainer-sdk](https://github.com/opendatahub-io/trainer-sdk) (68) -- top gap: Test-to-Source Ratio
- [kubeflow-sdk](https://github.com/opendatahub-io/kubeflow-sdk) (68) -- top gap: Test-to-Source Ratio
- [odh-cli](https://github.com/opendatahub-io/odh-cli) (68) -- top gap: Bug Report Template Quality
- [rhaii-cluster-validation](https://github.com/opendatahub-io/rhaii-cluster-validation) (68) -- top gap: Bug Report Template Quality
- [model-registry-bf4-kf](https://github.com/opendatahub-io/model-registry-bf4-kf) (68) -- top gap: AI Context Files
- [llama-stack-k8s-operator](https://github.com/opendatahub-io/llama-stack-k8s-operator) (67) -- top gap: AI Context Files
- [odh-model-controller](https://github.com/opendatahub-io/odh-model-controller) (66) -- top gap: AI Context Files
- [model-metadata-collection](https://github.com/opendatahub-io/model-metadata-collection) (66) -- top gap: Bug Report Template Quality
- [codeflare-operator](https://github.com/opendatahub-io/codeflare-operator) (65) -- top gap: AI Context Files
- [codeflare-operator-poc](https://github.com/opendatahub-io/codeflare-operator-poc) (65) -- top gap: AI Context Files
- [llm-d-kv-cache](https://github.com/opendatahub-io/llm-d-kv-cache) (64) -- top gap: AI Context Files
- [training-notebooks](https://github.com/opendatahub-io/training-notebooks) (64) -- top gap: AI Context Files
- [modelmesh-runtime-adapter](https://github.com/opendatahub-io/modelmesh-runtime-adapter) (64) -- top gap: AI Context Files
- [MLServer](https://github.com/opendatahub-io/MLServer) (62) -- top gap: AI Context Files
- [langfuse](https://github.com/opendatahub-io/langfuse) (62) -- top gap: One-Command Test Execution
- [kueue](https://github.com/opendatahub-io/kueue) (62) -- top gap: AI Context Files
- [llama-stack](https://github.com/opendatahub-io/llama-stack) (62) -- top gap: AI Context Files
- [base-containers](https://github.com/opendatahub-io/base-containers) (61) -- top gap: Bug Report Template Quality
- [kube-authkit](https://github.com/opendatahub-io/kube-authkit) (61) -- top gap: AI Context Files
- [model-registry-operator](https://github.com/opendatahub-io/model-registry-operator) (60) -- top gap: AI Context Files
- [caikit-nlp](https://github.com/opendatahub-io/caikit-nlp) (60) -- top gap: AI Context Files
- [trustyai-explainability](https://github.com/opendatahub-io/trustyai-explainability) (60) -- top gap: AI Context Files

### Needs Work (40-59) -- 25 repos

- [models-as-a-service](https://github.com/opendatahub-io/models-as-a-service) (59) -- top gap: AI Context Files
- [elyra](https://github.com/opendatahub-io/elyra) (59) -- top gap: AI Context Files
- [rest-proxy](https://github.com/opendatahub-io/rest-proxy) (59) -- top gap: AI Context Files
- [kubeflow](https://github.com/opendatahub-io/kubeflow) (58) -- top gap: AI Context Files
- [mcp-server-operator](https://github.com/opendatahub-io/mcp-server-operator) (58) -- top gap: AI Context Files
- [caikit-nlp-client](https://github.com/opendatahub-io/caikit-nlp-client) (58) -- top gap: AI Context Files
- [trustyai-service-operator](https://github.com/opendatahub-io/trustyai-service-operator) (57) -- top gap: AI Context Files
- [elyra-pipeline-editor](https://github.com/opendatahub-io/elyra-pipeline-editor) (55) -- top gap: AI Context Files
- [mlflow-go](https://github.com/opendatahub-io/mlflow-go) (55) -- top gap: AI Context Files
- [odh-ide-extensions](https://github.com/opendatahub-io/odh-ide-extensions) (53) -- top gap: AI Context Files
- [vllm-tgis-adapter](https://github.com/opendatahub-io/vllm-tgis-adapter) (53) -- top gap: AI Context Files
- [batch-gateway](https://github.com/opendatahub-io/batch-gateway) (52) -- top gap: AI Context Files
- [openvino](https://github.com/opendatahub-io/openvino) (52) -- top gap: One-Command Test Execution
- [llama-stack-provider-ragas](https://github.com/opendatahub-io/llama-stack-provider-ragas) (50) -- top gap: AI Context Files
- [openvino_model_server](https://github.com/opendatahub-io/openvino_model_server) (49) -- top gap: One-Command Test Execution
- [openvino.genai](https://github.com/opendatahub-io/openvino.genai) (48) -- top gap: One-Command Test Execution
- [distributed-workloads](https://github.com/opendatahub-io/distributed-workloads) (46) -- top gap: One-Command Test Execution
- [fms-guardrails-orchestrator](https://github.com/opendatahub-io/fms-guardrails-orchestrator) (46) -- top gap: One-Command Test Execution
- [guardrails-detectors](https://github.com/opendatahub-io/guardrails-detectors) (46) -- top gap: AI Context Files
- [llama-stack-client-python](https://github.com/opendatahub-io/llama-stack-client-python) (46) -- top gap: Test-to-Source Ratio
- [modelmesh](https://github.com/opendatahub-io/modelmesh) (45) -- top gap: AI Context Files
- [llama-stack-distribution](https://github.com/opendatahub-io/llama-stack-distribution) (44) -- top gap: One-Command Test Execution
- [lm-evaluation-harness](https://github.com/opendatahub-io/lm-evaluation-harness) (44) -- top gap: Test-to-Source Ratio
- [vllm-gaudi](https://github.com/opendatahub-io/vllm-gaudi) (42) -- top gap: AI Context Files
- [data-processing](https://github.com/opendatahub-io/data-processing) (40) -- top gap: Test-to-Source Ratio

### Not Ready (<40) -- 29 repos

- [llama-stack-provider-trustyai-garak](https://github.com/opendatahub-io/llama-stack-provider-trustyai-garak) (39)
- [elyra-examples](https://github.com/opendatahub-io/elyra-examples) (38)
- [rhaii-on-xks](https://github.com/opendatahub-io/rhaii-on-xks) (37)
- [openvino_contrib](https://github.com/opendatahub-io/openvino_contrib) (37)
- [perf_analyzer](https://github.com/opendatahub-io/perf_analyzer) (37)
- [llama-stack-provider-kfp-trainer](https://github.com/opendatahub-io/llama-stack-provider-kfp-trainer) (34)
- [modelcar-base-image](https://github.com/opendatahub-io/modelcar-base-image) (33)
- [caikit-tgis-serving](https://github.com/opendatahub-io/caikit-tgis-serving) (31)
- [fips-compliance-checker-claude-code-plugin](https://github.com/opendatahub-io/fips-compliance-checker-claude-code-plugin) (30)
- [openvino_tokenizers](https://github.com/opendatahub-io/openvino_tokenizers) (29)
- [rag](https://github.com/opendatahub-io/rag) (27)
- [llama-stack-demos](https://github.com/opendatahub-io/llama-stack-demos) (27)
- [client](https://github.com/opendatahub-io/client) (24)
- [ai-helpers](https://github.com/opendatahub-io/ai-helpers) (21)
- [ml-metadata](https://github.com/opendatahub-io/ml-metadata) (19)
- [odh-s2i-project-cds](https://github.com/opendatahub-io/odh-s2i-project-cds) (19)
- [llama-stack-provider-kft](https://github.com/opendatahub-io/llama-stack-provider-kft) (15)
- [vllm-orchestrator-gateway](https://github.com/opendatahub-io/vllm-orchestrator-gateway) (14)
- [llama-stack-provider-instructlab-train](https://github.com/opendatahub-io/llama-stack-provider-instructlab-train) (14)
- [odh-s2i-project-cookiecutter](https://github.com/opendatahub-io/odh-s2i-project-cookiecutter) (13)
- [agents](https://github.com/opendatahub-io/agents) (12)
- [odh-gitops](https://github.com/opendatahub-io/odh-gitops) (10)
- [opendatahub.io](https://github.com/opendatahub-io/opendatahub.io) (9)
- [opendatahub-documentation](https://github.com/opendatahub-io/opendatahub-documentation) (9)
- [llm-d-playbooks](https://github.com/opendatahub-io/llm-d-playbooks) (4)
- [model-runtimes-agent](https://github.com/opendatahub-io/model-runtimes-agent) (4)
- [odh-build-metadata](https://github.com/opendatahub-io/odh-build-metadata) (4)
- [odh-s2i-project-simple](https://github.com/opendatahub-io/odh-s2i-project-simple) (4)
- [dsp-dev-tools](https://github.com/opendatahub-io/dsp-dev-tools) (4)

## Repository Scores

| Repository | Score | Level | Languages |
|---|---|---|---|
| [odh-dashboard](https://github.com/opendatahub-io/odh-dashboard) | 86/100 | Ready | TypeScript, Go, JavaScript |
| [litellm](https://github.com/opendatahub-io/litellm) | 82/100 | Ready | Python, TypeScript, JavaScript |
| [data-science-pipelines](https://github.com/opendatahub-io/data-science-pipelines) | 81/100 | Ready | Python, TypeScript, Go |
| [feast](https://github.com/opendatahub-io/feast) | 80/100 | Ready | Python, TypeScript, Go |
| [eval-hub](https://github.com/opendatahub-io/eval-hub) | 78/100 | Partially Ready | Go, Shell, Python |
| [notebooks](https://github.com/opendatahub-io/notebooks) | 76/100 | Partially Ready | Python, Shell, TypeScript |
| [opendatahub-tests](https://github.com/opendatahub-io/opendatahub-tests) | 76/100 | Partially Ready | Python |
| [data-science-pipelines-operator](https://github.com/opendatahub-io/data-science-pipelines-operator) | 75/100 | Partially Ready | Go, Shell, Python |
| [workload-variant-autoscaler](https://github.com/opendatahub-io/workload-variant-autoscaler) | 75/100 | Partially Ready | Go, Shell |
| [model-registry](https://github.com/opendatahub-io/model-registry) | 75/100 | Partially Ready | TypeScript, Go, Python |
| [modelmesh-serving](https://github.com/opendatahub-io/modelmesh-serving) | 74/100 | Partially Ready | Go, Shell, Python |
| [kuberay](https://github.com/opendatahub-io/kuberay) | 74/100 | Partially Ready | Go, Python, TypeScript |
| [NeMo-Guardrails](https://github.com/opendatahub-io/NeMo-Guardrails) | 73/100 | Partially Ready | Python, JavaScript, Shell |
| [kube-auth-proxy](https://github.com/opendatahub-io/kube-auth-proxy) | 73/100 | Partially Ready | Go, Shell, JavaScript |
| [kserve](https://github.com/opendatahub-io/kserve) | 73/100 | Partially Ready | Python, Go, Shell |
| [argo-workflows](https://github.com/opendatahub-io/argo-workflows) | 72/100 | Partially Ready | Go, Python, TypeScript |
| [llm-d-inference-scheduler](https://github.com/opendatahub-io/llm-d-inference-scheduler) | 72/100 | Partially Ready | Go, Shell |
| [rhoai-mcp](https://github.com/opendatahub-io/rhoai-mcp) | 72/100 | Partially Ready | Python |
| [mlflow-operator](https://github.com/opendatahub-io/mlflow-operator) | 71/100 | Partially Ready | Python, Go, Shell |
| [training-operator](https://github.com/opendatahub-io/training-operator) | 71/100 | Partially Ready | Go, Python, Shell |
| [semantic-router](https://github.com/opendatahub-io/semantic-router) | 70/100 | Partially Ready | Go, TypeScript, Python |
| [spark-operator](https://github.com/opendatahub-io/spark-operator) | 70/100 | Partially Ready | Go, Shell, Python |
| [mod-arch-library](https://github.com/opendatahub-io/mod-arch-library) | 69/100 | Partially Ready | TypeScript, Go, JavaScript |
| [opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) | 69/100 | Partially Ready | Go, Shell, JavaScript |
| [mlflow](https://github.com/opendatahub-io/mlflow) | 69/100 | Partially Ready | Python, TypeScript, JavaScript |
| [trainer](https://github.com/opendatahub-io/trainer) | 69/100 | Partially Ready | Python, Go, Rust |
| [trainer-sdk](https://github.com/opendatahub-io/trainer-sdk) | 68/100 | Partially Ready | Python, Go, Shell |
| [kubeflow-sdk](https://github.com/opendatahub-io/kubeflow-sdk) | 68/100 | Partially Ready | Python |
| [odh-cli](https://github.com/opendatahub-io/odh-cli) | 68/100 | Partially Ready | Go |
| [rhaii-cluster-validation](https://github.com/opendatahub-io/rhaii-cluster-validation) | 68/100 | Partially Ready | Go |
| [model-registry-bf4-kf](https://github.com/opendatahub-io/model-registry-bf4-kf) | 68/100 | Partially Ready | Go, Python, Shell |
| [llama-stack-k8s-operator](https://github.com/opendatahub-io/llama-stack-k8s-operator) | 67/100 | Partially Ready | Go, Shell |
| [odh-model-controller](https://github.com/opendatahub-io/odh-model-controller) | 66/100 | Partially Ready | Go, Shell |
| [model-metadata-collection](https://github.com/opendatahub-io/model-metadata-collection) | 66/100 | Partially Ready | Go |
| [codeflare-operator](https://github.com/opendatahub-io/codeflare-operator) | 65/100 | Partially Ready | Go, Shell |
| [codeflare-operator-poc](https://github.com/opendatahub-io/codeflare-operator-poc) | 65/100 | Partially Ready | Go, Shell |
| [llm-d-kv-cache](https://github.com/opendatahub-io/llm-d-kv-cache) | 64/100 | Partially Ready | Go, Python, C++ |
| [training-notebooks](https://github.com/opendatahub-io/training-notebooks) | 64/100 | Partially Ready | Python, Shell, TypeScript |
| [modelmesh-runtime-adapter](https://github.com/opendatahub-io/modelmesh-runtime-adapter) | 64/100 | Partially Ready | Go, Shell |
| [MLServer](https://github.com/opendatahub-io/MLServer) | 62/100 | Partially Ready | Python, Shell, JavaScript |
| [langfuse](https://github.com/opendatahub-io/langfuse) | 62/100 | Partially Ready | TypeScript, Shell, JavaScript |
| [kueue](https://github.com/opendatahub-io/kueue) (verify gate) | 62/100 | Partially Ready | Go, JavaScript, Shell |
| [llama-stack](https://github.com/opendatahub-io/llama-stack) | 62/100 | Partially Ready | Python, TypeScript, Shell |
| [base-containers](https://github.com/opendatahub-io/base-containers) | 61/100 | Partially Ready | Python, Shell |
| [kube-authkit](https://github.com/opendatahub-io/kube-authkit) | 61/100 | Partially Ready | Python |
| [model-registry-operator](https://github.com/opendatahub-io/model-registry-operator) | 60/100 | Partially Ready | Go, Shell |
| [caikit-nlp](https://github.com/opendatahub-io/caikit-nlp) | 60/100 | Partially Ready | Python, Shell |
| [trustyai-explainability](https://github.com/opendatahub-io/trustyai-explainability) | 60/100 | Partially Ready | Java, Python |
| [models-as-a-service](https://github.com/opendatahub-io/models-as-a-service) | 59/100 | Needs Work | Go, Shell, Python |
| [elyra](https://github.com/opendatahub-io/elyra) | 59/100 | Needs Work | Python, TypeScript, JavaScript |
| [rest-proxy](https://github.com/opendatahub-io/rest-proxy) | 59/100 | Needs Work | Go |
| [kubeflow](https://github.com/opendatahub-io/kubeflow) | 58/100 | Needs Work | Go, Shell |
| [mcp-server-operator](https://github.com/opendatahub-io/mcp-server-operator) | 58/100 | Needs Work | Go |
| [caikit-nlp-client](https://github.com/opendatahub-io/caikit-nlp-client) | 58/100 | Needs Work | Python |
| [trustyai-service-operator](https://github.com/opendatahub-io/trustyai-service-operator) | 57/100 | Needs Work | Go |
| [elyra-pipeline-editor](https://github.com/opendatahub-io/elyra-pipeline-editor) | 55/100 | Needs Work | TypeScript, JavaScript |
| [mlflow-go](https://github.com/opendatahub-io/mlflow-go) | 55/100 | Needs Work | Go |
| [odh-ide-extensions](https://github.com/opendatahub-io/odh-ide-extensions) | 53/100 | Needs Work | Python, TypeScript, JavaScript |
| [vllm-tgis-adapter](https://github.com/opendatahub-io/vllm-tgis-adapter) | 53/100 | Needs Work | Python |
| [batch-gateway](https://github.com/opendatahub-io/batch-gateway) | 52/100 | Needs Work | Go |
| [openvino](https://github.com/opendatahub-io/openvino) | 52/100 | Needs Work | C++, Python, JavaScript |
| [llama-stack-provider-ragas](https://github.com/opendatahub-io/llama-stack-provider-ragas) | 50/100 | Needs Work | Python |
| [openvino_model_server](https://github.com/opendatahub-io/openvino_model_server) | 49/100 | Needs Work | C++, Python, Shell |
| [openvino.genai](https://github.com/opendatahub-io/openvino.genai) | 48/100 | Needs Work | C++, Python, TypeScript |
| [distributed-workloads](https://github.com/opendatahub-io/distributed-workloads) | 46/100 | Needs Work | Go, Python, Shell |
| [fms-guardrails-orchestrator](https://github.com/opendatahub-io/fms-guardrails-orchestrator) | 46/100 | Needs Work | Rust, Shell |
| [guardrails-detectors](https://github.com/opendatahub-io/guardrails-detectors) | 46/100 | Needs Work | Python |
| [llama-stack-client-python](https://github.com/opendatahub-io/llama-stack-client-python) | 46/100 | Needs Work | Python |
| [modelmesh](https://github.com/opendatahub-io/modelmesh) | 45/100 | Needs Work | Java, Shell |
| [llama-stack-distribution](https://github.com/opendatahub-io/llama-stack-distribution) | 44/100 | Needs Work | Shell |
| [lm-evaluation-harness](https://github.com/opendatahub-io/lm-evaluation-harness) | 44/100 | Needs Work | Python, Shell |
| [vllm-gaudi](https://github.com/opendatahub-io/vllm-gaudi) (verify gate) | 42/100 | Needs Work | Python, Shell, C++ |
| [data-processing](https://github.com/opendatahub-io/data-processing) | 40/100 | Needs Work | Python |
| [llama-stack-provider-trustyai-garak](https://github.com/opendatahub-io/llama-stack-provider-trustyai-garak) | 39/100 | Not Ready | Python |
| [elyra-examples](https://github.com/opendatahub-io/elyra-examples) (verify gate) | 38/100 | Not Ready | Python |
| [rhaii-on-xks](https://github.com/opendatahub-io/rhaii-on-xks) (verify gate) | 37/100 | Not Ready | Shell |
| [openvino_contrib](https://github.com/opendatahub-io/openvino_contrib) (verify gate) | 37/100 | Not Ready | C++, TypeScript, Python |
| [perf_analyzer](https://github.com/opendatahub-io/perf_analyzer) | 37/100 | Not Ready | Python |
| [llama-stack-provider-kfp-trainer](https://github.com/opendatahub-io/llama-stack-provider-kfp-trainer) (verify gate) | 34/100 | Not Ready | Python, Shell |
| [modelcar-base-image](https://github.com/opendatahub-io/modelcar-base-image) (verify gate) | 33/100 | Not Ready | Python, Shell |
| [caikit-tgis-serving](https://github.com/opendatahub-io/caikit-tgis-serving) (verify gate) | 31/100 | Not Ready | Shell |
| [fips-compliance-checker-claude-code-plugin](https://github.com/opendatahub-io/fips-compliance-checker-claude-code-plugin) (verify gate) | 30/100 | Not Ready | Python, Shell |
| [openvino_tokenizers](https://github.com/opendatahub-io/openvino_tokenizers) (verify gate) | 29/100 | Not Ready | C++, Python, JavaScript |
| [rag](https://github.com/opendatahub-io/rag) (verify gate) | 27/100 | Not Ready | Python, Go, Shell |
| [llama-stack-demos](https://github.com/opendatahub-io/llama-stack-demos) (verify gate) | 27/100 | Not Ready | Python |
| [client](https://github.com/opendatahub-io/client) (verify gate) | 24/100 | Not Ready | Python, Java |
| [ai-helpers](https://github.com/opendatahub-io/ai-helpers) (verify gate) | 21/100 | Not Ready | Python, Shell |
| [ml-metadata](https://github.com/opendatahub-io/ml-metadata) (verify gate) | 19/100 | Not Ready | Python, Go, Shell |
| [odh-s2i-project-cds](https://github.com/opendatahub-io/odh-s2i-project-cds) (verify gate) | 19/100 | Not Ready | Python |
| [llama-stack-provider-kft](https://github.com/opendatahub-io/llama-stack-provider-kft) (verify gate) | 15/100 | Not Ready | Python |
| [vllm-orchestrator-gateway](https://github.com/opendatahub-io/vllm-orchestrator-gateway) (verify gate) | 14/100 | Not Ready | Rust |
| [llama-stack-provider-instructlab-train](https://github.com/opendatahub-io/llama-stack-provider-instructlab-train) (verify gate) | 14/100 | Not Ready | Python |
| [odh-s2i-project-cookiecutter](https://github.com/opendatahub-io/odh-s2i-project-cookiecutter) (verify gate) | 13/100 | Not Ready | Python |
| [agents](https://github.com/opendatahub-io/agents) (verify gate) | 12/100 | Not Ready | Python, Go, Shell |
| [odh-gitops](https://github.com/opendatahub-io/odh-gitops) (verify gate) | 10/100 | Not Ready | Shell |
| [opendatahub.io](https://github.com/opendatahub-io/opendatahub.io) (verify gate) | 9/100 | Not Ready | TypeScript |
| [opendatahub-documentation](https://github.com/opendatahub-io/opendatahub-documentation) (verify gate) | 9/100 | Not Ready | Shell |
| [llm-d-playbooks](https://github.com/opendatahub-io/llm-d-playbooks) (verify gate) | 4/100 | Not Ready | Shell, Python |
| [model-runtimes-agent](https://github.com/opendatahub-io/model-runtimes-agent) (verify gate) | 4/100 | Not Ready | Python |
| [odh-build-metadata](https://github.com/opendatahub-io/odh-build-metadata) (verify gate) | 4/100 | Not Ready | Shell, Python |
| [odh-s2i-project-simple](https://github.com/opendatahub-io/odh-s2i-project-simple) (verify gate) | 4/100 | Not Ready | Python |
| [dsp-dev-tools](https://github.com/opendatahub-io/dsp-dev-tools) (verify gate) | 4/100 | Not Ready | Python, Shell |

## Quick Wins (Highest Impact Actions)

| Action | Repos Below 40 | Weight | How to Fix |
|---|---|---|---|
| AI Context Files | 80 repos | 8% | Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md. |
| Bug Report Template Quality | 73 repos | 8% | Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs. |
| Architecture Documentation | 92 repos | 3% | Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure. |
| Coverage Configuration | 57 repos | 3% | Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration. |
| PR Template | 63 repos | 2% | Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist. |
| Test Fixtures / Sample Data | 46 repos | 2% | Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs. |
| Pre-commit / Local Hooks | 45 repos | 3% | Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting. |

## All Checks Ranked by Average Score

| Check | Avg Score | Weight |
|---|---|---|
| AI Context Files | 21/100 | 8% |
| Architecture Documentation | 25/100 | 3% |
| Bug Report Template Quality | 26/100 | 8% |
| PR Template | 31/100 | 2% |
| Coverage Configuration | 35/100 | 3% |
| Test Fixtures / Sample Data | 38/100 | 2% |
| Pre-commit / Local Hooks | 50/100 | 3% |
| Build / Dependency Setup | 50/100 | 5% |
| Structured Logging / Errors | 50/100 | 3% |
| Code Ownership (CODEOWNERS) | 52/100 | 1% |
| Test-to-Source Ratio | 55/100 | 15% |
| Contributing / Dev Guide | 58/100 | 5% |
| One-Command Test Execution | 58/100 | 11% |
| Linting / Formatting in CI | 59/100 | 5% |
| Type Safety / Static Analysis | 65/100 | 3% |
| Test Isolation (unit vs e2e) | 74/100 | 4% |
| Code Navigability | 75/100 | 5% |
| Dependency Complexity | 75/100 | 2% |
| CI Runs Tests on PRs | 75/100 | 10% |
| Generated Code Ratio | 95/100 | 2% |

## Per-Repository Details

### odh-dashboard -- 86/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (4/7 quality keywords); claude.md found (4/7 quality keywords); AGENTS.md found (4/7 quality keywords); Agents.md found (4/7 quality keywords); agents.md found (4/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (8/50 sampled files); Error wrapping patterns (8 files) |
| Architecture Documentation | Understand | 3% | 70 | Architecture doc: docs/architecture.md; 68 module-level READMEs |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 120 lines (5639 source files, generated excluded); Files >500 lines: 181 (3%); Largest: mockPipelineSpec.ts (5220L), modelServingDeploy.cy.ts (2793L), token_k8s_client.go (2578L) |
| Generated Code Ratio | Navigate | 2% | 100 | 46/5695 files are generated (1%); Examples: http_mock.go, token_k8s_client_mock.go, internal_k8s_client_mock.go, mock_factory.go, mock_factory.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: npm lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 6 direct dependencies / 5649 source files (ratio: 0.00) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), OWNERS_ALIASES present |
| Test-to-Source Ratio | Verify | 15% | 70 | 1107 test files / 4542 source files (ratio: 0.24); Frontend-heavy repo (relaxed thresholds) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: packages/maas/test; npm test script defined |
| Coverage Configuration | Verify | 3% | 80 | Codecov configured; Coverage in CI workflow: test.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 6 CI workflow(s): automl-bff-tests.yml, autorag-bff-tests.yml, eval-hub-frontend-tests.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: automl-bff-tests.yml, eval-hub-bff-tests.yml, autorag-bff-tests.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~97% unit tests, ~3% infra-dependent (28/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | Husky git hooks configured; .husky/ directory found |

### litellm -- 82/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords); AGENTS.md found (2/7 quality keywords); Agents.md found (2/7 quality keywords); agents.md found (2/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 65 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (10 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 46 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 4/20 sampled test files |
| Code Navigability | Navigate | 5% | 70 | Average file: 281 lines (2137 source files, generated excluded); Files >500 lines: 285 (13%); Largest: proxy_server.py (9467L), utils.py (7739L), networking.tsx (7525L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/2158 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: npm lockfile, Poetry lockfile; Dockerfile/Containerfile for reproducible builds; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml; Pyright configured |
| Dependency Complexity | Navigate | 2% | 90 | 61 direct dependencies / 2158 source files (ratio: 0.03) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 826 test files / 1332 source files (ratio: 0.62) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, test-unit, test-integration; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test-litellm.yml, llm-translation-testing.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: test-linting.yml, ghcr_helm_deploy.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 100 | ~97% unit tests, ~3% infra-dependent (29/30 sampled); Makefile separates unit and integration test targets |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### data-science-pipelines -- 81/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | AGENTS.md found (6/7 quality keywords); Agents.md found (6/7 quality keywords); agents.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (12 files) |
| Architecture Documentation | Understand | 3% | 30 | 89 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: samples (53 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 201 lines (2293 source files, generated excluded); Files >500 lines: 174 (8%); Largest: pipeline_spec_pb.js (15776L), large-graph-runtime.ts (12660L), pipeline_spec.ts (10579L) |
| Generated Code Ratio | Navigate | 2% | 80 | 391/2708 files are generated (14%); Examples: cache_key.pb.go, pipeline_spec.pb.go, clientset.go, doc.go, register.go |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Go lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go; mypy.ini found |
| Dependency Complexity | Navigate | 2% | 90 | 244 direct dependencies / 2317 source files (ratio: 0.11) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 17 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 665 test files / 1652 source files (ratio: 0.40) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: manifests/kustomize/test; pytest.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 12 CI workflow(s): kfp-sdk-client-tests.yml, legacy-v2-api-integration-tests.yml, integration-tests-v1.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: pre-commit.yml, sdk-isort.yml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### feast -- 80/100 (Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Go structured logging (zerolog) found in go.mod; Error wrapping patterns (7 files) |
| Architecture Documentation | Understand | 3% | 30 | 76 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (164 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 196 lines (1084 source files, generated excluded); Files >500 lines: 100 (9%); Largest: feature_store.py (3352L), ray.py (2370L), test_search_api.py (2290L) |
| Generated Code Ratio | Navigate | 2% | 100 | 2/1234 files are generated (0%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Go lockfile; Build/install targets in Makefile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go, Java; mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 125 direct dependencies / 1232 source files (ratio: 0.10) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (CODEOWNERS) with 18 rules |
| Test-to-Source Ratio | Verify | 15% | 50 | 343 test files / 889 source files (ratio: 0.39) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, infra/feast-operator/test, infra/feast-operator/test-e2e; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 13 CI workflow(s): release.yml, pr_registration_integration_tests.yml, pr_local_integration_tests.yml |
| PR Template | Submit | 2% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: linter.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~87% unit tests, ~13% infra-dependent (26/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### eval-hub -- 78/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (6/7 quality keywords); claude.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has reproduction steps; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (17/50 sampled files); Error wrapping patterns (26 files) |
| Architecture Documentation | Understand | 3% | 30 | 8 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (1 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 185 lines (133 source files, generated excluded); Files >500 lines: 12 (9%); Largest: step_definitions_test.go (2232L), step_definitions_test.go (1218L), evaluations_test.go (854L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/133 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile, npm lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 167 direct dependencies / 133 source files (ratio: 1.26) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 8 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 43 test files / 90 source files (ratio: 0.48) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 100 | Codecov configured; Go coverage flags in Makefile; Coverage in CI workflow: ci.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~90% unit tests, ~10% infra-dependent (27/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### notebooks -- 76/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | AGENTS.md found (6/7 quality keywords); Agents.md found (6/7 quality keywords); agents.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (12 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 21 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (2 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 150 lines (141 source files, generated excluded); Files >500 lines: 7 (5%); Largest: konflux_generate_component_build_pipelines.py (866L), test_main.py (767L), gpu_library_loading_test.py (697L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/146 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 28 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 34 test files / 112 source files (ratio: 0.30) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test; pytest.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): build-notebooks-TEMPLATE.yaml, code-quality.yaml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: pr-merge-image-delete.yml, auto-add-issue-to-project.yml, sec-scan.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~80% unit tests, ~20% infra-dependent (24/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### opendatahub-tests -- 76/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | AGENTS.md found (4/7 quality keywords); Agents.md found (4/7 quality keywords); agents.md found (4/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 65 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (4 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 80 | Fixture directories: tests/fixtures (5 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 159 lines (355 source files, generated excluded); Files >500 lines: 23 (6%); Largest: infra.py (1198L), utils.py (976L), conftest.py (971L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/423 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: uv lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 2 direct dependencies / 423 source files (ratio: 0.00) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 9 rules |
| Test-to-Source Ratio | Verify | 15% | 100 | 261 test files / 162 source files (ratio: 1.61) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: check; tox.ini found; pytest.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): tox-tests.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: docs/CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### data-science-pipelines-operator -- 75/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (21/50 sampled files); Error wrapping patterns (12 files) |
| Architecture Documentation | Understand | 3% | 30 | 4 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 172 lines (66 source files, generated excluded); Files >500 lines: 4 (6%); Largest: dspipeline_params.go (907L), dspipeline_controller.go (819L), storage_test.go (562L) |
| Generated Code Ratio | Navigate | 2% | 100 | 1/67 files are generated (1%); Examples: zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 104 direct dependencies / 66 source files (ratio: 1.58) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 18 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 29 test files / 37 source files (ratio: 0.78) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, unittest, functest; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): functests.yml, nightly_tests.yml, unittests.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: precommit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 85 | ~52% unit tests, ~48% infra-dependent (15/29 sampled); Makefile separates unit and integration test targets |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### workload-variant-autoscaler -- 75/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (0/7 quality keywords); claude.md found (0/7 quality keywords); AGENTS.md found (6/7 quality keywords); Agents.md found (6/7 quality keywords); agents.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (13/50 sampled files); Error wrapping patterns (18 files) |
| Architecture Documentation | Understand | 3% | 30 | 8 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 256 lines (206 source files, generated excluded); Files >500 lines: 23 (11%); Largest: greedy_test.go (1684L), install.sh (1659L), system_test.go (1651L) |
| Generated Code Ratio | Navigate | 2% | 100 | 1/207 files are generated (0%); Examples: zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 70 | 106 direct dependencies / 206 source files (ratio: 0.51) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 14 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 88 test files / 118 source files (ratio: 0.75) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci-pr-checks.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-pr-checks.yaml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~79% unit tests, ~21% infra-dependent (22/28 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | .pre-commit-config.yaml found |

### model-registry -- 75/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Some logging (12/50 sampled files); Error wrapping patterns (11 files) |
| Architecture Documentation | Understand | 3% | 30 | 21 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 208 lines (1116 source files, generated excluded); Files >500 lines: 102 (9%); Largest: model_registry_service_api.py (15724L), artifact_test.go (3474L), model_catalog_service_api.py (2654L) |
| Generated Code Ratio | Navigate | 2% | 80 | 182/1301 files are generated (14%); Examples: model_base_model.go, model_metric_create.go, model_doc_artifact_update.go, model_metadata_struct_value.go, model_base_resource_update.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 106 direct dependencies / 1119 source files (ratio: 0.09) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 26 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 308 test files / 811 source files (ratio: 0.38) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, clients/python/test-e2e, clients/python/test, catalog/test, jobs/async-upload/test, jobs/async-upload/test-e2e, jobs/async-upload/test-integration; Multiple test types available |
| Coverage Configuration | Verify | 3% | 100 | Go coverage flags in Makefile; Coverage in CI workflow: python-tests.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): ui-frontend-build.yml, python-tests.yml, async-upload-test.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ui-bff-build.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### modelmesh-serving -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (19/50 sampled files); Error wrapping patterns (16 files) |
| Architecture Documentation | Understand | 3% | 30 | 15 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 173 lines (126 source files, generated excluded); Files >500 lines: 7 (6%); Largest: predictor_test.go (1286L), fvtclient.go (1019L), servingruntime_controller.go (801L) |
| Generated Code Ratio | Navigate | 2% | 80 | 14/140 files are generated (10%); Examples: kfs_inference_v2.pb.go, inference_grpc.pb.go, inference.pb.go, tensor_shape.pb.go, types.pb.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 70 | 123 direct dependencies / 126 source files (ratio: 0.98) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 23 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 34 test files / 92 source files (ratio: 0.37) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, e2e-test, tests/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, build.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: lint.yml, build.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~73% unit tests, ~27% infra-dependent (22/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### kuberay -- 74/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 95 | Found: .github/ISSUE_TEMPLATE/bug-report.yml; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Go structured logging (zerolog) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (12/50 sampled files); Error wrapping patterns (11 files) |
| Architecture Documentation | Understand | 3% | 30 | 11 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 217 lines (364 source files, generated excluded); Files >500 lines: 38 (10%); Largest: raycluster_controller_unit_test.go (3811L), raycluster_controller.go (2053L), pod_test.go (1954L) |
| Generated Code Ratio | Navigate | 2% | 60 | 78/443 files are generated (18%); Examples: datafile.go, client_manager_mock.go, kubernetes_mock.go, cluster_mock.go, utils.go |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Go lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 114 direct dependencies / 365 source files (ratio: 0.31) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 85 | 146 test files / 219 source files (ratio: 0.67) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: ray-operator/test, ray-operator/test, ray-operator/test, ray-operator/test-e2e, ray-operator/test-e2e, apiserver/test, apiserver/e2e-test, apiserversdk/test, apiserversdk/test, apiserversdk/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): odh-release.yml, image-release.yaml, e2e-tests.yaml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: helm.yaml, test-job.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~59% unit tests, ~41% infra-dependent (16/27 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### NeMo-Guardrails -- 73/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 90 | Python structured logging found in requirements.txt; Error wrapping patterns (9 files) |
| Architecture Documentation | Understand | 3% | 30 | 96 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (361 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 223 lines (668 source files, generated excluded); Files >500 lines: 64 (10%); Largest: test_flow_mechanics.py (2429L), statemachine.py (2174L), config.py (2068L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/668 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Poetry lockfile; Dockerfile/Containerfile for reproducible builds; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 11/20 sampled Python files |
| Dependency Complexity | Navigate | 2% | 90 | 145 direct dependencies / 668 source files (ratio: 0.22) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 296 test files / 372 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test; pytest configured in pyproject.toml; tox.ini found; pytest.ini found |
| Coverage Configuration | Verify | 3% | 80 | Coverage-related target in Makefile; Coverage in CI workflow: _test.yml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): _test.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### kube-auth-proxy -- 73/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug-report.yml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Some logging (7/50 sampled files); Error wrapping patterns (22 files) |
| Architecture Documentation | Understand | 3% | 30 | 13 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 80 | Fixture directories: testdata, examples (9 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 178 lines (264 source files, generated excluded); Files >500 lines: 17 (6%); Largest: oauthproxy_test.go (3583L), oauthproxy.go (1570L), server_test.go (1321L) |
| Generated Code Ratio | Navigate | 2% | 100 | 6/270 files are generated (2%); Examples: mock_lock.go, mock_store.go, mock_openshift_oauth.go, mock_oidc_test.go, mock_openshift_oauth_test.go |
| Build / Dependency Setup | Navigate | 5% | 100 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 67 direct dependencies / 264 source files (ratio: 0.25) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 9 rules |
| Test-to-Source Ratio | Verify | 15% | 85 | 128 test files / 136 source files (ratio: 0.94) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, test-integration, kube-rbac-proxy/test, kube-rbac-proxy/test-unit, kube-rbac-proxy/test-e2e; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~68% unit tests, ~32% infra-dependent (19/28 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### kserve -- 73/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (10 files) |
| Architecture Documentation | Understand | 3% | 30 | 123 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 30 | Average file: 759 lines (1069 source files, generated excluded); Files >500 lines: 165 (15%); Largest: llmisvc-full-install-with-manifests.sh (91399L), llmisvc-full-install-with-manifests.sh (90786L), llmisvc-full-install-with-manifests.sh (90744L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 80 | 115/1201 files are generated (10%); Examples: openapi_generated.go, clientset.go, register.go, doc.go, register.go |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: Go lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 207 direct dependencies / 1086 source files (ratio: 0.19) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 29 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 474 test files / 612 source files (ratio: 0.77) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: check, test, tools/tf2openapi/test, python/xgbserver/test, python/aiffairness/test, python/lgbserver/test, python/paddleserver/test, python/kserve/test, python/huggingfaceserver/test, python/custom_model/test, python/predictiveserver/test, python/custom_transformer/test, python/pmmlserver/test, python/artexplainer/test, python/sklearnserver/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 100 | Go coverage flags in Makefile; Coverage in CI workflow: go.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): go.yml, python-test.yml, precommit-check.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 60 | Found: CONTRIBUTING.md; 1/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~83% unit tests, ~17% infra-dependent (24/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### argo-workflows -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 90 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has environment/version fields; Has log/error output fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (9/50 sampled files); Error wrapping patterns (21 files) |
| Architecture Documentation | Understand | 3% | 70 | Architecture doc: docs/architecture.md; 11 module-level READMEs |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (207 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 197 lines (1403 source files, generated excluded); Files >500 lines: 56 (4%); Largest: operator_test.go (11613L), operator.go (4259L), util_test.go (4178L) |
| Generated Code Ratio | Navigate | 2% | 80 | 81/1484 files are generated (5%); Examples: clientset.go, doc.go, register.go, doc.go, register.go |
| Build / Dependency Setup | Navigate | 5% | 100 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 304 direct dependencies / 1403 source files (ratio: 0.22) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 50 | 272 test files / 1131 source files (ratio: 0.24) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, sdks/python/test, sdks/java/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Codecov configured; Coverage-related target in Makefile; Coverage in CI workflow: ci-build.yaml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): ci-build.yaml, release.yaml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-build.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~92% unit tests, ~8% infra-dependent (24/26 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llm-d-inference-scheduler -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 70 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (18/50 sampled files); Error wrapping patterns (13 files) |
| Architecture Documentation | Understand | 3% | 55 | Architecture doc: docs/architecture.md; 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 161 lines (78 source files, generated excluded); Files >500 lines: 5 (6%); Largest: e2e_test.go (939L), no_hit_lru_test.go (586L), precise_prefix_cache_test.go (580L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/78 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Go lockfile; Build/install targets in Makefile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 137 direct dependencies / 78 source files (ratio: 1.76) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), OWNERS_ALIASES present |
| Test-to-Source Ratio | Verify | 15% | 85 | 34 test files / 44 source files (ratio: 0.77) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, test-unit, test-integration, test-e2e; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci-pr-checks.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-pr-checks.yaml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: DEVELOPMENT.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~90% unit tests, ~10% infra-dependent (26/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### rhoai-mcp -- 72/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (7/7 quality keywords); claude.md found (7/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 40 | Architecture doc: docs/architecture.md *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 6/20 sampled test files |
| Code Navigability | Navigate | 5% | 70 | Average file: 193 lines (176 source files, generated excluded); Files >500 lines: 14 (8%); Largest: tools.py (1147L), test_tools.py (1048L), tools.py (1021L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/183 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: uv lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 6 direct dependencies / 183 source files (ratio: 0.03) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 70 | 61 test files / 122 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, test-unit, test-integration, check; Multiple test types available; pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 80 | Coverage in CI workflow: ci.yml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): ci.yml, eval.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### mlflow-operator -- 71/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (7/50 sampled files); Error wrapping patterns (16 files) |
| Architecture Documentation | Understand | 3% | 30 | 4 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 213 lines (55 source files, generated excluded); Files >500 lines: 5 (9%); Largest: helm_test.go (2185L), deploy.py (1010L), helm.go (588L) |
| Generated Code Ratio | Navigate | 2% | 100 | 2/57 files are generated (4%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 30 | 117 direct dependencies / 55 source files (ratio: 2.13) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 6 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 26 test files / 29 source files (ratio: 0.90) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test, test-e2e |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test.yml, integration-tests.yml, test-e2e.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~92% unit tests, ~8% infra-dependent (23/25 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### training-operator -- 71/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (11 files) |
| Architecture Documentation | Understand | 3% | 30 | 19 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (99 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 178 lines (271 source files, generated excluded); Files >500 lines: 18 (7%); Largest: training_client_test.py (1995L), training_client.py (1558L), mpijob_controller.go (1400L) |
| Generated Code Ratio | Navigate | 2% | 60 | 69/343 files are generated (20%); Examples: clientset.go, register.go, doc.go, register.go, clientset_generated.go |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Go lockfile; Build/install targets in Makefile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 76 direct dependencies / 274 source files (ratio: 0.28) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), OWNERS_ALIASES present |
| Test-to-Source Ratio | Verify | 15% | 50 | 67 test files / 207 source files (ratio: 0.32) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): unittests.yaml, test-python.yaml, integration-tests.yaml |
| PR Template | Submit | 2% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: test-go.yaml, pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~90% unit tests, ~10% infra-dependent (26/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### semantic-router -- 70/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (3) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (14/50 sampled files); Error wrapping patterns (14 files) |
| Architecture Documentation | Understand | 3% | 30 | 56 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 348 lines (1273 source files, generated excluded); Files >500 lines: 245 (19%); Largest: extproc_test.go (5228L), dsl_test.go (4518L), semantic-router_test.go (4474L) |
| Generated Code Ratio | Navigate | 2% | 100 | 4/1277 files are generated (0%); Examples: nlp_binding_mock.go, semantic-router_mock.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go, Rust |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 50 | 242 test files / 1031 source files (ratio: 0.23) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: paper/check, deploy/operator/test, src/vllm-sr/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 60 | Coverage in CI workflow: operator-ci.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): integration-test-k8s.yml, operator-ci.yml, publish-crate.yml |
| PR Template | Submit | 2% | 55 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: ci-changes.yml, integration-test-helm.yml, helm-publish.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~93% unit tests, ~7% infra-dependent (28/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### spark-operator -- 70/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (14/50 sampled files); Error wrapping patterns (14 files) |
| Architecture Documentation | Understand | 3% | 30 | 6 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (40 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 208 lines (134 source files, generated excluded); Files >500 lines: 10 (7%); Largest: sparkpod_defaulter_test.go (2351L), controller.go (1472L), controller_test.go (1440L) |
| Generated Code Ratio | Navigate | 2% | 60 | 27/161 files are generated (17%); Examples: clientset.go, register.go, doc.go, register.go, clientset_generated.go |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: Go lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 153 direct dependencies / 134 source files (ratio: 1.14) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 10 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 38 test files / 96 source files (ratio: 0.40) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: unit-test, e2e-test |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): integration.yaml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: integration.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~83% unit tests, ~17% infra-dependent (25/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | .pre-commit-config.yaml found |

### mod-arch-library -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (0/7 quality keywords); claude.md found (0/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (12/50 sampled files); Error wrapping patterns (6 files) |
| Architecture Documentation | Understand | 3% | 70 | Architecture doc: docs/architecture.md; 14 module-level READMEs |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 66 lines (307 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 4/312 files are generated (1%); Examples: http_mock.go, token_k8s_client_mock.go, internal_k8s_client_mock.go, mock_factory.go |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: npm lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 70 | 47 test files / 261 source files (ratio: 0.18); Frontend-heavy repo (relaxed thresholds) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: mod-arch-starter/bff/test; npm test script defined |
| Coverage Configuration | Verify | 3% | 60 | Coverage in CI workflow: test.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): release.yml, publish.yml, test.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~90% unit tests, ~10% infra-dependent (27/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | Husky git hooks configured; .husky/ directory found |

### opendatahub-operator -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Found .github/ISSUE_TEMPLATE/bug_report.md but name/about fields don't indicate a bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (9/50 sampled files); Error wrapping patterns (16 files) |
| Architecture Documentation | Understand | 3% | 70 | Architecture doc: docs/design.md; 6 module-level READMEs |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 209 lines (559 source files, generated excluded); Files >500 lines: 57 (10%); Largest: mutating_test.go (2768L), monitoring_test.go (2214L), test_context_test.go (2109L) |
| Generated Code Ratio | Navigate | 2% | 100 | 15/574 files are generated (3%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Go lockfile; Build/install targets in Makefile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 124 direct dependencies / 559 source files (ratio: 0.22) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), OWNERS_ALIASES present |
| Test-to-Source Ratio | Verify | 15% | 70 | 196 test files / 363 source files (ratio: 0.54) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, unit-test, e2e-test, e2e-test, unit-test-cli; Multiple test types available |
| Coverage Configuration | Verify | 3% | 100 | Codecov configured; Go coverage flags in Makefile; Coverage in CI workflow: security-full-scan.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): test-gateway-integration.yaml, test-unit.yaml, test-unit-cli.yaml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: security-full-scan.yml, test-linter.yaml |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~54% unit tests, ~46% infra-dependent (15/28 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### mlflow -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (6) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (7 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 78 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: tests/data, examples (378 files) |
| Code Navigability | Navigate | 5% | 50 | Average file: 321 lines (4227 source files, generated excluded); Files >500 lines: 418 (10%); Largest: Service.java (274253L), ModelRegistry.java (53284L), DatabricksArtifacts.java (23030L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/4419 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Java; mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 157 direct dependencies / 4419 source files (ratio: 0.04) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 8 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 1432 test files / 2987 source files (ratio: 0.48) |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 14 CI workflow(s): typescript.yml, lint.yml, uc-oss.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: lint.yml, docs.yml, copilot-setup-steps.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### trainer -- 69/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (5 files) |
| Architecture Documentation | Understand | 3% | 30 | 16 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (11 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 142 lines (538 source files, generated excluded); Files >500 lines: 16 (3%); Largest: framework_test.go (2625L), trainingruntime_test.go (1865L), progression_test.go (1764L) |
| Generated Code Ratio | Navigate | 2% | 80 | 34/576 files are generated (6%); Examples: clientset.go, register.go, doc.go, register.go, clientset_generated.go |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Go lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go, Rust |
| Dependency Complexity | Navigate | 2% | 90 | 85 direct dependencies / 542 source files (ratio: 0.16) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 14 entries |
| Test-to-Source Ratio | Verify | 15% | 25 | 66 test files / 476 source files (ratio: 0.14) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, test-integration, test-e2e; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): test-rust.yaml, test-go.yaml, test-e2e.yaml |
| PR Template | Submit | 2% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: test-go.yaml, test-python.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 100 | ~89% unit tests, ~11% infra-dependent (25/28 sampled); Makefile separates unit and integration test targets |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### trainer-sdk -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (5 files) |
| Architecture Documentation | Understand | 3% | 30 | 10 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (4 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 119 lines (474 source files, generated excluded); Files >500 lines: 9 (2%); Largest: torch_test.go (1350L), wrapper.go (1191L), framework_test.go (1176L) |
| Generated Code Ratio | Navigate | 2% | 80 | 32/513 files are generated (6%); Examples: clientset.go, register.go, doc.go, register.go, clientset_generated.go |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Go lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 80 direct dependencies / 481 source files (ratio: 0.17) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 13 entries |
| Test-to-Source Ratio | Verify | 15% | 25 | 45 test files / 436 source files (ratio: 0.10) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, test-integration, test-e2e; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test-go.yaml, test-e2e.yaml, test-python.yaml |
| PR Template | Submit | 2% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: test-go.yaml, test-python.yaml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~93% unit tests, ~7% infra-dependent (27/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### kubeflow-sdk -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 55 | Found: .github/ISSUE_TEMPLATE/bug_report.yaml; Has environment/version fields; YAML template with required fields *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (13 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 7 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 80 | Fixture directories: examples (8 files) |
| Code Navigability | Navigate | 5% | 30 | Average file: 314 lines (100 source files, generated excluded); Files >500 lines: 21 (21%); Largest: transformers_test.py (4297L), transformers.py (1777L), backend_test.py (1689L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/111 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (6/20 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 90 | 22 direct dependencies / 111 source files (ratio: 0.20) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 7 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 30 test files / 81 source files (ratio: 0.37) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: verify; pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 100 | Go coverage flags in Makefile; Coverage in CI workflow: test-python.yaml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): test-e2e.yaml, test-python.yaml, test-spark-examples.yaml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~89% unit tests, ~11% infra-dependent (25/28 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### odh-cli -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 64 | CLAUDE.md found (1/7 quality keywords); claude.md found (1/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (6/50 sampled files); Error wrapping patterns (17 files) |
| Architecture Documentation | Understand | 3% | 40 | Architecture doc: docs/design.md *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 5/20 sampled test files |
| Code Navigability | Navigate | 5% | 90 | Average file: 187 lines (239 source files, generated excluded); Files >500 lines: 12 (5%); Largest: impacted.go (1463L), impacted_test.go (1328L), impacted_test.go (1058L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/239 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 91 direct dependencies / 239 source files (ratio: 0.38) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 70 | 85 test files / 154 source files (ratio: 0.55) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: check, test |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: docs/development.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~90% unit tests, ~10% infra-dependent (27/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### rhaii-cluster-validation -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (6/7 quality keywords); claude.md found (6/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (6/34 sampled files); Error wrapping patterns (11 files) |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (1 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 119 lines (34 source files, generated excluded); Files >500 lines: 1 (3%); Largest: controller.go (723L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/34 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 41 direct dependencies / 34 source files (ratio: 1.21) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 15 test files / 19 source files (ratio: 0.79) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yaml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~93% unit tests, ~7% infra-dependent (14/15 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### model-registry-bf4-kf -- 68/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (6/50 sampled files); Error wrapping patterns (10 files) |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 5/17 sampled test files |
| Code Navigability | Navigate | 5% | 70 | Average file: 236 lines (60 source files, generated excluded); Files >500 lines: 7 (12%); Largest: core_test.go (3381L), core.go (1466L), api_model_registry_service.go (952L) |
| Generated Code Ratio | Navigate | 2% | 20 | 63/123 files are generated (51%); Examples: model_base_execution.go, model_base_execution_create.go, model_metadata_struct_value.go, model_base_resource_update.go, model_metadata_value.go *Rec: Add '// Code generated' headers to generated files and document which files are auto-generated in CLAUDE.md.* |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 68 direct dependencies / 60 source files (ratio: 1.13) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 17 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 17 test files / 43 source files (ratio: 0.40) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 100 | Go coverage flags in Makefile; Coverage in CI workflow: python-tests.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): python-tests.yml, build.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~88% unit tests, ~12% infra-dependent (15/17 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### llama-stack-k8s-operator -- 67/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (4) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (19/44 sampled files); Error wrapping patterns (17 files) |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 50 | Average file: 266 lines (49 source files, generated excluded); Files >500 lines: 10 (20%); Largest: llamastackdistribution_controller.go (1927L), resource_helper_test.go (1056L), llamastackdistribution_controller_test.go (990L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 1/50 files are generated (2%); Examples: zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 70 direct dependencies / 49 source files (ratio: 1.43) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 85 | 23 test files / 26 source files (ratio: 0.88) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test, test-e2e |
| Coverage Configuration | Verify | 3% | 100 | Go coverage flags in Makefile; Coverage in CI workflow: code-coverage.yml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): run-e2e-test.yml, generate-release.yml, code-coverage.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: pre-commit.yml, generate-release.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 50 | ~45% unit tests, ~55% infra-dependent (9/20 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 70 | .pre-commit-config.yaml found |

### odh-model-controller -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (21/50 sampled files); Error wrapping patterns (17 files) |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 80 | Fixture directories: test/data (7 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 202 lines (129 source files, generated excluded); Files >500 lines: 10 (8%); Largest: configmap_handler_test.go (999L), inferenceservice_controller_test.go (954L), llm_inferenceservice_controller_test.go (941L) |
| Generated Code Ratio | Navigate | 2% | 100 | 1/130 files are generated (1%); Examples: zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 100 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 167 direct dependencies / 129 source files (ratio: 1.29) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 34 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 42 test files / 87 source files (ratio: 0.48) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test, test-e2e |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): test.yml, test-e2e.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started, Develop, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~67% unit tests, ~33% infra-dependent (20/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### model-metadata-collection -- 66/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (7/7 quality keywords); claude.md found (7/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (8/30 sampled files); Error wrapping patterns (12 files) |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 50 | Average file: 368 lines (31 source files, generated excluded); Files >500 lines: 8 (26%); Largest: catalog_test.go (1396L), main.go (853L), registry_test.go (848L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/31 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 70 | 29 direct dependencies / 31 source files (ratio: 0.94) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 12 test files / 19 source files (ratio: 0.63) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test, check |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build-and-push-static-model-catalog-data.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Build, Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~92% unit tests, ~8% infra-dependent (11/12 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### codeflare-operator -- 65/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (4/18 sampled files); Error wrapping patterns (2 files) |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 224 lines (22 source files, generated excluded); Files >500 lines: 3 (14%); Largest: raycluster_webhook_test.go (880L), raycluster_controller.go (713L), mnist_rayjob_raycluster_test.go (559L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/22 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 10 | 92 direct dependencies / 22 source files (ratio: 4.18) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 31 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 9 test files / 13 source files (ratio: 0.69) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test-unit, test-e2e |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): unit_tests.yml, odh-release.yml, component_tests.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: precommit.yml, unit_tests.yml, tag-and-build.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 30 | ~12% unit tests, ~88% infra-dependent (1/8 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### codeflare-operator-poc -- 65/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (4/18 sampled files); Error wrapping patterns (2 files) |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 225 lines (22 source files, generated excluded); Files >500 lines: 4 (18%); Largest: raycluster_webhook_test.go (880L), raycluster_controller.go (713L), mnist_rayjob_raycluster_test.go (559L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/22 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 10 | 95 direct dependencies / 22 source files (ratio: 4.32) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 31 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 9 test files / 13 source files (ratio: 0.69) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test-unit, test-e2e |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): unit_tests.yml, odh-release.yml, component_tests.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: precommit.yml, unit_tests.yml, tag-and-build.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 30 | ~12% unit tests, ~88% infra-dependent (1/8 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### llm-d-kv-cache -- 64/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (17/50 sampled files); Error wrapping patterns (14 files) |
| Architecture Documentation | Understand | 3% | 70 | Architecture doc: docs/architecture.md; 16 module-level READMEs |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (22 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 177 lines (111 source files, generated excluded); Files >500 lines: 4 (4%); Largest: e2e_test.go (915L), cgo_functions_test.go (810L), cgo_functions.c (591L) |
| Generated Code Ratio | Navigate | 2% | 100 | 4/115 files are generated (3%); Examples: tokenizer_grpc.pb.go, tokenizer.pb.go, indexer_grpc.pb.go, indexer.pb.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go, C++ |
| Dependency Complexity | Navigate | 2% | 50 | 122 direct dependencies / 111 source files (ratio: 1.10) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (CODEOWNERS) with 4 rules |
| Test-to-Source Ratio | Verify | 15% | 50 | 29 test files / 82 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, unit-test, e2e-test, kv_connectors/llmd_fs_backend/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci-pr-checks.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci-pr-checks.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~89% unit tests, ~11% infra-dependent (24/27 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### training-notebooks -- 64/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (16 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 12 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (2 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 188 lines (116 source files, generated excluded); Files >500 lines: 17 (15%); Largest: konflux_generate_component_build_pipelines.py (863L), bootstrapper.py (769L), bootstrapper.py (769L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/119 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 17 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 29 test files / 90 source files (ratio: 0.32) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 70 | pytest.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): build-notebooks-TEMPLATE.yaml, code-quality.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: pr-merge-image-delete.yml, auto-add-issue-to-project.yml, sec-scan.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~79% unit tests, ~21% infra-dependent (23/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### modelmesh-runtime-adapter -- 64/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (29/50 sampled files); Error wrapping patterns (26 files) |
| Architecture Documentation | Understand | 3% | 30 | 6 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 158 lines (90 source files, generated excluded); Files >500 lines: 6 (7%); Largest: adaptmodellayout_test.go (1246L), adaptmodellayout_test.go (652L), puller_test.go (637L) |
| Generated Code Ratio | Navigate | 2% | 60 | 26/116 files are generated (22%); Examples: mock_provider_test.go, mock_triton_server.go, mock_triton.go, model_config.pb.go, triton_grpc.pb.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 50 | 97 direct dependencies / 90 source files (ratio: 1.08) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 25 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 27 test files / 63 source files (ratio: 0.43) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, model-serving-puller/test, model-mesh-mlserver-adapter/test, model-mesh-triton-adapter/test, model-mesh-ovms-adapter/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 2% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (29/29 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### MLServer -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (2 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 54 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: tests/testdata (26 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 110 lines (344 source files, generated excluded); Files >500 lines: 6 (2%); Largest: generate-pinned-requirements.py (1053L), test_pandas.py (744L), test_base.py (673L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/371 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Poetry lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), OWNERS_ALIASES present |
| Test-to-Source Ratio | Verify | 15% | 85 | 143 test files / 228 source files (ratio: 0.63) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test; pytest configured in pyproject.toml; tox.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): tests.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: tests.yml |
| Contributing / Dev Guide | Submit | 5% | 80 | Found: CONTRIBUTING.md; 3/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### langfuse -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (6/7 quality keywords); claude.md found (6/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 80 | Found: .github/ISSUE_TEMPLATE/bug_report.yml; Has reproduction steps; Has environment/version fields; YAML template with required fields |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (10 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 33 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 224 lines (2096 source files, generated excluded); Files >500 lines: 197 (9%); Largest: root.ts (16411L), otelMapping.servertest.ts (6754L), queryBuilder.servertest.ts (4826L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/2097 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: pnpm lockfile; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 30 | CODEOWNERS found (.github/CODEOWNERS) but empty *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 191 test files / 1906 source files (ratio: 0.10); Frontend-heavy repo (relaxed thresholds) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): pipeline.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: sdk-api-spec.yml, pipeline.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | Husky git hooks configured; .husky/ directory found |

### kueue -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 70 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has environment/version fields |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (9/50 sampled files); Error wrapping patterns (6 files) |
| Architecture Documentation | Understand | 3% | 30 | 47 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (44 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 294 lines (633 source files, generated excluded); Files >500 lines: 88 (14%); Largest: scheduler_test.go (7541L), pod_controller_test.go (5833L), cache_test.go (3920L) |
| Generated Code Ratio | Navigate | 2% | 80 | 88/721 files are generated (12%); Examples: clientset.go, register.go, doc.go, register.go, clientset_generated.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 90 | 145 direct dependencies / 633 source files (ratio: 0.23) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 18 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 240 test files / 393 source files (ratio: 0.61) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: verify |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 60 | CI runs tests (but may not trigger on PRs); Tests found in 1 CI workflow(s): odh-release.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~68% unit tests, ~32% infra-dependent (17/25 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llama-stack -- 62/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (5) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (7 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 21 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 6/20 sampled test files |
| Code Navigability | Navigate | 5% | 70 | Average file: 166 lines (1072 source files, generated excluded); Files >500 lines: 75 (7%); Largest: test_openai_vector_stores.py (5660L), ifeval_utils.py (3319L), test_openai_responses.py (3311L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/1072 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 12 direct dependencies / 1072 source files (ratio: 0.01) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 50 | 254 test files / 818 source files (ratio: 0.31) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 80 | Python coverage config; Coverage in CI workflow: codeql.yml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 8 CI workflow(s): release-branch-scheduled-ci.yml, record-integration-tests.yml, integration-vector-io-tests.yml |
| PR Template | Submit | 2% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: pre-commit.yml, post-release.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 6/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (26/26 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### base-containers -- 61/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords); AGENTS.md found (5/7 quality keywords); Agents.md found (5/7 quality keywords); agents.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/4 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 191 lines (9 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/9 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 4 test files / 5 source files (ratio: 0.80) |
| One-Command Test Execution | Verify | 11% | 60 | tox.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): ci.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: docs/development.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (4/4 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### kube-authkit -- 61/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (8 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 3/14 sampled test files |
| Code Navigability | Navigate | 5% | 70 | Average file: 280 lines (26 source files, generated excluded); Files >500 lines: 3 (12%); Largest: test_oidc.py (1181L), oidc.py (643L), test_factory.py (518L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/26 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 8/12 sampled Python files |
| Dependency Complexity | Navigate | 2% | 90 | 4 direct dependencies / 26 source files (ratio: 0.15) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 100 | 14 test files / 12 source files (ratio: 1.17) |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 80 | Coverage in CI workflow: test.yml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): publish.yml, test.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~71% unit tests, ~29% infra-dependent (10/14 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### model-registry-operator -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 85 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (16/38 sampled files); Error wrapping patterns (15 files) |
| Architecture Documentation | Understand | 3% | 30 | 3 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 260 lines (47 source files, generated excluded); Files >500 lines: 6 (13%); Largest: modelcatalog_controller_test.go (1436L), modelregistry_controller_test.go (1332L), modelcatalog_controller.go (1293L) |
| Generated Code Ratio | Navigate | 2% | 80 | 3/50 files are generated (6%); Examples: zz_generated.deepcopy.go, zz_generated.conversion.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 30 | 121 direct dependencies / 47 source files (ratio: 2.57) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 13 test files / 34 source files (ratio: 0.38) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started, Build, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~54% unit tests, ~46% infra-dependent (7/13 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### caikit-nlp -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (9/50 sampled files); Error wrapping patterns (8 files) |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: tests/fixtures, examples (31 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 225 lines (71 source files, generated excluded); Files >500 lines: 9 (13%); Largest: peft_prompt_tuning.py (1241L), embedding.py (1226L), test_embedding.py (1145L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/79 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dockerfile/Containerfile for reproducible builds *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (4/20 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 90 | 1 direct dependencies / 79 source files (ratio: 0.01) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 70 | 27 test files / 52 source files (ratio: 0.52) |
| One-Command Test Execution | Verify | 11% | 60 | tox.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): publish-library.yml, build-library.yml, lint-code.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (27/27 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### trustyai-explainability -- 60/100 (Partially Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 8 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 146 lines (709 source files, generated excluded); Files >500 lines: 30 (4%); Largest: ModelInferRequest.java (5632L), ModelInferResponse.java (4037L), ModelMetadataResponse.java (3177L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/710 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dockerfile/Containerfile for reproducible builds *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Java |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 70 | 238 test files / 472 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: tests/test; Maven build found with test files |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yaml |
| PR Template | Submit | 2% | 55 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Has checklist items *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### models-as-a-service -- 59/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Good logging coverage (17/50 sampled files); Error wrapping patterns (23 files) |
| Architecture Documentation | Understand | 3% | 30 | 14 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 248 lines (121 source files, generated excluded); Files >500 lines: 16 (13%); Largest: test_subscription.py (1982L), deploy.sh (1655L), test_models_endpoint.py (1431L) |
| Generated Code Ratio | Navigate | 2% | 100 | 2/123 files are generated (2%); Examples: store_mock.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 34 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 44 test files / 77 source files (ratio: 0.57) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: maas-controller/test, maas-api/test |
| Coverage Configuration | Verify | 3% | 60 | Coverage in CI workflow: maas-api-ci.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): maas-api-ci.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: maas-api-ci.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~75% unit tests, ~25% infra-dependent (21/28 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### elyra -- 59/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (3) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (9/50 sampled files); Error wrapping patterns (11 files) |
| Architecture Documentation | Understand | 3% | 30 | 12 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 2/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 210 lines (259 source files, generated excluded); Files >500 lines: 29 (11%); Largest: test_processor_kfp.py (1883L), test_metadata_app.py (1785L), test_pipeline_app.py (1401L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/272 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Yarn lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 60 | tsconfig.json found (strict mode not enabled); Some type annotations (5/20 sampled) |
| Dependency Complexity | Navigate | 2% | 90 | 25 direct dependencies / 272 source files (ratio: 0.09) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 71 test files / 201 source files (ratio: 0.35) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test-integration, test; pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 80 | Coverage-related target in Makefile; Coverage in CI workflow: build.yml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: build.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | Husky git hooks configured |

### rest-proxy -- 59/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (5/6 sampled files); Error wrapping patterns (3 files) |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 170 lines (8 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 60 | 3/11 files are generated (27%); Examples: grpc_predict_v2.pb.gw.go, grpc_predict_v2_grpc.pb.go, grpc_predict_v2.pb.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 30 | 29 direct dependencies / 8 source files (ratio: 3.62) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 27 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 2 test files / 6 source files (ratio: 0.33) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: test |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: test.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### kubeflow -- 58/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Good logging coverage (22/50 sampled files); Error wrapping patterns (15 files) |
| Architecture Documentation | Understand | 3% | 30 | 9 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 276 lines (61 source files, generated excluded); Files >500 lines: 11 (18%); Largest: notebook_controller_test.go (1971L), notebook_webhook.go (894L), notebook_dspa_secret_test.go (888L) |
| Generated Code Ratio | Navigate | 2% | 100 | 3/64 files are generated (5%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 22 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 20 test files / 41 source files (ratio: 0.49) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: components/odh-notebook-controller/test, components/odh-notebook-controller/e2e-test, components/notebook-controller/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 60 | Coverage in CI workflow: notebook_controller_unit_test.yaml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): notebook_controller_unit_test.yaml, odh_notebook_controller_unit_test.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: code-quality.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~69% unit tests, ~31% infra-dependent (11/16 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### mcp-server-operator -- 58/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (3/13 sampled files); Error wrapping patterns (2 files) |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 212 lines (14 source files, generated excluded); Files >500 lines: 1 (7%); Largest: mcpserver_test.go (1132L) |
| Generated Code Ratio | Navigate | 2% | 80 | 1/15 files are generated (7%); Examples: zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 100 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 10 | 90 direct dependencies / 14 source files (ratio: 6.43) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 70 | 5 test files / 9 source files (ratio: 0.56) |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test, test-e2e |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~75% unit tests, ~25% infra-dependent (3/4 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### caikit-nlp-client -- 58/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (2/19 sampled files); Error wrapping patterns (7 files) |
| Architecture Documentation | Understand | 3% | 30 | 3 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: tests/fixtures, examples (21 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 151 lines (18 source files, generated excluded); Files >500 lines: 1 (6%); Largest: http_client.py (541L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/19 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (4/10 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 90 | 3 direct dependencies / 19 source files (ratio: 0.16) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 9 test files / 10 source files (ratio: 0.90) |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml; noxfile.py found |
| Coverage Configuration | Verify | 3% | 80 | Coverage in CI workflow: tests-docker.yml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): release.yml, tests-docker.yml, tests.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: tests.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (9/9 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### trustyai-service-operator -- 57/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (zap) found in go.mod; Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Some logging (15/50 sampled files); Error wrapping patterns (12 files) |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 247 lines (133 source files, generated excluded); Files >500 lines: 16 (12%); Largest: lmevaljob_controller_test.go (4373L), unit_test.go (2137L), lmevaljob_controller_validation_test.go (1798L) |
| Generated Code Ratio | Navigate | 2% | 100 | 6/139 files are generated (4%); Examples: zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go, zz_generated.deepcopy.go |
| Build / Dependency Setup | Navigate | 5% | 90 | Lockfiles: Go lockfile; Build/install targets in Makefile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 70 | 120 direct dependencies / 133 source files (ratio: 0.90) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 34 test files / 99 source files (ratio: 0.34) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 90 | Makefile targets: test, tests/test |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): controller-tests.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint-yaml.yaml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~63% unit tests, ~37% infra-dependent (19/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### elyra-pipeline-editor -- 55/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (20 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 220 lines (102 source files, generated excluded); Files >500 lines: 7 (7%); Largest: index.ts (5335L), common-canvas.d.ts (3011L), index.test.ts (1395L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/102 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Yarn lockfile; Build/install targets in Makefile |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 70 | 22 test files / 80 source files (ratio: 0.28); Frontend-heavy repo (relaxed thresholds) |
| One-Command Test Execution | Verify | 11% | 80 | npm test script defined |
| Coverage Configuration | Verify | 3% | 60 | Coverage in CI workflow: build.yaml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): build.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (22/22 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | Husky git hooks configured |

### mlflow-go -- 55/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Good logging coverage (11/25 sampled files); Error wrapping patterns (6 files) |
| Architecture Documentation | Understand | 3% | 45 | ADR directory: docs/adr (11 records); 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: testdata (1 files) |
| Code Navigability | Navigate | 5% | 50 | Average file: 328 lines (27 source files, generated excluded); Files >500 lines: 7 (26%); Largest: client_test.go (1175L), client_test.go (1148L), client.go (767L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 60 | 6/33 files are generated (18%); Examples: databricks.pb.go, model_registry.pb.go, service.pb.go, assessments.pb.go, datasets.pb.go |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Go lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 70 | 9 test files / 18 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: check |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): go.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: go.yaml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~86% unit tests, ~14% infra-dependent (6/7 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### odh-ide-extensions -- 53/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (3/22 sampled files); Error wrapping patterns (1 files) |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 27 lines (23 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/23 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: npm lockfile, Yarn lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 90 | 2 direct dependencies / 23 source files (ratio: 0.09) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 12 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 6 test files / 17 source files (ratio: 0.35); Frontend-heavy repo (relaxed thresholds) |
| One-Command Test Execution | Verify | 11% | 80 | npm test script defined |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): build_extension.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 40 | Lint targets in Makefile (but not confirmed in CI) *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop, Getting Started, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (6/6 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | Husky git hooks configured |

### vllm-tgis-adapter -- 53/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (13 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 80 | Fixture directories: tests/fixtures, examples (9 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 143 lines (31 source files, generated excluded); Files >500 lines: 1 (3%); Largest: grpc_server.py (994L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/33 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 9 direct dependencies / 33 source files (ratio: 0.27) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 31 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 8 test files / 25 source files (ratio: 0.32) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml; noxfile.py found |
| Coverage Configuration | Verify | 3% | 80 | Coverage in CI workflow: tests.yaml; Coverage config in pyproject.toml; Multiple coverage signals detected |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): tests.yaml, release.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit-autoupdate.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (8/8 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### batch-gateway -- 52/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Good logging coverage (20/50 sampled files); Error wrapping patterns (19 files) |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 186 lines (57 source files, generated excluded); Files >500 lines: 3 (5%); Largest: client_test.go (1103L), file_handler_test.go (701L), file_handler.go (653L) |
| Generated Code Ratio | Navigate | 2% | 80 | 5/62 files are generated (8%); Examples: mock_files_client.go, mock_event_client.go, mock_status_client.go, mock_db_client.go, mock_queue_client.go |
| Build / Dependency Setup | Navigate | 5% | 80 | Lockfiles: Go lockfile; Build/install targets in Makefile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 70 | 45 direct dependencies / 57 source files (ratio: 0.79) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 14 entries |
| Test-to-Source Ratio | Verify | 15% | 50 | 12 test files / 45 source files (ratio: 0.27) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, check, test-integration; Multiple test types available |
| Coverage Configuration | Verify | 3% | 80 | Go coverage flags in Makefile |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~92% unit tests, ~8% infra-dependent (11/12 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### openvino -- 52/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (7) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 81 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: samples (140 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 167 lines (10205 source files, generated excluded); Files >500 lines: 579 (6%); Largest: convolution_gpu_test.cpp (11196L), caffe_pb2.py (9544L), deformable_convolution.cpp (7789L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/10247 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): C++, C |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 91 rules |
| Test-to-Source Ratio | Verify | 15% | 85 | 4667 test files / 5580 source files (ratio: 0.84) |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 60 | Coverage in CI workflow: coverage.yml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 12 CI workflow(s): job_tensorflow_models_tests.yml, job_tensorflow_layer_tests.yml, job_python_api_tests.yml |
| PR Template | Submit | 2% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: py_checks.yml |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llama-stack-provider-ragas -- 50/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (4 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 3/4 sampled test files |
| Code Navigability | Navigate | 5% | 90 | Average file: 105 lines (22 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/24 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: npm lockfile, uv lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 50 | 32 direct dependencies / 24 source files (ratio: 1.33) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 4 test files / 20 source files (ratio: 0.20) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 60 | Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ci.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (4/4 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### openvino_model_server -- 49/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (5 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 66 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 2/20 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 267 lines (611 source files, generated excluded); Files >500 lines: 72 (12%); Largest: ensemble_tests.cpp (6409L), ensemble_flow_custom_node_tests.cpp (5967L), llmnode_test.cpp (4131L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/611 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Yarn lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): C++, Go, Java, C |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 17 entries |
| Test-to-Source Ratio | Verify | 15% | 70 | 222 test files / 389 source files (ratio: 0.57) |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 50 | Coverage-related target in Makefile *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): integration-tests-konflux.yml, integration-tests.yml, fast-checks.yml |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: docs/CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### openvino.genai -- 48/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (7/50 sampled files); Error wrapping patterns (16 files) |
| Architecture Documentation | Understand | 3% | 30 | 24 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: samples (139 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 217 lines (498 source files, generated excluded); Files >500 lines: 48 (10%); Largest: test_vlm_pipeline.py (1927L), adapter.cpp (1771L), classes.cpp (1532L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/501 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): C++, C |
| Dependency Complexity | Navigate | 2% | 90 | 1 direct dependencies / 501 source files (ratio: 0.00) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 25 rules |
| Test-to-Source Ratio | Verify | 15% | 50 | 97 test files / 404 source files (ratio: 0.24) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 5 CI workflow(s): windows.yml, manylinux_2_28.yml, sdl.yml |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: lint.yml, sdl.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting Started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### distributed-workloads -- 46/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 90 | Go structured logging (logr) found in go.mod; Kubernetes-style logging (klog) found in go.mod; Error wrapping patterns (10 files) |
| Architecture Documentation | Understand | 3% | 30 | 29 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (141 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 153 lines (130 source files, generated excluded); Files >500 lines: 7 (5%); Largest: rhai_features_tests.go (1059L), prestage_models_datasets.py (852L), ray_finetune_llm_deepspeed.py (743L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/130 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Go lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 70 | 78 direct dependencies / 130 source files (ratio: 0.60) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), OWNERS_ALIASES present |
| Test-to-Source Ratio | Verify | 15% | 100 | 97 test files / 33 source files (ratio: 2.94) |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 70 | CI has PR triggers and test steps, but in separate workflows; Tests found in 1 CI workflow(s): odh-release.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 50 | ~40% unit tests, ~60% infra-dependent (12/30 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### fms-guardrails-orchestrator -- 46/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 100 | Found: .github/ISSUE_TEMPLATE/bug_report.md; Has reproduction steps; Has expected/actual behavior fields; Has environment/version fields; Has log/error output fields |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 30 | Average file: 495 lines (77 source files, generated excluded); Files >500 lines: 17 (22%); Largest: chat_completions_streaming.rs (5653L), completions_streaming.rs (4701L), remediation-script.sh (2127L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/77 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Cargo lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Rust |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 50 | 19 test files / 58 source files (ratio: 0.33) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): test.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (19/19 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 70 | .pre-commit-config.yaml found |

### guardrails-detectors -- 46/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 3 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 14/15 sampled test files |
| Code Navigability | Navigate | 5% | 70 | Average file: 154 lines (29 source files, generated excluded); Files >500 lines: 1 (3%); Largest: test_llm_judge_detector.py (588L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/34 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (9/19 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 85 | 15 test files / 19 source files (ratio: 0.79) |
| One-Command Test Execution | Verify | 11% | 60 | tox.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): test-llm-judge.yaml, test-huggingface-runtime.yaml, test-builtin-detectors.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (15/15 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llama-stack-client-python -- 46/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (8 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (3 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 148 lines (422 source files, generated excluded); Files >500 lines: 31 (7%); Largest: _base_client.py (1999L), test_client.py (1692L), response_object_stream.py (1550L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/423 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: uv lockfile; Dev container configuration |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 90 | 15 direct dependencies / 423 source files (ratio: 0.04) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 25 | 67 test files / 356 source files (ratio: 0.19) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~97% unit tests, ~3% infra-dependent (29/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### modelmesh -- 45/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 5 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 5/20 sampled test files |
| Code Navigability | Navigate | 5% | 50 | Average file: 443 lines (120 source files, generated excluded); Files >500 lines: 23 (19%); Largest: ModelMesh.java (7365L), LegacyModelMeshService.java (5330L), TasRuntimeOuterClass.java (4876L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/120 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dockerfile/Containerfile for reproducible builds *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Java |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 25 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 52 test files / 68 source files (ratio: 0.76) |
| One-Command Test Execution | Verify | 11% | 70 | Maven build found with test files |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~90% unit tests, ~10% infra-dependent (27/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### llama-stack-distribution -- 44/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 160 lines (7 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/7 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 3 rules |
| Test-to-Source Ratio | Verify | 15% | 85 | 3 test files / 4 source files (ratio: 0.75) |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): redhat-distro-container.yml |
| PR Template | Submit | 2% | 70 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~67% unit tests, ~33% infra-dependent (2/3 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### lm-evaluation-harness -- 44/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (6 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 122 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: tests/testdata, examples (712 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 153 lines (248 source files, generated excluded); Files >500 lines: 18 (7%); Largest: task.py (1721L), instructions_util.py (1696L), instructions_util.py (1696L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/254 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy.ini found |
| Dependency Complexity | Navigate | 2% | 90 | 20 direct dependencies / 254 source files (ratio: 0.08) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 25 | 17 test files / 237 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 60 | Python coverage config |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): unit_tests.yml, new_tasks.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: unit_tests.yml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: docs/CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (17/17 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### vllm-gaudi -- 42/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (10) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (12 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 7 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: tests/data, examples (79 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 256 lines (943 source files, generated excluded); Files >500 lines: 130 (14%); Largest: config.py (2413L), hpu_model_runner.py (2213L), llm_engine.py (2091L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/1025 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dockerfile/Containerfile for reproducible builds *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): C++; mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 1 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 70 | 342 test files / 683 source files (ratio: 0.50) |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 40 | PR template found: .github/PULL_REQUEST_TEMPLATE.md *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: ruff.yml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### data-processing -- 40/100 (Needs Work)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (8 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 6 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 156 lines (19 source files, generated excluded); Files >500 lines: 1 (5%); Largest: subset_selection.py (931L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/19 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 60 | CODEOWNERS found (.github/CODEOWNERS) with 2 rules (sparse) |
| Test-to-Source Ratio | Verify | 15% | 25 | 2 test files / 17 source files (ratio: 0.12) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 2 CI workflow(s): validate-notebooks.yml, execute-all-notebooks.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: validate-python.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (2/2 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### llama-stack-provider-trustyai-garak -- 39/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (14 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 3 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 2/10 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 30 | Average file: 354 lines (45 source files, generated excluded); Files >500 lines: 10 (22%); Largest: test_evalhub_adapter.py (2329L), garak_adapter.py (1383L), result_utils.py (1154L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/46 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dockerfile/Containerfile for reproducible builds *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (6/20 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 90 | 9 direct dependencies / 46 source files (ratio: 0.20) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 10 test files / 36 source files (ratio: 0.28) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | pytest configured in pyproject.toml |
| Coverage Configuration | Verify | 3% | 60 | Coverage config in pyproject.toml |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): run-tests.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (10/10 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### elyra-examples -- 38/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 100 | Good logging coverage (14/46 sampled files); Error wrapping patterns (8 files) |
| Architecture Documentation | Understand | 3% | 30 | 31 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/3 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 85 lines (46 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/46 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 25 | 3 test files / 43 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: component-catalog-connectors/artifactory-connector/test, component-catalog-connectors/kfp-example-components-connector/test, component-catalog-connectors/mlx-connector/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 85 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: build.yaml |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (3/3 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### rhaii-on-xks -- 37/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 12 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 220 lines (21 source files, generated excluded); Files >500 lines: 1 (5%); Largest: verify-llm-d-deployment.sh (2114L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/21 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 18 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 8 test files / 13 source files (ratio: 0.62) |
| One-Command Test Execution | Verify | 11% | 100 | Makefile targets: test, charts/cert-manager-operator/test, charts/sail-operator/test, charts/lws-operator/test; Multiple test types available |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 100 | Linting in CI: kserve-update-chart.yaml, kserve-ci.yaml, kserve-release.yaml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 30 | ~12% unit tests, ~88% infra-dependent (1/8 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### openvino_contrib -- 37/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 11 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 116 lines (432 source files, generated excluded); Files >500 lines: 8 (2%); Largest: convolution.cpp (8897L), group_convolution.cpp (822L), bidirectional_lstm_sequence_composition.cpp (755L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/434 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): C++, Java |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | CODEOWNERS found (.github/CODEOWNERS) with 7 rules |
| Test-to-Source Ratio | Verify | 15% | 50 | 107 test files / 327 source files (ratio: 0.33) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 4 CI workflow(s): windows.yml, token_merging.yml, linux.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: openvino_code.yml |
| Contributing / Dev Guide | Submit | 5% | 60 | Found: CONTRIBUTING.md; 1/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### perf_analyzer -- 37/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (2 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Factory/fixture patterns in 6/20 sampled test files |
| Code Navigability | Navigate | 5% | 90 | Average file: 94 lines (764 source files, generated excluded); Files >500 lines: 17 (2%); Largest: doctest.h (7824L), test_llm_profile_data_parser.py (1587L), test_cli.py (1579L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/765 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dev container configuration *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 25 | 69 test files / 696 source files (ratio: 0.10) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): python-package-genai.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (30/30 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### llama-stack-provider-kfp-trainer -- 34/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 69 lines (16 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/16 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 10 | Dockerfile/Containerfile for reproducible builds *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | mypy configured in pyproject.toml |
| Dependency Complexity | Navigate | 2% | 70 | 10 direct dependencies / 16 source files (ratio: 0.62) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 25 | 1 test files / 15 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | tox.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): lint.yml, test.yml, mypy.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (1/1 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### modelcar-base-image -- 33/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 22 lines (11 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/12 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: Go lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (1/4 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 3 test files / 9 source files (ratio: 0.33) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 80 | Makefile targets: python/test |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (3/3 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### caikit-tgis-serving -- 31/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 4 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 54 lines (29 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/29 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: Poetry lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 11 entries |
| Test-to-Source Ratio | Verify | 15% | 85 | 11 test files / 18 source files (ratio: 0.61) |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 100 | Found: CONTRIBUTING.md; 5/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~91% unit tests, ~9% infra-dependent (10/11 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### fips-compliance-checker-claude-code-plugin -- 30/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 88 | CLAUDE.md found (2/7 quality keywords); claude.md found (2/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 80 | Fixture directories: tests/fixtures (9 files) |
| Code Navigability | Navigate | 5% | 70 | Average file: 164 lines (13 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/13 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 1/1 sampled Python files |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 100 | 7 test files / 6 source files (ratio: 1.17) |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Build, Contribut *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (7/7 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### openvino_tokenizers -- 29/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (1) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (9 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 1/6 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 225 lines (54 source files, generated excluded); Files >500 lines: 7 (13%); Largest: tokenizer_pipeline.py (1623L), tokenizers_test.py (1114L), hf_parser.py (1088L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/55 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: Poetry lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): C++ |
| Dependency Complexity | Navigate | 2% | 90 | 2 direct dependencies / 55 source files (ratio: 0.04) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 25 | 6 test files / 49 source files (ratio: 0.12) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 3 CI workflow(s): windows.yml, linux.yml, mac.yml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build, Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (6/6 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### rag -- 27/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (10 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 13 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 194 lines (47 source files, generated excluded); Files >500 lines: 3 (6%); Largest: client.go (1581L), evaluation_utilities.py (900L), beir_benchmarks.py (619L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/47 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 100 | OWNERS file found (OpenShift/Kubernetes-style), 19 entries |
| Test-to-Source Ratio | Verify | 15% | 25 | 3 test files / 44 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 70 | ~67% unit tests, ~33% infra-dependent (2/3 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### llama-stack-demos -- 27/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (12 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 10 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 148 lines (60 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/62 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 10/20 sampled Python files |
| Dependency Complexity | Navigate | 2% | 90 | 10 direct dependencies / 62 source files (ratio: 0.16) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 11 test files / 51 source files (ratio: 0.22) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yaml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 50 | ~45% unit tests, ~55% infra-dependent (5/11 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 70 | .pre-commit-config.yaml found |

### client -- 24/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (2 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 5 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 209 lines (109 source files, generated excluded); Files >500 lines: 9 (8%); Largest: _client.py (1936L), _client.py (1659L), __init__.py (810L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/109 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Java |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 10 | 5 test files / 104 source files (ratio: 0.05) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: contribut, CONTRIBUT, Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (5/5 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 100 | .pre-commit-config.yaml found; Includes both linting and type/test hooks |

### ai-helpers -- 21/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (3/7 quality keywords); claude.md found (3/7 quality keywords); AGENTS.md found (3/7 quality keywords); Agents.md found (3/7 quality keywords); agents.md found (3/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 15 | Issue templates exist (7) but no dedicated bug template *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (5 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 5 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 296 lines (18 source files, generated excluded); Files >500 lines: 2 (11%); Largest: compare_reqs.py (523L), env_finder.py (515L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/18 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 30 | Build/install targets in Makefile; Dev container configuration *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 12/14 sampled Python files |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 18 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: lint.yml |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Setup *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 70 | .pre-commit-config.yaml found |

### ml-metadata -- 19/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (9 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 1 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 40 | Some fixture patterns in 2/13 sampled test files *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 30 | Average file: 332 lines (64 source files, generated excluded); Files >500 lines: 14 (22%); Largest: metadata_store_test.py (2631L), metadata_store.py (2012L), types.py (1578L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/64 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 13 test files / 51 source files (ratio: 0.25) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 50 | Found: CONTRIBUTING.md; 0/6 development keywords *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (13/13 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### odh-s2i-project-cds -- 19/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 50 lines (7 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/15 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 90 | 2 direct dependencies / 15 source files (ratio: 0.13) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 25 | 1 test files / 14 source files (ratio: 0.07) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 60 | tox.ini found |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (1/1 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llama-stack-provider-kft -- 15/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 94 lines (8 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/9 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: uv lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (2/9 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 50 | 17 direct dependencies / 9 source files (ratio: 1.89) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 9 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### vllm-orchestrator-gateway -- 14/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 50 | Average file: 228 lines (4 source files, generated excluded); Files >500 lines: 1 (25%); Largest: main.rs (547L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/4 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 70 | Lockfiles: Cargo lockfile; Dockerfile/Containerfile for reproducible builds |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Rust |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 4 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 100 | CI runs tests on pull requests; Tests found in 1 CI workflow(s): tests.yaml |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Getting started *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llama-stack-provider-instructlab-train -- 14/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 56 lines (4 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/4 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: uv lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (1/4 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 30 | 16 direct dependencies / 4 source files (ratio: 4.00) *Rec: Consider reducing direct dependencies or documenting key dependencies to help AI agents understand the project's dependency surface.* |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 4 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: pre-commit.yml |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 90 | .pre-commit-config.yaml found; Includes linting hooks |

### odh-s2i-project-cookiecutter -- 13/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 40 lines (5 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/5 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 70 | 4 direct dependencies / 5 source files (ratio: 0.80) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 50 | 1 test files / 4 source files (ratio: 0.25) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 90 | ~100% unit tests, ~0% infra-dependent (1/1 sampled) |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### agents -- 12/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 70 | Some logging (4/37 sampled files); Error wrapping patterns (10 files) |
| Architecture Documentation | Understand | 3% | 60 | ADR directory: adr (3 records); 26 module-level READMEs |
| Test Fixtures / Sample Data | Understand | 2% | 90 | Fixture directories: examples (92 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 141 lines (40 source files, generated excluded); Files >500 lines: 1 (2%); Largest: nps_mcp_server.py (757L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/41 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 80 | Statically typed language(s): Go |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 25 | 3 test files / 38 source files (ratio: 0.08) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 50 | ~33% unit tests, ~67% infra-dependent (1/3 sampled) *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### odh-gitops -- 10/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 15 | 2 module-level README(s) *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 70 | Average file: 177 lines (14 source files, generated excluded); Files >500 lines: 1 (7%); Largest: extract-olm-bundle.sh (711L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/14 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 14 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 100 | PR template found: .github/PULL_REQUEST_TEMPLATE.md; Mentions testing; Has checklist items; Mentions review |
| Linting / Formatting in CI | Submit | 5% | 80 | Linting in CI: helm.yaml |
| Contributing / Dev Guide | Submit | 5% | 90 | Found: CONTRIBUTING.md; 4/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### opendatahub.io -- 9/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 97 lines (45 source files, generated excluded); Files >500 lines: 1 (2%); Largest: const.ts (845L) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/45 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 60 | Lockfiles: npm lockfile |
| Type Safety / Static Analysis | Navigate | 3% | 90 | TypeScript strict mode enabled |
| Dependency Complexity | Navigate | 2% | 90 | 22 direct dependencies / 45 source files (ratio: 0.49) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 45 source files (ratio: 0.00); Frontend-heavy repo (relaxed thresholds) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 70 | Found: CONTRIBUTING.md; 2/6 development keywords |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### opendatahub-documentation -- 9/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 100 | CLAUDE.md found (5/7 quality keywords); claude.md found (5/7 quality keywords) |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 60 | Fixture directories: examples (1 files) |
| Code Navigability | Navigate | 5% | 90 | Average file: 71 lines (3 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/3 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 3 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 30 | CI triggers on PRs but no test step found *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No linting in CI detected *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### llm-d-playbooks -- 4/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 15 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 109 lines (7 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/7 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 2/3 sampled Python files |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 7 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### model-runtimes-agent -- 4/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (1 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 50 | Average file: 304 lines (17 source files, generated excluded); Files >500 lines: 3 (18%); Largest: app.py (1708L), html_report.py (686L), accelerator_validator.py (574L) *Rec: Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.* |
| Generated Code Ratio | Navigate | 2% | 100 | 0/21 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 70 | Type annotations in 10/20 sampled Python files |
| Dependency Complexity | Navigate | 2% | 90 | 8 direct dependencies / 21 source files (ratio: 0.38) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 21 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Develop *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### odh-build-metadata -- 4/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 20 | Error wrapping patterns (3 files) *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 34199 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 68 lines (26121 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/26121 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 50 | Some type annotations (4/20 sampled) *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 26121 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### odh-s2i-project-simple -- 4/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 0 | No architecture documentation found *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 15 lines (3 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/3 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 70 | 2 direct dependencies / 3 source files (ratio: 0.67) |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 3 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 40 | README has development sections: Build *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

### dsp-dev-tools -- 4/100 (Not Ready)

| Check | Phase | Weight | Score | Evidence |
|---|---|---|---|---|
| AI Context Files | Understand | 8% | 0 | No AI context files found (CLAUDE.md, AGENTS.md, etc.) *Rec: Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.* |
| Bug Report Template Quality | Understand | 8% | 0 | No .github/ISSUE_TEMPLATE/ directory *Rec: Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.* |
| Structured Logging / Errors | Understand | 3% | 0 | No structured logging detected *Rec: Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python, Sentry for frontend) and wrap errors with context.* |
| Architecture Documentation | Understand | 3% | 30 | 8 module-level READMEs *Rec: Add architecture documentation (ARCHITECTURE.md, docs/design/, or module-level READMEs) to help AI agents understand codebase structure.* |
| Test Fixtures / Sample Data | Understand | 2% | 0 | No test fixtures or sample data found *Rec: Add test fixtures or sample data directories (testdata/, fixtures/, examples/) to help AI agents understand expected inputs and reproduce bugs.* |
| Code Navigability | Navigate | 5% | 90 | Average file: 48 lines (27 source files, generated excluded); Files >500 lines: 0 (0%) |
| Generated Code Ratio | Navigate | 2% | 100 | 0/27 files are generated (0%) |
| Build / Dependency Setup | Navigate | 5% | 0 | No dependency lockfiles or build configuration found *Rec: Add dependency lockfiles (go.sum, package-lock.json, poetry.lock) and a documented build setup to ensure reproducible builds.* |
| Type Safety / Static Analysis | Navigate | 3% | 0 | No type safety or static analysis configured *Rec: Enable type checking (mypy for Python, tsconfig strict for TypeScript) or add type annotations to help AI agents understand function contracts.* |
| Dependency Complexity | Navigate | 2% | 80 | No dependency manifest found or zero dependencies |
| Code Ownership (CODEOWNERS) | Submit | 1% | 0 | No CODEOWNERS or OWNERS file *Rec: Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.* |
| Test-to-Source Ratio | Verify | 15% | 0 | 0 test files / 27 source files (ratio: 0.00) *Rec: Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.* |
| One-Command Test Execution | Verify | 11% | 0 | No obvious one-command test execution found *Rec: Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.* |
| Coverage Configuration | Verify | 3% | 0 | No coverage configuration found *Rec: Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.* |
| CI Runs Tests on PRs | Verify | 10% | 0 | No .github/workflows/ directory *Rec: Ensure CI workflows triggered by pull_request events include a step that runs tests.* |
| PR Template | Submit | 2% | 0 | No PR template found *Rec: Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.* |
| Linting / Formatting in CI | Submit | 5% | 0 | No CI workflows *Rec: Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.* |
| Contributing / Dev Guide | Submit | 5% | 0 | No contributing/development guide found *Rec: Add CONTRIBUTING.md with build, test, and debug instructions.* |
| Test Isolation (unit vs e2e) | Verify | 4% | 0 | No test files found *Rec: Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.* |
| Pre-commit / Local Hooks | Verify | 3% | 0 | No pre-commit hooks or local validation configured *Rec: Add pre-commit hooks (.pre-commit-config.yaml, husky, lefthook) for fast local feedback on formatting and linting.* |

---
*AI Bug Automation Readiness Report -- Generated 2026-03-17 16:37*
