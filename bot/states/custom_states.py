from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    plan = State()
    payment = State()
    subscription = State()
