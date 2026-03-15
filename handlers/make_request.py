import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from database.engine import get_session
from database.models import User

req_router = Router()
first_dep_list = ['2131378607']
sec_dep_list = []
third_dep_list = ['2131378607']

class Message_maker(StatesGroup):
    user_id = State()
    department = State()
    content = State()

@req_router.message(Command('make_request'))
async def set_department(message:types.Message, state:FSMContext):
    await message.answer('Я живой')
    await state.update_data(user_id=message.from_user.id)
    kb = [
        [types.KeyboardButton(text='Какое-то подразделение')],
        [types.KeyboardButton(text='Еще какое-то подразделение')],
        [types.KeyboardButton(text='И еще одно подразделение')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder='Выберите одно из подразделений:')
    await message.answer('Вы можете отправить жалобу следующим подразделениям УСК:\n\n' \
    '+ какое-то подразделение - занимается тем-то, тем-то, тем-то\n' \
    '+ еще какое-то подразделение - занимается этим, этим и этим\n' \
    '+ и еще одно подразделение - отважно выполняет это, это и это', reply_markup=keyboard)
    await state.set_state(Message_maker.department)

@req_router.message(Message_maker.department, F.text)
async def add_content(message:types.Message, state:FSMContext):
    await state.update_data(department=message.text)
    await message.answer(f'Вы выбрали {message.text}!\n', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Далее введите текст запроса: ')
    await state.set_state(Message_maker.content)

@req_router.message(Message_maker.content, F.text)
async def ready_to_send(message:types.Message, state:FSMContext):
    await state.update_data(content=message.text)
    await message.answer('Запрос сохранен!')
    data = await state.get_data()
    request = f'Запрос к {data.get('department')}:\n\n{data.get("content")}\n\n' \
            f'ID отправителя: {data.get('user_id')}'
    async for session in get_session():
        if data.get('department') == 'Какое-то подразделение':
            recipients = first_dep_list
        if data.get('department') == 'Еще какое-то подразделение':
            recipients = sec_dep_list
        if data.get('department') == 'И еще одно подразделение':
            recipients = third_dep_list
        else:
            print('Ошибка в data.get("department")')
        for user_id in recipients:
            try:
                await message.bot.send_message(chat_id=user_id, text=request)
            except Exception as e:
                await message.reply(f'Ошибка у {user_id}: {e}')
            await asyncio.sleep(0.05)

        await message.reply('Ваш запрос успешно отправлен!')
        await state.clear()