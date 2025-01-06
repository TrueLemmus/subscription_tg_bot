from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Subscription, SubscriptionType, SubscriptionStatus, SubscriptionPlan
from datetime import date, timedelta
from .subscription_plan import get_subscription_plan


async def create_subscription(session: AsyncSession,
                              user_id: int,
                              subscription_plan_id: int,
                              start_date: date = None,
                              end_date: date = None,
                              status: SubscriptionStatus = SubscriptionStatus.ACTIVE) -> Subscription:

    subscription_plan: SubscriptionPlan = await get_subscription_plan(session, subscription_plan_id)

    if not start_date:
        start_date = date.today()

    if not end_date:
        if subscription_plan.type != SubscriptionType.LIFETIME:
            # Примерный расчет
            end_date = start_date + timedelta(days=SubscriptionType(subscription_plan.type).value * 30)
        else:
            end_date = None  # Бессрочная подписка

    new_subscription = Subscription(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        subscription_plan_id=subscription_plan_id,
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


async def get_active_subscriptions_by_user(session: AsyncSession,
                                           user_id: int) -> list[Subscription]:
    result = await session.execute(select(Subscription).where(Subscription.user_id == user_id,
                                                              Subscription.status == SubscriptionStatus.ACTIVE))
    subscriptions = result.scalars().one_or_none()
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


async def renew_subscription(session: AsyncSession,
                             subscription_id: int,
                             subscription_plan_id: int,
                             status: SubscriptionStatus = SubscriptionStatus.ACTIVE) -> Subscription:
    subscription: Subscription = await get_subscription_by_id(session, subscription_id)
    if subscription:
        subscription_plan: SubscriptionPlan = await get_subscription_plan(session, subscription_plan_id)
        if subscription_plan.type != SubscriptionType.LIFETIME:
            # Примерный расчет
            end_date = subscription.end_date + timedelta(days=SubscriptionType(subscription_plan.type) * 30)
        else:
            end_date = None  # Бессрочная подписка
        subscription.end_date = end_date
        subscription.subscription_plan_id = subscription_plan.id
        await session.commit()
        await session.refresh(subscription)
    return subscription


async def get_subscriptions_to_cancel(session: AsyncSession) -> List[Subscription]:
    result = await session.execute(
        select(Subscription).where(
            Subscription.end_date <= date.today(),
            Subscription.status == SubscriptionStatus.ACTIVE
            )
        )
    subscriptions = result.scalars().all()
    return subscriptions
