from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, or_f, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.formatting import as_numbered_list, Bold, as_list

from filters.type_of_chat import ChatTypeFilter
from keyboards.for_navigate import news_keyboard, keyboard

news_router = Router()
news_router.message.filter(ChatTypeFilter(['private']))


class AddNews(StatesGroup):
    name = State()
    short_description = State()
    content = State()
    author = State()


@news_router.message(or_f(Command('news'), F.text == 'news'))
async def news_cmd(message: types.Message):
    await message.answer('Виберіть команду із клавіатури:', reply_markup=news_keyboard)


@news_router.message(F.text == 'view last 5 news')
async def view_news_cmd(message: types.Message):
    text = as_list(
        Bold('News:'),
        as_numbered_list(
            'New1',
            'New2',
            'New3',
            'New4',
            'New5'
        )
    )
    await message.answer(text.as_html(), parse_mode=ParseMode.HTML, reply_markup=keyboard)


@news_router.message(StateFilter(None), F.text == 'add new task')
async def add_new_cmd(message: types.Message,  state: FSMContext):
    await state.set_state(AddNews.name)
    await message.answer(text="Вкажіть заголовок новини:", reply_markup=ReplyKeyboardRemove())


@news_router.message(AddNews.name, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddNews.short_description)
    await message.answer("Вкажіть короткий опис новини:")


@news_router.message(AddNews.short_description, F.text)
async def add_new_content_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(short_description=message.text)
    await state.set_state(AddNews.content)
    await message.answer("Вкажіть увесь вміст новини:")


@news_router.message(AddNews.content, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(content=message.text)
    await state.set_state(AddNews.author)
    await message.answer("Вкажіть автора (це може бути ваше реальне ім'я або псевдонім):")


@news_router.message(AddNews.content, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(AddNews.author)
    await message.answer("Вкажіть автора (це може бути ваше реальне ім'я або псевдонім):")


@news_router.message(AddNews.author, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(author=message.text)
    data = await state.get_data()
    await message.answer("Чудово! Новину успішно додано")
    await message.answer(str(data), reply_markup=keyboard)
    await state.clear()