from aiogram import types

keyboard = types.ReplyKeyboardMarkup(
    keyboard= [
        [
            types.KeyboardButton(text='help'),
            types.KeyboardButton(text='about')
        ],
        [
            types.KeyboardButton(text='inst')
        ]
    ],
    resize_keyboard=True
)