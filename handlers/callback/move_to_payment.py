from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from states import UserStates
from handlers import buy_handler
from db import AsyncSessionLocal
from crud import get_subscription_plan
from models import SubscriptionPlan


@main_router.callback_query(lambda c: c.data and c.data.startswith('subscription'))
async def move_to_payment_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.payment)
    plan_id = callback_query.data.split('_')[1]

    async with AsyncSessionLocal() as session:
        plan: SubscriptionPlan = await get_subscription_plan(session=session, plan_id=plan_id)

    response = f'Вы выбрали:\n{plan.label} за {plan.price} руб.'
    await state.update_data(plan_id=plan.id)
    await callback_query.answer(response)
    await callback_query.message.edit_text(text=f"{response}")
    await buy_handler(callback_query.message, state)
