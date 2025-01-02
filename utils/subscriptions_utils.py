import asyncio
from typing import Dict, List
from config import config
from db import AsyncSessionLocal
from models import Subscription, SubscriptionType, SubscriptionStatus
from crud import (get_subscriptions_by_user,
                  create_subscription, renew_subscription,
                  update_subscription_status, get_subscriptions_to_cancel)
from .channel_utils import remove_user_from_channel


async def subscribe_user(user_id: int, subscription_type: SubscriptionType) -> Subscription:
    async with AsyncSessionLocal() as session:
        subscriptions: List[Subscription] = await get_subscriptions_by_user(session, user_id)
        subscription: Subscription = subscriptions[0]
        if subscription:
            subscription = await renew_subscription(session, subscription.id, subscription_type)
        else:
            subscription = await create_subscription(session, user_id, subscription_type)
        await session.commit()
        await session.refresh(subscription)
        return subscription


def get_subscription_cost() -> Dict[str, float]:
    # 1 3 6 12 LifeTime
    cost = {}
    cost['one_month'] = float(config.MONTHLY_COST)
    cost['three_months'] = round(config.MONTHLY_COST * 3 * 0.84, 0)
    cost['six_months'] = round(config.MONTHLY_COST * 6 * 0.67, 0)
    cost['twelve_months'] = round(config.MONTHLY_COST * 12 * 0.50, 0)
    cost['life_time'] = float(config.MONTHLY_COST * 12)
    return cost


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
