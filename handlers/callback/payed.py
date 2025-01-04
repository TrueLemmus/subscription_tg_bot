from datetime import datetime, timedelta

from aiogram import types
from aiogram.fsm.context import FSMContext

from loader import bot
from routers import main_router
from states import UserStates
from utils import subscribe_user
from models.subscription import SubscriptionType, Subscription
from config import config


@main_router.callback_query(lambda c: c.data and 'payed' in c.data)
async def payed_callback(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    plan = data.get('plan')
    await state.set_state(UserStates.subscription)
    subscription: Subscription = await subscribe_user(callback_query.message.from_user.id,
                                                      SubscriptionType(plan))
    await callback_query.answer('Вы оплатили подписку!')
    invite_link: types.ChatInviteLink = await bot.create_chat_invite_link(chat_id=config.PRIVATE_CHANNEL_ID,
                                                                          expire_date=datetime.now() + timedelta(days=1),
                                                                          member_limit=1)
    text = f'Подписка успешно оформлена. Подписка будет действовать до {subscription.end_date}\n'\
           f'Ваша ссылка на канал {invite_link.invite_link}'
    await callback_query.message.edit_text(text=text)
