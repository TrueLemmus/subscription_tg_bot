import asyncio
import logging
from celery import shared_task
from utils import cancel_subscriptions

logger = logging.getLogger(__name__)


@shared_task()
def cancel_subscriptions_task():
    try:
        logger.info("Запуск задачи cancel_subscriptions...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cancel_subscriptions())
        print("Отменяются подписки...")
        logger.info("Задача cancel_subscriptions выполнена успешно.")
    except Exception as e:
        logger.error(f"Ошибка в задаче cancel_subscriptions: {e}")
        raise e
