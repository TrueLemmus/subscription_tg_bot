from aiogram import Router, types
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(Command("help"))
async def command_help_handler(message: types.Message):
    await message.answer("Это справка по боту.")
