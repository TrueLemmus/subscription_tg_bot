from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from models import SubscriptionPlan, SubscriptionType
from typing import List, Optional


# Create
async def create_subscription_plan(
    session: AsyncSession,
    label: str,
    description: str,
    type: SubscriptionType,
    price: int
) -> SubscriptionPlan:
    """
    Создает новый план подписки и добавляет его в базу данных.
    """
    new_plan = SubscriptionPlan(
        label=label,
        description=description,
        type=type,
        price=price
    )
    session.add(new_plan)
    await session.commit()
    await session.refresh(new_plan)
    return new_plan


# Read (Получение по ID)
async def get_subscription_plan(
    session: AsyncSession,
    plan_id: int
) -> Optional[SubscriptionPlan]:
    """
    Получает план подписки по его ID.
    Возвращает None, если план не найден.
    """
    result = await session.execute(
        select(SubscriptionPlan).where(SubscriptionPlan.id == plan_id)
    )
    plan = result.scalars().first()
    return plan


# Read (Получение всех)
async def get_all_subscription_plans(
    session: AsyncSession
) -> List[SubscriptionPlan]:
    """
    Получает список всех планов подписки.
    """
    result = await session.execute(select(SubscriptionPlan))
    plans = result.scalars().all()
    return plans


# Update
async def update_subscription_plan(
    session: AsyncSession,
    plan_id: int,
    label: Optional[str] = None,
    description: Optional[str] = None,
    type: Optional[SubscriptionType] = None,
    price: Optional[int] = None
) -> Optional[SubscriptionPlan]:
    """
    Обновляет существующий план подписки.
    Возвращает обновленный план или None, если план не найден.
    """
    result = await session.execute(
        select(SubscriptionPlan).where(SubscriptionPlan.id == plan_id)
    )
    plan = result.scalars().first()
    if not plan:
        return None

    if label is not None:
        plan.label = label
    if description is not None:
        plan.description = description
    if type is not None:
        plan.type = type
    if price is not None:
        plan.price = price

    await session.commit()
    await session.refresh(plan)
    return plan


# Delete
async def delete_subscription_plan(
    session: AsyncSession,
    plan_id: int
) -> bool:
    """
    Удаляет план подписки по его ID.
    Возвращает True, если удаление прошло успешно, иначе False.
    """
    result = await session.execute(
        select(SubscriptionPlan).where(SubscriptionPlan.id == plan_id)
    )
    plan = result.scalars().first()
    if not plan:
        return False

    await session.delete(plan)
    await session.commit()
    return True
