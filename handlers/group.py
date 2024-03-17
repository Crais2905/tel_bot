from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, or_f
from filters.type_of_chat import ChatTypeFilter

group_router = Router()
group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@group_router.message(Command('group'))
async def group_mud(message: types.Message):
    await message.answer('text in group')


@group_router.message(F.text.contains('spam'))
async def spam_hnd(message: types.Message):
    await message.answer('spam text')


@group_router.message(F.text.lower() == 'інстаграм', F.text == 'inst')
async def inst_link_cmd(message: types.Message):
    text = "It's our <b><a href='https://www.instagram.com/sviatoslav.lisovets?igsh=MXR1ZTBidm1jcG90dg=='>inst</a></b>"
    await message.answer(
        text,
        parse_mode=ParseMode.HTML
    )

