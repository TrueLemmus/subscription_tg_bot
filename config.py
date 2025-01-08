from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    CELERY_BROKER: str
    CELERY_BACKEND: str
    TIMEZONE: str = 'Europe/Moscow'
    PRIVATE_CHANNEL_ID: str
    PAYMENTS_TOKEN: str
    LOG_LEVEL: str = 'DEBUG'

    class Config:
        env_file = ".env"


config = Config()
