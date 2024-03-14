from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import ReplyKeyboardRemove

from filters.type_of_chat import ChatTypeFilter
from keyboards.for_navigate import keyboard

private_router = Router()
private_router.message.filter(ChatTypeFilter(['private']))


@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('this answer for start', reply_markup=keyboard)


@private_router.message(or_f(Command('help'), F.text.lower() == 'help'))
async def help_cmd(message: types.Message):
    await message.answer('commands list', reply_markup=ReplyKeyboardRemove())


@private_router.message(or_f(Command('about'), F.text.lower() == 'about'))
async def help_cmd(message: types.Message):
    await message.answer('info about us')


@private_router.message(or_f(Command('inst'), F.text.lower() == 'інстаграм', F.text == 'inst'))
async def inst_link_cmd(message: types.Message):
    await message.answer(
        'https://www.instagram.com/sviatoslav.lisovets?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=='
    )



