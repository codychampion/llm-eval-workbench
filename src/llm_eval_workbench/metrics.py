from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UsageMetrics:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    cost_usd: float
    latency_seconds: float


def estimate_tokens(text: str) -> int:
    return max(1, len(text.split()))

