from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User


async def create_user(session: AsyncSession, full_name: str, id: Optional[int] = None) -> User:
    new_user = User(id=id, full_name=full_name)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def get_user_by_full_name(session: AsyncSession, full_name: str) -> User:
    result = await session.execute(select(User).where(User.full_name == full_name))
    user = result.scalars().first()
    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    return user


async def update_user_full_name(session: AsyncSession, user_id: int, new_full_name: str) -> User:
    user = await get_user_by_id(session, user_id)
    if user:
        user.full_name = new_full_name
        await session.commit()
        await session.refresh(user)
    return user


async def delete_user(session: AsyncSession, user_id: int) -> None:
    user = await get_user_by_id(session, user_id)
    if user:
        await session.delete(user)
        await session.commit()
