from typing import List

import requests
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.buttons.inline import updt_dlt_btn, user_inline
from app.buttons.reply import auth, btns, user_btns
from app.states import EventState, TgUserState, UpdateEventState
from aiogram.types import ReplyKeyboardRemove

router = Router()
url = 'http://127.0.0.1:8000/'
#######################REGISTER#########################

@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    response = requests.get(url + f'user/{message.from_user.id}')
    if response.status_code == 404:
        await message.answer('Вы не зарегистрированы!', reply_markup=auth)
        return
    curr_user = requests.get(url + f'user/{message.from_user.id}').json()
    if curr_user['role'] == 'admin':
        await message.answer(f'Hello, {message.from_user.full_name}', reply_markup=btns)
        return
    await message.answer(f'Hello, {message.from_user.full_name}', reply_markup=user_btns)

@router.message(F.text == 'Зарегистрироваться')
async def register(msg: Message):
    tg_id = msg.from_user.id
    data = {
        "id": tg_id,
    }
    requests.post(url+'user/create/', json=data)
    await msg.answer('Success!', reply_markup=btns)

################CREATE##################################

@router.message(F.text == 'Create event')
async def create_event(msg: Message, state: FSMContext):
    await msg.answer('Event name:')
    await state.set_state(EventState.title)

@router.message(EventState.title)
async def title(msg: Message, state: FSMContext):
    title = msg.text
    await state.update_data(title=title)
    await msg.answer('Event Description: ')
    await state.set_state(EventState.description)
@router.message(EventState.description)
async def desciption(msg: Message, state: FSMContext):
    desciption = msg.text
    await state.update_data(desciption=desciption)
    await msg.answer('Event Date')
    await state.set_state(EventState.date)


@router.message(EventState.date)
async def date(msg: Message, state: FSMContext):
    date = msg.text
    if date.isdigit():
        await msg.answer("Enter date like(day-month-year)")
        return
    await state.update_data(date=date)
    await msg.answer('Event location: ')
    await state.set_state(EventState.location)
@router.message(EventState.location)
async def location(msg: Message, state: FSMContext):
    location = msg.text
    await state.update_data(location=location)
    dt = await state.get_data()
    data = {
        'title': dt['title'],
        'description': dt['desciption'],
        'date': dt['date'],
        'location': dt['location']

    }
    requests.post(url+'event/create/', json=data)
    await msg.answer('Event has been created successfuly!')


#######################EVENT LIST ########################

@router.message(F.text == 'Event list')
async def event_list(message:Message, state: FSMContext):
    data = requests.get(url+'event/all/').json()
    if len(data) == 0:
        await message.answer('Событий пока нет!')
        return
    events = requests.get(url+'event/all/').json()
    text = ''
    for e in events:
        text += f'''
ID: {e['id']}
Title: {e['title']}
Description: {e['description']}
Date: {e['date']}
Location: {e['location']}

'''
    await message.answer(text)
    await state.set_state(EventState.id)

#################### DETAIL ########################


@router.message(EventState.id)
async def detail(message: Message, state: FSMContext):
    curr_user = requests.get(url+f'user/{message.from_user.id}').json()
    event_id = message.text
    event = requests.get(url+f'event/{event_id}').json()
    text = ''
    text += f'''
Title: {event['title']}
Description: {event['description']}
Date: {event['date']}
Location: {event['location']}
'''
    if curr_user['role'] == 'admin':
        await message.answer(text, reply_markup=updt_dlt_btn)
        return
    await message.answer(text, reply_markup=user_inline)

    await state.update_data(id=event_id)
    await state.update_data(title=event['title'], desciption=event['description'], date=event['date'], location=event['location'])

@router.callback_query(F.data == 'confirm')
async def confirm(call: CallbackQuery, state: FSMContext):
    dt = await state.get_data()
    user = requests.get(url+f'user/{call.from_user.id}').json()
    user_id = call.from_user.id
    updated_user: List[list]= user['events']
    updated_user.append(dt)
    requests.patch(url+f'user/update/{user_id}/', json=user)
    await call.message.answer('Success!')
    await state.clear()

####################### UPDATE #######################

@router.callback_query(F.data == 'update')
async def update_event(call: CallbackQuery, state: FSMContext):

    await call.message.answer("If you want to change it enter title or enter('Skip')")
    await state.set_state(UpdateEventState.title)


@router.message(UpdateEventState.title)
async def title(msg: Message, state: FSMContext):
    title = msg.text
    await state.update_data(title=title)
    await msg.answer("If you want to change it enter description or enter('Skip')")
    await state.set_state(UpdateEventState.description)


@router.message(UpdateEventState.description)
async def desciption(msg: Message, state: FSMContext):
    desciption = msg.text
    await state.update_data(description=desciption)
    await msg.answer("If you want to change it enter date or enter('Skip')")
    await state.set_state(UpdateEventState.date)


@router.message(UpdateEventState.date)
async def date(msg: Message, state: FSMContext):
    date = msg.text
    if date.isdigit():
        await msg.answer("Enter date like(day-month-year)")
        return
    await state.update_data(date=date)
    await msg.answer("If you want to change it enter location or enter('Skip')")
    await state.set_state(UpdateEventState.location)
@router.message(UpdateEventState.location)
async def location(msg: Message, state: FSMContext):
    location = msg.text
    await state.update_data(location=location)
    dt = await state.get_data()
    event_id = dt['id']
    data = {
        'title': dt['title'],
        'description': dt['description'],
        'date': dt['date'],
        'location': dt['location']

    }
    requests.patch(url+f'event/update/{event_id}', json=data)
    await msg.answer('Event has been updated successfuly!')



####################### DELETE ##########
@router.callback_query(F.data == 'delete')
async def delete(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    dt = await state.get_data()
    event_id = dt['id']
    requests.delete(url+f'event/delete/{event_id}')
    await call.message.answer('Событие удалено!')




@router.message(Command('current_user'))
async def is_staff(message: Message):
    user_id = message.from_user.id
    print(user_id)
    response = requests.get(url+f'user/{user_id}/')
    if response.status_code == 404:
        return

    data = response.json()
    print(data)

@router.message(Command('user_list'))
async def user_list(msg: Message):
    users = requests.get(url+'user/list/').json()
    text = ''
    for u in users:
        text += f'''
User ID: {u['id']}
Role: {u['role']}
Events: '''
        for e in u['events']:
            text+=f'''
Event ID: {e['id']}
Title: {e['title']}
Description: {e['description']}
Date: {e['date']}
Location: {e['location']}
'''
    await msg.answer('-------------------------\n'+text)


