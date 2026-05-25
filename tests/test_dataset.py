from llm_eval_workbench.dataset import load_dataset


def test_load_dataset_reads_cases() -> None:
    cases = load_dataset("evals/datasets/safety_smoke.jsonl")
    assert len(cases) == 4
    assert cases[1].expected_refusal is True


def test_regulated_readiness_demo_covers_enterprise_suites() -> None:
    cases = load_dataset("evals/datasets/regulated_readiness_demo.jsonl")
    suites = {case.metadata["suite"] for case in cases}
    assert len(cases) == 8
    assert {"rag_groundedness", "access_control_reasoning", "governance_classification"} <= suites
