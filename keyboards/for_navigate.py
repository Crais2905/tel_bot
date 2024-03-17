from aiogram import types

keyboard = types.ReplyKeyboardMarkup(
    keyboard= [
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