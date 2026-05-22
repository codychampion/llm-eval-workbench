from __future__ import annotations

import argparse
import json

from rich.console import Console

from llm_eval_workbench.config import load_config
from llm_eval_workbench.runner import run_eval


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run LLM evaluation configs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run an eval config")
    run_parser.add_argument("--config", required=True, help="Path to YAML config")
    run_parser.add_argument("--output", required=True, help="Output directory for artifacts")
    run_parser.add_argument("--json", action="store_true", help="Print JSON summary")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    console = Console()

    if args.command == "run":
        config = load_config(args.config)
        summary = run_eval(config, args.output)
        if args.json:
            console.print_json(json.dumps(summary))
        else:
            console.print(
                f"[green]Completed[/green] {summary['eval_name']} "
                f"with pass rate {summary['pass_rate']:.2%} across {summary['case_count']} cases."
            )
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

