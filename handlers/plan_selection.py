from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from keyboards import tariff_plan_message_and_keyboard
from states import UserStates


@main_router.message(UserStates.plan)
async def plan_selection_handler(message: types.Message,  state: FSMContext):
    await message.delete()
    message_text, keyboard = tariff_plan_message_and_keyboard()
    await message.answer(text=message_text, reply_markup=keyboard)
