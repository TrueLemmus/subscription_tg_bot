from aiogram import Router, types
from aiogram.filters import Command

from keyboards import tariff_plan_message_and_keyboard

from crud import get_user_by_id, create_user

router = Router(name=__name__)


@router.message(Command("start"))
async def command_start_handler(message: types.Message):
    text = 'Приветствую!\nДля подписки выбери один из тарифов ниже:'
    await message.answer(text)
    message_text, keyboard = tariff_plan_message_and_keyboard()
    await message.answer(text=message_text, reply_markup=keyboard)
