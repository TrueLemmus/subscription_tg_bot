from aiogram import Dispatcher

from .start import router as start_router
from .help import router as help_router
# Импортируйте другие роутеры


def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(help_router)
