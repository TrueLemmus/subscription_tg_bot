from aiogram import types
from aiogram.filters import Command

from routers import main_router


@main_router.message(Command("help"))
async def command_help_handler(message: types.Message):
    await message.answer("Это справка по боту.")
