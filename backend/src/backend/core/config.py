from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[4]


class Settings(BaseSettings):
    app_name: str = "Project Management con Agente AI"
    app_description: str = "API per la gestione di organizzazioni, progetti, attività e documenti, integrate con un agente AI."
    app_version: str = "0.1.0"

    postgres_db: str
    postgres_user: str
    postgres_password: str

    postgres_host: str = "localhost"
    postgres_port: int = 5432



    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()