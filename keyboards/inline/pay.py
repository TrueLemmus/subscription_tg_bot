from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def pay_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить",
                              callback_data='payed')],
    ])

    return keyboard
