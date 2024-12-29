from typing import List
from db import AsyncSessionLocal
from models import Subscription, SubscriptionType
from crud import get_subscriptions_by_user, create_subscription, renew_subscription


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
