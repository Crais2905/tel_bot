import asyncio

import aiofiles
from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, or_f, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.formatting import as_numbered_list, Bold, as_list, as_marked_list, as_key_value, as_marked_section
import json

from aiogram.utils.keyboard import InlineKeyboardBuilder

from filters.type_of_chat import ChatTypeFilter
from keyboards.for_navigate import news_keyboard, keyboard, cancel_keyboard

tasks_router = Router()
tasks_router.message.filter(ChatTypeFilter(['private']))


class AddTask(StatesGroup):
    name = State()
    number = State()
    content = State()
    deadline = State()


async def read_tasks():
    async with aiofiles.open('./tasks.json', encoding='utf-8') as file:
        data = await file.read()
        json_data = json.loads(data)
    return json_data


async def write_file(data):
    async with aiofiles.open('./tasks.json', 'w', encoding='utf-8') as file:
        await file.write(json.dumps(data, indent=4))


@tasks_router.message(or_f(Command('cancel'), F.text.casefold() == 'cancel'))
async def cancel_cmd(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        return

    await state.clear()
    await message.answer('Дію відмінено', reply_markup=keyboard)


@tasks_router.message(or_f(Command('tasks'), F.text == 'tasks'))
async def tasks_cmd(message: types.Message):
    await message.answer('Виберіть команду із клавіатури:', reply_markup=news_keyboard)


@tasks_router.message(F.text == 'view all tasks')
async def view_tasks_cmd(message: types.Message):
    counter = 1
    for i in await read_tasks():
        text = as_marked_section(
            Bold(f'Task {counter}'),
            as_key_value('Тема', i['name']),
            as_key_value('Номер', i['number']),
            as_key_value('Завдання', i['content']),
            as_key_value('Дедлайн', i['deadline']),
            marker='📌'
        )

        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(text='Видалити', callback_data=f'delete_task_{counter}'),
            types.InlineKeyboardButton(text='Редагувати', callback_data=f'edit_task_{counter}')
        )

        await message.answer(text.as_html(), parse_mode=ParseMode.HTML, reply_markup=builder.as_markup())
        counter += 1
        await asyncio.sleep(0.4)


@tasks_router.callback_query(F.data.split('_')[0] == 'delete')
async def del_task(callback: types.CallbackQuery):
    del_item_id = callback.data.split('_')[-1]
    tasks = await read_tasks()
    tasks.pop(int(del_item_id))
    await write_file(tasks)
    await callback.message.answer('Завдання видалено')


# @tasks_router.callback_query(F.data.split('_')[0] == 'edit')
# async def edit_task(callback: types.CallbackQuery):
#     edit_item_id = callback.data.split('-')[-1]
#     tasks = await read_tasks()



# FSM


@tasks_router.message(StateFilter(None), F.text == 'add new task')
async def add_new_cmd(message: types.Message,  state: FSMContext):
    await state.set_state(AddTask.name)
    await message.answer(text="Вкажіть тему:", reply_markup=ReplyKeyboardRemove())


@tasks_router.message(AddTask.name, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddTask.number)
    await message.answer("Вкажіть номер уроку(1 чи 2):", reply_markup=cancel_keyboard)


@tasks_router.message(AddTask.number, F.text)
async def add_new_content_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(AddTask.content)
    await message.answer("Вкажіть завдання:", reply_markup=cancel_keyboard)


@tasks_router.message(AddTask.content, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(content=message.text)
    await state.set_state(AddTask.deadline)
    await message.answer("Вкажіть дедлайн виконання завдання:", reply_markup=cancel_keyboard)


@tasks_router.message(AddTask.deadline, F.text)
async def add_new_short_description_cmd(message: types.Message,  state: FSMContext):
    await state.update_data(deadline=message.text)
    data = await state.get_data()
    data_to_update = await read_tasks()
    data_to_update.append(data)
    await write_file(data_to_update)
    await message.answer("Чудово! Завдання успішно додано", reply_markup=keyboard)
    await state.clear()

