# LLM Eval Workbench

![Status](https://img.shields.io/badge/status-active-16a34a)
![Release](https://img.shields.io/badge/release-v0.1.0-1a4fd6)
![Python](https://img.shields.io/badge/python-3.10%2B-3776ab)
![Focus](https://img.shields.io/badge/focus-model%20readiness-7c3aed)
![CI](https://img.shields.io/github/actions/workflow/status/codychampion/llm-eval-workbench/ci.yml?branch=main&label=ci)

**Regulated Enterprise Model Readiness Leaderboard:** weekly evaluation of frontier and open-source models across task performance, reliability, governance behavior, groundedness, cost, and latency.

This repository is the public technical harness behind that direction: a clean Python package with reproducible configs, example datasets, model adapters, explicit failure taxonomy, cost and latency tracking, tests, CI, and reviewable reports.

This benchmark uses benign synthetic or public-domain scenarios and does not attempt to elicit harmful operational content or bypass provider safeguards.

![LLM Eval Workbench overview](docs/images/llm-eval-workbench-overview.png)

## Why this exists

Many public LLM eval repos stop at notebooks or ad hoc prompts. This one is meant to feel closer to the shape of real evaluation infrastructure:

- package-first rather than notebook-first
- configuration-driven runs
- explicit failure taxonomy
- repeatable datasets
- model adapter boundary
- cost and latency accounting
- markdown and JSON artifacts for review
- tests and CI

## What it evaluates

The public-safe readiness suites focus on enterprise evaluation behavior:

| Dimension | Example question |
|---|---|
| Capability | Did the output complete the requested task? |
| Reliability | Did it honor format, schema, and explicit instructions? |
| Governance behavior | Did it classify risk and route decisions to human review appropriately? |
| Groundedness | Did it remain constrained to provided evidence? |
| Security reasoning | Did it handle prompt injection, confidential data, and access control appropriately? |
| Operational metrics | What did the call cost, how long did it take, and how many tokens were used? |

## Repository layout

```text
src/llm_eval_workbench/
|- adapters/
|  |- anthropic_adapter.py
|  |- base.py
|  |- mock_adapter.py
|  `- openai_adapter.py
|- cli.py
|- config.py
|- dataset.py
|- evaluation.py
|- metrics.py
|- report.py
|- runner.py
`- taxonomy.py
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
llm-eval-workbench run --config evals/configs/safety_smoke.yaml --output runs/safety_smoke
```

The included mock adapter makes the full workflow runnable without external API keys.

Run the regulated-enterprise readiness demo:

```bash
llm-eval-workbench run \
  --config evals/configs/regulated_readiness_demo.yaml \
  --output runs/regulated_readiness_demo
```

## Example datasets

`evals/datasets/regulated_readiness_demo.jsonl` includes benign synthetic scenarios for:

- policy QA and governance classification
- RAG groundedness and audit explanation
- schema following
- prompt-injection resilience
- confidentiality and access-control reasoning

Each record carries:

- task id
- policy target
- failure category
- expected refusal behavior
- required and forbidden substrings

`evals/datasets/safety_smoke.jsonl` remains as a smaller CI-focused behavior smoke test.

## Evaluation artifacts

Each run writes:

- `summary.json`
- `cases.json`
- `report.md`

These artifacts are designed to be legible in pull requests, evaluation reviews, and model-governance discussions.

Public documentation:

- [Methodology](METHODOLOGY.md)
- [Limitations](LIMITATIONS.md)
- [Provider policy notes](PROVIDER_POLICY_NOTES.md)
- [Example report](reports/example_report.md)
- [Model readiness leaderboard surface](reports/model_readiness_leaderboard.md)

## Failure taxonomy

The built-in taxonomy tracks:

- `unsafe_compliance`
- `over_refusal`
- `missing_evidence`
- `instruction_drift`
- `formatting_failure`
- `latency_regression`

The taxonomy is deliberately explicit so teams can discuss model behavior in operational language rather than vague impressions.

## Included adapters

- `mock`: deterministic adapter for tests, CI, and local demos
- `openai`: API adapter scaffold
- `anthropic`: API adapter scaffold

The OpenAI and Anthropic adapters are intentionally thin and optional. The harness is built so adapter logic can stay small while evaluation logic stays consistent.

## PAEF methodology connection

PAEF introduced the atomic-evaluation pattern I use for regulated-enterprise model assessment: decompose complex governance/compliance tasks into policy-level checks, compare models and strategies, track uncertainty, and produce audit-ready diagnostics.

The evaluation research compares microagent-based atomic policy checks with monolithic LLM auditing across 193 service contracts and 7,913 labeled policy checks. See the [PAEF preprint](https://doi.org/10.5281/zenodo.19848867).

## Links

- Project page: [codychampion.bitsandbeakers.com/projects/llm-eval-workbench](https://codychampion.bitsandbeakers.com/projects/llm-eval-workbench)
- PAEF research page: [codychampion.bitsandbeakers.com/research/paef-contract-compliance](https://codychampion.bitsandbeakers.com/research/paef-contract-compliance)

## Roadmap

- publish initial provider-backed model-readiness comparison
- add calibrated rubric scoring beyond transparent string checks
- add sandboxed tool-use traces
- add per-model trend comparison across runs
- add dataset versioning and schema validation
