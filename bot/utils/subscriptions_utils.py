import asyncio
import json
import uuid

from typing import List
from db import AsyncSessionLocal
from models import Subscription, SubscriptionStatus, SubscriptionPlan
from crud import (get_active_subscriptions_by_user,
                  create_subscription,
                  renew_subscription,
                  update_subscription_status,
                  get_subscriptions_to_cancel,
                  get_subscription_plan)
from .channel_utils import remove_user_from_channel


async def subscribe_user(user_id: int, plan_id: int) -> Subscription:
    async with AsyncSessionLocal() as session:
        plan: SubscriptionPlan = await get_subscription_plan(session, plan_id)
        subscription: Subscription = await get_active_subscriptions_by_user(session, user_id)
        if subscription:
            subscription = await renew_subscription(session, subscription.id, plan.id)
        else:
            subscription = await create_subscription(session, user_id, plan.id)
        await session.commit()
        await session.refresh(subscription)
        return subscription


def generate_payload(user_id: int) -> str:
    """
    Генерирует уникальный payload для платежа.

    :param user_id: Идентификатор пользователя, совершающего платеж
    :return: Строка payload, закодированная в base64
    """
    # Генерация уникального идентификатора заказа
    order_id = str(uuid.uuid4())

    # Создание словаря с информацией о заказе
    payload_dict = {
        'order_id': order_id,
        'user_id': user_id,
    }

    # Преобразование словаря в JSON
    payload_json = json.dumps(payload_dict)
    return payload_json


async def cancel_subscriptions() -> None:
    async with AsyncSessionLocal() as session:
        subscriptions: List[Subscription] = await get_subscriptions_to_cancel(session)

    if subscriptions:
        semaphore = asyncio.Semaphore(10)

        async def process_subscription(subscription: Subscription):
            async with semaphore:
                async with AsyncSessionLocal() as session:
                    await update_subscription_status(session, subscription.id, SubscriptionStatus.EXPIRED)
                    await remove_user_from_channel(subscription.user_id)

        await asyncio.gather(*(process_subscription(s) for s in subscriptions))
