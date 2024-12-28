import logging

from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states import UserStates

router = Router(name=__name__)


@router.callback_query(lambda c: c.data and c.data.startswith('subscription'))
async def tariff_plan_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.payment)
    data = callback_query.data.split('_')
    match data[1]:
        case '1':
            response = 'Вы выбрали подписку на один месяц'
            tariff = 1
        case '3':
            response = 'Вы выбрали подписку на три месяца'
            tariff = 3
        case '6':
            response = 'Вы выбрали подписку на шесть месяцев'
            tariff = 6
        case '12':
            response = 'Вы выбрали подписку на двенадцать месяцев'
            tariff = 12
        case 'life':
            response = 'Вы выбрали пожизненную подписку'
            tariff = 'life'

    await state.update_data(tariff=tariff)
    await callback_query.answer(response)
    # Например, редактируем сообщение
    await callback_query.message.edit_text(f"{response}")
    data = await state.get_data()
    logging.info(data)
