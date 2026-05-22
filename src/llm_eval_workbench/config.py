from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class AdapterConfig:
    kind: str


@dataclass(frozen=True)
class RunConfig:
    owner: str
    purpose: str
    max_latency_seconds: float


@dataclass(frozen=True)
class EvalConfig:
    name: str
    adapter: AdapterConfig
    dataset: Path
    run: RunConfig


def load_config(path: str | Path) -> EvalConfig:
    config_path = Path(path)
    repo_root = config_path.resolve().parents[2]
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    return EvalConfig(
        name=raw["name"],
        adapter=AdapterConfig(kind=raw["adapter"]["kind"]),
        dataset=(repo_root / raw["dataset"]).resolve()
        if not Path(raw["dataset"]).is_absolute()
        else Path(raw["dataset"]),
        run=RunConfig(
            owner=raw["run"]["owner"],
            purpose=raw["run"]["purpose"],
            max_latency_seconds=float(raw["run"]["max_latency_seconds"]),
        ),
    )
