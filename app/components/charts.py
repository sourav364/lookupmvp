"""Placeholder chart functions for Streamlit app."""
from __future__ import annotations

import pandas as pd


def dummy_chart() -> pd.DataFrame:
    """Return a small dataframe for demo charts."""

    return pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
