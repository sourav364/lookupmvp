"""Placeholder dashboard tile utilities."""
from __future__ import annotations

import streamlit as st
from typing import Any, Dict


def render_tile(tile: Dict[str, Any]) -> None:
    """Render a simple placeholder tile."""

    with st.container():
        st.write(tile.get("spec"))
