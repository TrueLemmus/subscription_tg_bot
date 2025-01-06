from typing import List
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from db import AsyncSessionLocal
from models import SubscriptionPlan
from crud import get_all_subscription_plans


async def tariff_plan_keyboard() -> InlineKeyboardMarkup:
    async with AsyncSessionLocal() as session:
        subscription_plans: List[SubscriptionPlan] = await get_all_subscription_plans(session=session)

    inline_keyboard = []
    for plan in subscription_plans:
        button = InlineKeyboardButton(
            text=f'{plan.description} за {plan.price} pyб.',
            callback_data=f'subscription_{plan.id}'
        )
        inline_keyboard.append([button,])

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
