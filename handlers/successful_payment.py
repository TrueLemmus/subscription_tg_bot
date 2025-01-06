from datetime import datetime, timedelta

from aiogram import F
from aiogram.types import Message, ChatInviteLink
from aiogram.fsm.context import FSMContext
from routers import main_router
from loader import bot
from utils import subscribe_user
from config import config
from models import Subscription


# successful payment
@main_router.message(F.successful_payment.is_not(None))
async def successful_payment_handler(message: Message, state: FSMContext):
    payload = await state.get_value('payload')
    plan_id = await state.get_value('plan_id')
    invoice_payload = message.successful_payment.invoice_payload

    if payload != invoice_payload:
        message.answer('Ошибка обработки платежа, обратитесь в поддержку.')
        return

    await bot.send_message(message.chat.id,
                           f'Платеж на сумму {message.successful_payment.total_amount // 100}'
                           f' {message.successful_payment.currency} прошел успешно!!!')
    subscription: Subscription = await subscribe_user(message.from_user.id, plan_id)
    await bot.unban_chat_member(chat_id=config.PRIVATE_CHANNEL_ID,
                                user_id=message.from_user.id,
                                only_if_banned=True)
    invite_link: ChatInviteLink = await bot.create_chat_invite_link(chat_id=config.PRIVATE_CHANNEL_ID,
                                                                    expire_date=datetime.now() + timedelta(days=1),
                                                                    member_limit=1)
    text = f'Подписка успешно оформлена. Подписка будет действовать до {subscription.end_date}\n'\
           f'Ваша ссылка на канал {invite_link.invite_link}'
    await message.answer(text=text)
