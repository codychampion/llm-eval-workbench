# Architecture

## Design goals

This repo is meant to look and behave like lightweight internal eval infrastructure rather than a notebook dump.

The core design choices are:

1. Separate adapters from evaluation logic.
2. Keep datasets declarative and versionable.
3. Make failure categories explicit enough for safety review.
4. Always produce artifacts that can be inspected after the run.
5. Track operational metrics alongside quality metrics.

## Execution flow

1. Load an eval config.
2. Load dataset rows from JSONL.
3. Instantiate an adapter.
4. Execute each case and collect response text plus operational metadata.
5. Score each result against configured requirements.
6. Aggregate pass rate, taxonomy counts, latency, token, and cost summaries.
7. Write JSON and Markdown artifacts.

## Why this shape matters

The repo is intentionally structured so it can grow toward:

- model safeguards evaluation
- frontier-risk probes
- red-team style scenario libraries
- observability hooks
- regression tracking over time

That makes it useful as a foundation for more serious internal evaluation work.
