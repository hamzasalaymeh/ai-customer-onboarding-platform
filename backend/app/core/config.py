from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Customer Onboarding Platform"
    environment: str = "development"
    debug: bool = True

    cors_origins: str = "http://localhost:5173"

    database_url: str = "sqlite:///./onboarding.db"

    ai_provider_api_key: str = ""
    ai_model_name: str = "claude-sonnet-5"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
