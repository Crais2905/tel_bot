from aiogram import types

keyboard = types.ReplyKeyboardMarkup(
    keyboard= [
        [
            types.KeyboardButton(text='help'),
            types.KeyboardButton(text='about'),
            types.KeyboardButton(text='inst')
        ],
        [
            types.KeyboardButton(text='tasks'),
            types.KeyboardButton(text='news')
        ]
    ],
    resize_keyboard=True
)


news_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='view last 5 news')
        ],
        [
            types.KeyboardButton(text='add new task')
        ]
    ],
    resize_keyboard=True
)