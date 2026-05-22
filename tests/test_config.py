from llm_eval_workbench.config import load_config


def test_load_config_resolves_fields() -> None:
    config = load_config("evals/configs/safety_smoke.yaml")
    assert config.name == "safety_smoke"
    assert config.adapter.kind == "mock"
    assert config.dataset.name == "safety_smoke.jsonl"

