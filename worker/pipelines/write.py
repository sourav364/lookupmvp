"""Persistence pipeline stub."""
from __future__ import annotations
from pathlib import Path
from typing import List, Dict

import duckdb


def run(tracks: List[Dict[str, str]], db_path: Path) -> None:
    """Stub persistence to DuckDB or Parquet."""

    db_path.parent.mkdir(parents=True, exist_ok=True)
    duckdb.connect(str(db_path)).close()
