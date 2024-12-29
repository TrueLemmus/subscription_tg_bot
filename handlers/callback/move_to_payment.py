from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from states import UserStates
from keyboards import move_to_payment_inline_keyboard


@main_router.callback_query(lambda c: c.data and c.data.startswith('subscription'))
async def move_to_payment_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.payment)
    data = callback_query.data.split('_')
    match data[1]:
        case '1':
            response = 'Вы выбрали подписку на один месяц'
            plan = 1
        case '3':
            response = 'Вы выбрали подписку на три месяца'
            plan = 3
        case '6':
            response = 'Вы выбрали подписку на шесть месяцев'
            plan = 6
        case '12':
            response = 'Вы выбрали подписку на двенадцать месяцев'
            plan = 12
        case 'life':
            response = 'Вы выбрали пожизненную подписку'
            plan = 'Lifetime'

    await state.update_data(plan=plan)
    await callback_query.answer(response)
    # Например, редактируем сообщение
    await callback_query.message.edit_text(text=f"{response}", reply_markup=move_to_payment_inline_keyboard())
