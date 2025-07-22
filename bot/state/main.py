from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    fullname = State()
    age = State()
    email = State()
    phone = State()

    