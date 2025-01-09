from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_handler_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать тариф",
                              callback_data='select_plan')],
    ])

    return keyboard
