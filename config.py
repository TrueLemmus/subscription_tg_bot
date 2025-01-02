from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    MONTHLY_COST: int
    CELERY_BROKER: str
    CELERY_BACKEND: str
    TIMEZONE: str = 'Europe/Moscow'

    class Config:
        env_file = ".env"


config = Config()
