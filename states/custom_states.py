from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    tariff = State()
    payment = State()
    subscription = State()
