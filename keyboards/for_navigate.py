from aiogram import types

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='help'),
            types.KeyboardButton(text='about'),
            types.KeyboardButton(text='inst')
        ],
        [
            types.KeyboardButton(text='tasks')
        ]
    ],
    resize_keyboard=True
)


news_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='view all tasks')
        ],
        [
            types.KeyboardButton(text='add new task')
        ]
    ],
    resize_keyboard=True
)


cancel_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='cancel')
        ]
    ],
    resize_keyboard=True
)
