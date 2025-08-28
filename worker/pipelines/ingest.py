"""Ingestion pipeline stub."""
from __future__ import annotations


def process(video_url: str) -> None:
    """Validate video path and pretend to chunk video."""

    if not video_url:
        raise ValueError("video_url is required")
    # In future this will download and chunk the video into frames.
