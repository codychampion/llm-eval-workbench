# Regulated Enterprise Model Readiness Leaderboard

Weekly evaluation of frontier and open-source models across task performance, reliability, governance behavior, groundedness, cost, and latency.

## Public status

No provider-backed model comparison is published yet. The first row below is a deterministic pipeline validation run using the built-in `mock` adapter; it demonstrates the artifact and scoring surface without representing a model ranking.

| Adapter / Model | Provider | Suite | Eval date | Cases | Pass rate | Avg latency | Total estimated cost | Status |
|---|---|---|---|---:|---:|---:|---:|---|
| `mock` | local deterministic fixture | `regulated_enterprise_readiness_demo` | 2026-05-25 | 8 | 100.00% | 0.34s | $0.00476 | Pipeline validation only |

## Planned reporting columns

Future provider-backed rows will include capability, reliability, governance, and groundedness scores; latency p50/p95; cost per 1,000 tasks; cost per successful task; suite version; regression since the prior run; and limitations.

## Public-safety posture

This benchmark evaluates models on regulated-enterprise readiness. It uses benign synthetic or public-domain scenarios and does not attempt to elicit harmful operational content or bypass provider safeguards.

See [METHODOLOGY.md](../METHODOLOGY.md), [LIMITATIONS.md](../LIMITATIONS.md), and [PROVIDER_POLICY_NOTES.md](../PROVIDER_POLICY_NOTES.md).
