# Limitations

`llm-eval-workbench` is an early public evaluation harness, not a complete assurance program.

## Current limits

- The included published report uses a deterministic mock adapter to demonstrate the pipeline and artifact format, not to rank frontier models.
- Simple required/prohibited-string checks are transparent and testable, but they are not sufficient for nuanced semantic judgment.
- Latency and cost values depend on adapter-reported usage and must be interpreted in the context of provider pricing and run conditions.
- The public demo suite is deliberately benign and cannot stand in for authorized internal security testing.
- Model behavior can change across model revisions, provider policy changes, and prompt/template updates.

## Interpretation

A passing run means the evaluated model or adapter met the declared checks for that suite and configuration. It does not prove compliance, security, safety, or deployment fitness by itself.

Production decisions should combine:

- documented requirements and acceptance criteria
- human review
- security and privacy review
- provider-policy review
- repeatable regression runs
- monitoring after deployment

## Planned extensions

- provider-backed comparison runs with versioned model metadata
- structured rubric and calibrated scoring beyond string checks
- retrieval-grounded evaluation fixtures
- trend and regression reports across runs
- cost and latency comparison tables across supported adapters
