from __future__ import annotations

from llm_eval_workbench.adapters.base import ModelResponse
from llm_eval_workbench.metrics import UsageMetrics, estimate_tokens


class MockAdapter:
    """Deterministic adapter for tests, CI, and local examples."""

    def generate(self, prompt: str) -> ModelResponse:
        normalized = prompt.lower()
        if "sabotage a production database" in normalized:
            text = "I can't help with sabotaging a production system or causing harm."
        elif "exactly one sentence" in normalized:
            text = "This eval harness tracks latency and cost alongside task quality so runs stay reviewable."
        elif "two bullets" in normalized:
            text = "- Reproducibility improves when configs define the run.\n- Reviewability improves when the expected checks are explicit."
        elif "label line and a rationale line" in normalized:
            text = "Label: operational risk\nRationale: latency tracking matters because regressions can break user-facing systems before quality metrics move."
        else:
            text = "Unhandled mock prompt."

        prompt_tokens = estimate_tokens(prompt)
        completion_tokens = estimate_tokens(text)
        usage = UsageMetrics(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            cost_usd=(prompt_tokens + completion_tokens) * 0.00002,
            latency_seconds=0.34,
        )
        return ModelResponse(text=text, usage=usage, metadata={"adapter": "mock"})

