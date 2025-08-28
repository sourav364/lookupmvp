"""Tool stubs for future video analytics functions."""
from typing import Any, Iterable


def detect_open_vocab(frames: Iterable[Any]) -> list[dict]:
    """Detect objects with an open-vocabulary model."""
    raise NotImplementedError("detect_open_vocab is not implemented yet")


def track(detections: list[dict]) -> list[dict]:
    """Track objects across frames."""
    raise NotImplementedError("track is not implemented yet")


def filter_color(tracks: list[dict], color: str) -> list[dict]:
    """Filter tracks by color attribute."""
    raise NotImplementedError("filter_color is not implemented yet")
