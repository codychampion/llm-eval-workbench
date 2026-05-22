from __future__ import annotations

import json
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from llm_eval_workbench.adapters.mock_adapter import MockAdapter
from llm_eval_workbench.config import EvalConfig
from llm_eval_workbench.dataset import load_dataset
from llm_eval_workbench.evaluation import evaluate_case
from llm_eval_workbench.report import write_markdown_report
from llm_eval_workbench.taxonomy import FAILURE_TAXONOMY


def build_adapter(kind: str):
    if kind == "mock":
        return MockAdapter()
    if kind == "openai":
        from llm_eval_workbench.adapters.openai_adapter import OpenAIAdapter

        return OpenAIAdapter()
    if kind == "anthropic":
        from llm_eval_workbench.adapters.anthropic_adapter import AnthropicAdapter

        return AnthropicAdapter()
    raise ValueError(f"Unsupported adapter kind: {kind}")


def run_eval(config: EvalConfig, output_dir: str | Path) -> dict:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    cases = load_dataset(config.dataset)
    adapter = build_adapter(config.adapter.kind)

    results = []
    for case in cases:
        response = adapter.generate(case.prompt)
        result = evaluate_case(case, response, config.run.max_latency_seconds)
        results.append(result)

    failure_counts = Counter(result.failure_category for result in results if result.failure_category)
    summary = {
        "eval_name": config.name,
        "adapter": config.adapter.kind,
        "case_count": len(results),
        "pass_rate": sum(1 for result in results if result.passed) / max(1, len(results)),
        "avg_latency_seconds": sum(result.usage["latency_seconds"] for result in results) / max(1, len(results)),
        "total_cost_usd": sum(result.usage["cost_usd"] for result in results),
        "failure_categories": {category: failure_counts.get(category, 0) for category in FAILURE_TAXONOMY},
    }

    case_payload = [asdict(result) for result in results]
    (output_path / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (output_path / "cases.json").write_text(json.dumps(case_payload, indent=2), encoding="utf-8")
    write_markdown_report(output_path, summary, case_payload)
    return summary

