from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

auth = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Зарегистрироваться')
    ]
])
btns = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Event list')
    ],
    [
        KeyboardButton(text='Create event')
    ]
])
# location_btn = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(text='Отправить локацию', request_location=True)
#     ]
# ])
user_btns = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Event list')
    ],
    [
        KeyboardButton(text='События в котором я участвую')
    ]
])