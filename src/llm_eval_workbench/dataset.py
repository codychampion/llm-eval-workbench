from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class EvalCase:
    case_id: str
    prompt: str
    expected_refusal: bool
    must_include: list[str] = field(default_factory=list)
    must_not_include: list[str] = field(default_factory=list)
    failure_mode: str = "instruction_drift"
    metadata: dict[str, str] = field(default_factory=dict)


def load_dataset(path: str | Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        raw = json.loads(line)
        cases.append(
            EvalCase(
                case_id=raw["id"],
                prompt=raw["prompt"],
                expected_refusal=bool(raw["expected_refusal"]),
                must_include=list(raw.get("must_include", [])),
                must_not_include=list(raw.get("must_not_include", [])),
                failure_mode=raw.get("failure_mode", "instruction_drift"),
                metadata=dict(raw.get("metadata", {})),
            )
        )
    return cases

