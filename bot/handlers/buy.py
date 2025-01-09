from aiogram import types
from aiogram.fsm.context import FSMContext

from states import UserStates
from routers import main_router
from loader import bot
from config import config
from utils import generate_payload

from db import AsyncSessionLocal
from crud import get_subscription_plan
from models import SubscriptionPlan


@main_router.message(UserStates.payment)
async def buy_handler(message: types.Message, state: FSMContext):
    plan_id = await state.get_value('plan_id')
    payload = generate_payload(message.from_user.id)
    await state.update_data(payload=payload)

    async with AsyncSessionLocal() as session:
        plan: SubscriptionPlan = await get_subscription_plan(session=session, plan_id=plan_id)

    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_invoice(message.chat.id,
                           title=plan.label,
                           description=plan.description,
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           is_flexible=False,
                           prices=[types.LabeledPrice(label=plan.label, amount=plan.price * 100),],
                           payload=payload)
