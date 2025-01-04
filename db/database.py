from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import config
from models import Base  # Предполагается, что models/__init__.py импортирует Base

# Создание асинхронного движка
engine = create_async_engine(
    config.DATABASE_URL,
    echo=False,  # Включает логирование SQL-запросов
    future=True
)

# Создание асинхронной фабрики сессий
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)


# Функция для инициализации моделей и создания таблиц
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
