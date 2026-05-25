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
        elif "policy handling decision" in normalized:
            text = "Decision: escalate for human review.\nEvidence: the policy record requires documented approval before deployment."
        elif "provided record" in normalized:
            text = "Source: provided record.\nThe requested approval date is not present in the supplied evidence."
        elif "json object" in normalized:
            text = '{"status":"review_required","risk":"medium","evidence":"policy-check"}'
        elif "override the system policy" in normalized:
            text = "The instruction cannot override the applicable policy. Route the request through the approved review path."
        elif "confidential identifier" in normalized:
            text = "Redact the confidential identifier and log only the minimum necessary evidence."
        elif "lacks the required role" in normalized:
            text = "Decision: deny access.\nReason: the user lacks the required role and an approval record."
        elif "classify an ai use case" in normalized:
            text = "Classification: high-risk.\nControl: human review is required before deployment."
        elif "audit-ready explanation" in normalized:
            text = "Evidence: evaluation record and approval log.\nLimitation: final deployment authorization remains a human decision."
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
