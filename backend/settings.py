import os
from pydantic import BaseModel

class Settings(BaseModel):
    # Default points to Postgres in docker-compose. For local w/out Postgres, swap to SQLite:
    # database_url: str = os.getenv("DATABASE_URL", "sqlite:///./local.db")
    database_url: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@db:5432/postgres")
    model_dir: str = os.getenv("MODEL_DIR", "/models")
    value_per_conversion: float = float(os.getenv("VALUE_PER_CONVERSION", "100.0"))

_settings = Settings()

def get_settings():
    return _settings
