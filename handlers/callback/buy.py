from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from handlers import buy_handler
from states import UserStates


@main_router.callback_query(lambda c: c.data and 'buy' in c.data)
async def buy_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.payment)
    await callback_query.answer()
    await buy_handler(callback_query.message)
