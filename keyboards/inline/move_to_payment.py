from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def move_to_payment_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать способ оплаты и оплатить",
                              callback_data='payment_method')],
    ])

    return keyboard
