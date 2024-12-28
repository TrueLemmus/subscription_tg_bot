from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Subscription, SubscriptionType, SubscriptionStatus
from datetime import date, timedelta


async def create_subscription(session: AsyncSession,
                              user_id: int,
                              type: SubscriptionType,
                              start_date: date = None,
                              end_date: date = None,
                              status: SubscriptionStatus = SubscriptionStatus.ACTIVE) -> Subscription:
    if not start_date:
        start_date = date.today()

    if not end_date:
        if type != SubscriptionType.LIFETIME:
            end_date = start_date + timedelta(days=type.value * 30)  # Примерный расчет
        else:
            end_date = None  # Бессрочная подписка

    new_subscription = Subscription(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        type=type,
        status=status
    )
    session.add(new_subscription)
    await session.commit()
    await session.refresh(new_subscription)
    return new_subscription


async def get_subscription_by_id(session: AsyncSession,
                                 subscription_id: int) -> Subscription:
    result = await session.execute(select(Subscription).where(Subscription.id == subscription_id))
    subscription = result.scalars().first()
    return subscription


async def get_subscriptions_by_user(session: AsyncSession,
                                    user_id: int) -> list[Subscription]:
    result = await session.execute(select(Subscription).where(Subscription.user_id == user_id))
    subscriptions = result.scalars().all()
    return subscriptions


async def update_subscription_status(session: AsyncSession,
                                     subscription_id: int,
                                     new_status: SubscriptionStatus) -> Subscription:
    subscription = await get_subscription_by_id(session, subscription_id)
    if subscription:
        subscription.status = new_status
        await session.commit()
        await session.refresh(subscription)
    return subscription


async def delete_subscription(session: AsyncSession,
                              subscription_id: int) -> None:
    subscription = await get_subscription_by_id(session, subscription_id)
    if subscription:
        await session.delete(subscription)
        await session.commit()
