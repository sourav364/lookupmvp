"""Pydantic models for API requests and responses."""
from __future__ import annotations

from typing import Any, Dict, List
from pydantic import BaseModel


class JobCreate(BaseModel):
    """Request body for creating a processing job."""

    video_url: str
    zones_json: Dict[str, Any]


class JobStatus(BaseModel):
    """Response model for job status."""

    job_id: str
    status: str


class QARequest(BaseModel):
    """Request body for question answering."""

    video_id: str
    question: str


class QAResponse(BaseModel):
    """Response model for question answering."""

    answer: str
    metrics: Dict[str, Any]
    clips: List[Any]
    boxes: List[Any]
    plan: Dict[str, Any]
    confidence: float


class TileSpec(BaseModel):
    """Dashboard tile specification."""

    id: str | None = None
    video_id: str
    spec: Dict[str, Any]
