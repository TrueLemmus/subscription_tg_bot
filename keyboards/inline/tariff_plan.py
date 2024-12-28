from typing import Dict, Tuple
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils import get_subscription_cost


def tariff_plan_message_and_keyboard() -> Tuple[str, InlineKeyboardMarkup]:
    costs: Dict[str, float] = get_subscription_cost()

    message_text = (
        f"• <b>1 месяц</b> за <b>{costs.get('one_month')} р.</b>\n"
        f"• <b>3 месяца</b> за <b>{costs.get('three_months')} р.</b>\n"
        f"• <b>6 месяцев</b> за <b>{costs.get('six_months')} р.</b>\n"
        f"• <b>12 месяцев</b> за <b>{costs.get('twelve_months')} р.</b>\n"
        f"• <b>Пожизненная подписка</b> за <b>{costs.get('life_time')} р.</b>"
    )

    # Создаем кнопки без форматирования
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Оформить 1 месяц",
                              callback_data='subscription_1_month')],
        [InlineKeyboardButton(text="Оформить 3 месяца",
                              callback_data='subscription_3_month')],
        [InlineKeyboardButton(text="Оформить 6 месяцев",
                              callback_data='subscription_6_month')],
        [InlineKeyboardButton(text="Оформить 12 месяцев",
                              callback_data='subscription_12_month')],
        [InlineKeyboardButton(text="Оформить пожизненно",
                              callback_data='subscription_life_time')]
    ])

    return message_text, keyboard
