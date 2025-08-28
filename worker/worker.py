"""RQ worker entry point."""
from __future__ import annotations

import redis
from rq import Connection, Queue, Worker

from api.config import settings


def main() -> None:
    """Start an RQ worker listening to the 'lookup' queue."""

    conn = redis.from_url(settings.redis_url)
    with Connection(conn):
        worker = Worker(["lookup"])
        worker.work()


if __name__ == "__main__":
    main()
