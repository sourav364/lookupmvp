"""Basic schema validation tests."""
from api.schemas import JobCreate, QARequest, QAResponse, TileSpec


def test_job_create() -> None:
    job = JobCreate(video_url="http://example.com/video.mp4", zones_json={})
    assert job.video_url.startswith("http")


def test_qa_response() -> None:
    resp = QAResponse(answer="a", metrics={}, clips=[], boxes=[], plan={}, confidence=0.1)
    assert resp.answer == "a"


def test_tile_spec() -> None:
    tile = TileSpec(video_id="v1", spec={"type": "chart"})
    assert tile.video_id == "v1"
