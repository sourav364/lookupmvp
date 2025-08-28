"""Metrics computation stub."""
from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd


def run(data: List[str], output_dir: Path) -> None:
    """Produce a dummy counts.parquet file."""

    output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame({"timestamp": ["2025-01-01T00:00:00Z"], "count": [0]})
    df.to_parquet(output_dir / "counts.parquet")
