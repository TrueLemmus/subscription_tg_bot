import logging
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from routers import main_router
from keyboards import start_handler_inline_keyboard

from db import AsyncSessionLocal
from crud import get_user_by_id, create_user


@main_router.message(Command("start"))
async def command_start_handler(message: types.Message,  state: FSMContext):
    # await state.set_state(UserStates.tariff)
    async with AsyncSessionLocal() as session:
        user = await get_user_by_id(session=session, user_id=message.from_user.id)
        if not user:
            user = await create_user(session=session, full_name=message.from_user.full_name, id=message.from_user.id)
    logging.info(user)
    text = f'Приветствую {message.from_user.first_name}!\nВыберите одно из возможных действий:'
    await message.answer(text=text, reply_markup=start_handler_inline_keyboard())
