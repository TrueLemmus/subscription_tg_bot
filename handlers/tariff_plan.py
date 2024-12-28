from aiogram import Router, types

router = Router(name=__name__)


@router.callback_query(lambda c: c.data and c.data.startswith('subscription'))
async def tariff_plan_handler(callback_query: types.CallbackQuery):
    data = callback_query.data.split('_')
    match data[1]:
        case '1':
            response = 'Вы выбрали подписку на один месяц'
        case '3':
            response = 'Вы выбрали подписку на три месяца'
        case '6':
            response = 'Вы выбрали подписку на шесть месяцев'
        case '12':
            response = 'Вы выбрали подписку на двенадцать месяцев'
        case 'life':
            response = 'Вы выбрали пожизненную подписку'

    await callback_query.answer(response)
    # Например, редактируем сообщение
    await callback_query.message.edit_text(f"{response}")
