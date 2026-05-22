from llm_eval_workbench.dataset import load_dataset


def test_load_dataset_reads_cases() -> None:
    cases = load_dataset("evals/datasets/safety_smoke.jsonl")
    assert len(cases) == 4
    assert cases[1].expected_refusal is True

