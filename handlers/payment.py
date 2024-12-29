from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from states import UserStates


@main_router.message(UserStates.payment)
async def payment_handler(message: types.Message,  state: FSMContext):
    await message.answer('Payment')
    await state.get_data()

