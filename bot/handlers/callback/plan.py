from aiogram import types
from aiogram.fsm.context import FSMContext

from routers import main_router
from handlers.plan_selection import plan_selection_handler

from states import UserStates


@main_router.callback_query(lambda c: c.data and 'select_plan' in c.data)
async def plan_callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.plan)
    await plan_selection_handler(callback_query.message, state)
