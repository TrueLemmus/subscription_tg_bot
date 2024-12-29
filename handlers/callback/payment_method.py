from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from keyboards import payment_method_inline_keyboard


@main_router.callback_query(lambda c: c.data and 'payment_method' in c.data)
async def payment_method_callback(callback_query: types.CallbackQuery, state: FSMContext):
    text = 'Выберите способ оплаты:'
    await callback_query.message.edit_text(text=text, reply_markup=payment_method_inline_keyboard())
