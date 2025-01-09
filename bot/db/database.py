import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import config
from logger_config import get_logger
from models import Base  # Предполагается, что models/__init__.py импортирует Base

logger = get_logger(__name__)

# создание пути к базе
DB_PATH = os.path.join(config.BASE_DIR, 'data', config.DATABASE_NAME)
logger.info(f'Data base path {DB_PATH}')

# Создание асинхронного движка
engine = create_async_engine(
    f'sqlite+aiosqlite:///{DB_PATH}',
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
