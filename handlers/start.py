import logging
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards import tariff_plan_message_and_keyboard
from states import UserStates

from db import AsyncSessionLocal
from crud import get_user_by_id, create_user

router = Router(name=__name__)


@router.message(Command("start"))
async def command_start_handler(message: types.Message,  state: FSMContext):
    await state.set_state(UserStates.tariff)
    async with AsyncSessionLocal() as session:
        user = await get_user_by_id(session=session, user_id=message.from_user.id)
        if not user:
            user = await create_user(session=session, full_name=message.from_user.full_name, id=message.from_user.id)
    logging.info(user)
    text = 'Приветствую!\nДля подписки выбери один из тарифов ниже:'
    await message.answer(text)
    message_text, keyboard = tariff_plan_message_and_keyboard()
    await message.answer(text=message_text, reply_markup=keyboard)
