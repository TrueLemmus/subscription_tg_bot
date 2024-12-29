from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from keyboards import pay_inline_keyboard


@main_router.callback_query(lambda c: c.data and 'payment_telegram_wallet' in c.data)
async def telegram_wallet_payment_callback(callback_query: types.CallbackQuery, state: FSMContext):
    text = 'Чтобы оплатить через кошелёк телеграм нажмите кнопку оплатить.'
    await callback_query.message.edit_text(text=text, reply_markup=pay_inline_keyboard())
