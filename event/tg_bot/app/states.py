from aiogram.fsm.state import StatesGroup, State


class EventState(StatesGroup):
    id = State()
    title = State()
    description = State()
    date = State()
    location = State()

class TgUserState(StatesGroup):
    contact = State()

class UpdateEventState(StatesGroup):
    title = State()
    description = State()
    date = State()
    location = State()