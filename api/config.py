"""Application configuration using environment variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings loaded from environment variables."""

    openai_api_key: str | None = None
    openai_model: str | None = None
    roboflow_api_key: str | None = None
    twelvelabs_api_key: str | None = None
    pinecone_api_key: str | None = None
    redis_url: str = "redis://localhost:6379/0"
    storage_bucket_url: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
