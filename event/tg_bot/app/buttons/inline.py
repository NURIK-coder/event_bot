from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

updt_dlt_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Изменить', callback_data='update')
    ],
    [
        InlineKeyboardButton(text='Удалить', callback_data='delete')
    ]
])
user_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Учасвтвовать', callback_data='confirm')
    ],
    [
        InlineKeyboardButton(text='Отменить участие', callback_data='cancel')
    ]
])