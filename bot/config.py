import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    BOT_TOKEN: str
    DATABASE_NAME: str
    CELERY_BROKER: str
    CELERY_BACKEND: str
    TIMEZONE: str = 'Europe/Moscow'
    PRIVATE_CHANNEL_ID: str
    PAYMENTS_TOKEN: str
    LOG_LEVEL: str = 'DEBUG'

    class Config:
        env_file = ".env"


config = Config()
