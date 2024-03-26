from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.formatting import as_section, Bold

from filters.type_of_chat import ChatTypeFilter
from keyboards.for_navigate import keyboard

private_router = Router()
private_router.message.filter(ChatTypeFilter(['private']))


@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('<b>Ласкаво просимо до нашого бота!</b>\n\nДля того, щоб дізнатись наші можливості напишіть /about', reply_markup=keyboard, parse_mode=ParseMode.HTML)


@private_router.message(or_f(Command('help'), F.text.lower() == 'help'))
async def help_cmd(message: types.Message):
    text = as_section(
        Bold('Ось усі доступні команди:'),
        '/about\n',
        '/inst\n',
        '/tasks'
    )
    await message.answer(text.as_html(), reply_markup=keyboard, parse_mode=ParseMode.HTML)


@private_router.message(or_f(Command('about'), F.text.lower() == 'about'))
async def help_cmd(message: types.Message):
    await message.answer('У нашому боті ви можете зручно добавляти та перегляти завдання, які вам потрібно виконати', reply_markup=keyboard)


@private_router.message(or_f(Command('inst'), F.text.lower() == 'інстаграм', F.text == 'inst'))
async def inst_link_cmd(message: types.Message):
    text = "Це мій <b><a href='https://www.instagram.com/sviatoslav.lisovets?igsh=MXR1ZTBidm1jcG90dg=='>Instagram</a></b>"
    await message.answer(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )


