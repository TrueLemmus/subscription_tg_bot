from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from states import UserStates
from db import AsyncSessionLocal
from crud import create_subscription
from models.subscription import SubscriptionType, Subscription


@main_router.callback_query(lambda c: c.data and 'payed' in c.data)
async def payed_callback(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    plan = data.get('plan')
    await state.set_state(UserStates.subscription)
    async with AsyncSessionLocal() as session:
        subscription: Subscription = await create_subscription(session=session,
                                                               user_id=callback_query.message.from_user.id,
                                                               type=SubscriptionType(plan))
    await callback_query.answer('Вы оплатили подписку!')
    text = f'Подписка успешно оформлена. Подписка будет действовать до {subscription.end_date}'
    await callback_query.message.edit_text(text=text)
