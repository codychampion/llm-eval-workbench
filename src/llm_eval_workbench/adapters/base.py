from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from llm_eval_workbench.metrics import UsageMetrics


@dataclass(frozen=True)
class ModelResponse:
    text: str
    usage: UsageMetrics
    metadata: dict[str, str]


class ModelAdapter(Protocol):
    def generate(self, prompt: str) -> ModelResponse:
        ...

