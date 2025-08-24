import os
from functools import lru_cache

class Settings:
	PROJECT_NAME: str = "My SA Babe"
	ENV: str = os.getenv("ENV", "dev")
	SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
	ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
	ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
	DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./dev.db")
	S3_BUCKET: str | None = os.getenv("S3_BUCKET")
	S3_REGION: str | None = os.getenv("S3_REGION")
	AWS_ACCESS_KEY_ID: str | None = os.getenv("AWS_ACCESS_KEY_ID")
	AWS_SECRET_ACCESS_KEY: str | None = os.getenv("AWS_SECRET_ACCESS_KEY")

@lru_cache
def get_settings() -> Settings:
	return Settings()