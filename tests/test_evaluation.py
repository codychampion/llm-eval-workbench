from llm_eval_workbench.adapters.base import ModelResponse
from llm_eval_workbench.dataset import EvalCase
from llm_eval_workbench.evaluation import evaluate_case
from llm_eval_workbench.metrics import UsageMetrics


def make_response(text: str, latency: float = 0.2) -> ModelResponse:
    return ModelResponse(
        text=text,
        usage=UsageMetrics(
            prompt_tokens=10,
            completion_tokens=10,
            total_tokens=20,
            cost_usd=0.001,
            latency_seconds=latency,
        ),
        metadata={"adapter": "test"},
    )


def test_refusal_case_passes_when_refusal_detected() -> None:
    case = EvalCase(
        case_id="refusal",
        prompt="bad thing",
        expected_refusal=True,
        must_include=["can't help"],
        failure_mode="unsafe_compliance",
    )
    result = evaluate_case(case, make_response("I can't help with that harm request."), 1.0)
    assert result.passed is True


def test_missing_required_content_uses_case_failure_mode() -> None:
    case = EvalCase(
        case_id="grounded",
        prompt="good thing",
        expected_refusal=False,
        must_include=["reproducibility", "reviewability"],
        failure_mode="missing_evidence",
    )
    result = evaluate_case(case, make_response("Only reproducibility is mentioned."), 1.0)
    assert result.failure_category == "missing_evidence"


def test_latency_budget_can_fail_case() -> None:
    case = EvalCase(case_id="slow", prompt="hello", expected_refusal=False)
    result = evaluate_case(case, make_response("hello", latency=2.0), 1.0)
    assert result.failure_category == "latency_regression"

