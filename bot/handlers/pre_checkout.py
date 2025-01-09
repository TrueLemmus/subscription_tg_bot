from aiogram.types import PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from routers import main_router
from loader import bot
from states import UserStates


# pre checkout  (must be answered in 10 seconds)
@main_router.pre_checkout_query(lambda query: True)
async def pre_checkout_query_handler(pre_checkout_q: PreCheckoutQuery, state: FSMContext):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
    await state.set_state(UserStates.subscription)
