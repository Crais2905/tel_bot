from aiogram import types, Router, F
from aiogram.filters import Command
from filters.type_of_chat import ChatTypeFilter

group_router = Router()
group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@group_router.message(Command('group'))
async def group_mud(message: types.Message):
    await message.answer('text in group')


@group_router.message(F.text.contains('spam'))
async def spam_hnd(message: types.Message):
    await message.answer('spam text')

