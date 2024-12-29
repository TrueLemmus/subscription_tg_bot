from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def payment_method_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить СПБ",
                              callback_data='payment_SPB')],
        [InlineKeyboardButton(text="Оплатить через телеграм кошелёк",
                              callback_data='payment_telegram_wallet')],
    ])

    return keyboard
