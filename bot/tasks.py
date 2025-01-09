import asyncio
from celery import shared_task
from utils import cancel_subscriptions
from logger_config import get_logger

logger = get_logger(__name__)


@shared_task()
def cancel_subscriptions_task():
    try:
        logger.info("Запуск задачи cancel_subscriptions...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cancel_subscriptions())
        logger.info("Задача cancel_subscriptions выполнена успешно.")
    except Exception as e:
        logger.error(f"Ошибка в задаче cancel_subscriptions: {e}")
        raise e
