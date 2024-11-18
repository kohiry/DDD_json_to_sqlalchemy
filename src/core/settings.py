from pydantic_settings import BaseSettings

__all__ = [
    "settings",
]


class Settings(BaseSettings):
    API_HOST: str
    API_PORT: int
    LOG_LEVEL: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DRIVER_ALEMBIC: str
    POSTGRES_DRIVER_SQLALCHEMY: str
    POSTGRES_CONN_LINK: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
