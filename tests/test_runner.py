import json

from llm_eval_workbench.config import load_config
from llm_eval_workbench.runner import run_eval


def test_run_eval_writes_artifacts(tmp_path) -> None:
    config = load_config("evals/configs/safety_smoke.yaml")
    summary = run_eval(config, tmp_path)
    assert summary["case_count"] == 4
    assert (tmp_path / "summary.json").exists()
    assert (tmp_path / "cases.json").exists()
    assert (tmp_path / "report.md").exists()

    payload = json.loads((tmp_path / "summary.json").read_text(encoding="utf-8"))
    assert payload["adapter"] == "mock"

