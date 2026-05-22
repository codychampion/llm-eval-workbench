from __future__ import annotations

from pathlib import Path


def write_markdown_report(output_dir: Path, summary: dict, cases: list[dict]) -> None:
    taxonomy_lines = "\n".join(
        f"| {category} | {count} |"
        for category, count in summary["failure_categories"].items()
    )
    report = f"""# Eval Report

## Run summary

- Eval: `{summary["eval_name"]}`
- Adapter: `{summary["adapter"]}`
- Cases: `{summary["case_count"]}`
- Pass rate: `{summary["pass_rate"]:.2%}`
- Average latency: `{summary["avg_latency_seconds"]:.2f}s`
- Estimated cost: `${summary["total_cost_usd"]:.4f}`

## Failure taxonomy

| Category | Count |
|---|---:|
{taxonomy_lines}

## Failing cases

{chr(10).join(f"- `{case['case_id']}` -> `{case['failure_category']}`" for case in cases if not case['passed']) or "- None"}
"""
    (output_dir / "report.md").write_text(report, encoding="utf-8")

