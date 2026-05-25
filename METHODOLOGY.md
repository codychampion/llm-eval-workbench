# Methodology

## Regulated Enterprise Model Readiness

`llm-eval-workbench` evaluates whether model-backed workflows behave reliably enough to support regulated enterprise use cases. It is designed for repeatable comparisons across models, providers, prompts, and evaluation strategies.

This benchmark uses benign synthetic or public-domain scenarios and does not attempt to elicit harmful operational content or bypass provider safeguards.

## Evaluation dimensions

| Dimension | What is measured |
|---|---|
| Capability | Completion of the requested task and required content. |
| Reliability | Format adherence, instruction stability, and repeatability. |
| Governance behavior | Risk classification, human-review routing, and policy-following behavior. |
| Groundedness | Whether responses remain bounded by provided evidence. |
| Security reasoning | Prompt-injection resilience, confidentiality handling, and access-control decisions. |
| Operations | Latency and estimated cost recorded alongside behavioral outcomes. |

## Starter suites

The public-safe `regulated_readiness_demo` suite includes:

- policy question answering
- RAG groundedness
- structured output and schema following
- prompt-injection resilience
- confidentiality handling
- access-control reasoning
- governance classification
- audit explanation quality

The deterministic `mock` adapter exists to test the evaluation pipeline and report shape. It is not a scored model comparison. Provider-backed model results should identify the model version, provider, run date, dataset version, and limitations.

## Scoring and evidence

Each evaluation case declares expected behavior, required evidence strings, prohibited strings, and a failure category. A run produces:

- case-level outputs and operational metrics
- aggregate pass rate
- explicit failure taxonomy counts
- Markdown and JSON artifacts for review

Current failure categories are:

- `unsafe_compliance`
- `over_refusal`
- `missing_evidence`
- `instruction_drift`
- `formatting_failure`
- `latency_regression`

## Connection to PAEF

PAEF introduced the atomic-evaluation pattern used here for regulated-enterprise model assessment: decompose complex governance or compliance tasks into policy-level checks, compare models and evaluation strategies, track uncertainty, and produce audit-ready diagnostics.

The PAEF evaluation study compares microagent-based atomic policy checks with monolithic LLM auditing across 193 service contracts and 7,913 labeled policy checks. See the [PAEF preprint](https://doi.org/10.5281/zenodo.19848867).

## Public leaderboard policy

A future public leaderboard will publish only benign evaluation scenarios and aggregate results. It should report:

- model and provider
- model version or date
- evaluation date
- scenario suite version
- capability, reliability, governance, and groundedness scores
- latency p50 and p95
- cost per 1,000 tasks and cost per successful task
- known limitations and regressions

Sensitive red-team work, proprietary data, harmful prompts, and unsafe outputs do not belong in the public benchmark.
