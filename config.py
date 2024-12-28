from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    MONTHLY_COST: int

    class Config:
        env_file = ".env"


config = Config()
