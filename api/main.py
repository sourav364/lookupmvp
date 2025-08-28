"""FastAPI application for lookup MVP."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List
from uuid import uuid4

import redis
from fastapi import FastAPI, HTTPException
from rq import Queue

from .config import settings
from .planner import compile_plan
from .schemas import (
    QARequest,
    QAResponse,
    JobCreate,
    JobStatus,
    TileSpec,
)

app = FastAPI(title="lookup")

jobs: Dict[str, str] = {}
dashboards: Dict[str, List[Dict[str, Any]]] = {}
DASHBOARD_FILE = Path("storage/dashboards.json")
if DASHBOARD_FILE.exists():
    dashboards = json.loads(DASHBOARD_FILE.read_text())


def _save_dashboards() -> None:
    DASHBOARD_FILE.write_text(json.dumps(dashboards))


@app.get("/health")
def health() -> Dict[str, str]:
    """Health check endpoint."""

    return {"status": "ok"}


def _enqueue(job: JobCreate) -> str:
    try:
        conn = redis.from_url(settings.redis_url)
        q = Queue("lookup", connection=conn)
        rq_job = q.enqueue("worker.pipelines.ingest.process", job.video_url)
        job_id = rq_job.id
    except Exception:
        job_id = str(uuid4())
    jobs[job_id] = "queued"
    return job_id


@app.post("/jobs")
def create_job(job: JobCreate) -> Dict[str, str]:
    """Create a processing job and enqueue it."""

    job_id = _enqueue(job)
    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> JobStatus:
    """Get job status, progressing through fake states."""

    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    status = jobs[job_id]
    if status == "queued":
        jobs[job_id] = "running"
        status = "running"
    elif status == "running":
        jobs[job_id] = "done"
        status = "done"
    return JobStatus(job_id=job_id, status=status)


@app.post("/qa")
def qa(req: QARequest) -> QAResponse:
    """Return a fixed QA response."""

    plan = compile_plan(req.question)
    return QAResponse(
        answer="Stub: 12 people between 19:00-21:00",
        metrics={"count_series": [["2025-01-01T19:00:00Z", 6], ["2025-01-01T19:01:00Z", 12]]},
        clips=[],
        boxes=[],
        plan=plan,
        confidence=0.5,
    )


@app.get("/dashboards")
def list_dashboards(video_id: str) -> List[Dict[str, Any]]:
    """Return stored dashboard tiles for a video."""

    return dashboards.get(video_id, [
        {"id": "default", "video_id": video_id, "spec": {"type": "placeholder"}}
    ])


@app.post("/dashboards/{video_id}/pin", status_code=201)
def pin_dashboard(video_id: str, tile: TileSpec) -> Dict[str, str]:
    """Store a dashboard tile specification."""

    tile.id = str(uuid4())
    tile.video_id = video_id
    dashboards.setdefault(video_id, []).append(tile.model_dump())
    _save_dashboards()
    return {"id": tile.id}
