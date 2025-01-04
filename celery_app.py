import logging
from celery import Celery
from celery.schedules import crontab
from config import config

# Настройка логирования
logger = logging.getLogger(__name__)

celery_app = Celery(
    'subscription_tg_bot',
    broker=config.CELERY_BROKER,
    backend=config.CELERY_BACKEND,
    include=['tasks'],  # Добавляем модуль с задачами
)

celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=10,
    timezone=config.TIMEZONE,
    enable_utc=True,
)

celery_app.conf.beat_schedule = {
    'cancel-subscriptions': {
        'task': 'tasks.cancel_subscriptions_task',
        'schedule': crontab(hour='0,12', minute=0)
    },
}
