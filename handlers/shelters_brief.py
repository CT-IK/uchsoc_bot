import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message
from database.engine import get_session
from database.models import User
from handlers.make_request import *

sh_router = Router()
responsible_dep = third_dep_list
uni_kb = [[types.KeyboardButton(text='Назад')]]
uni_keyboard = types.ReplyKeyboardMarkup(keyboard=uni_kb, resize_keyboard=True)

class Brief_maker(StatesGroup):
    customer = State()
    customers_tg = State()
    faculty = State()
    num_of_people = State()
    date = State()
    state_of_add = State()
    additional = State()
    rts = State()

    texts = {
        'Brief_maker:customer': 'Введите ФИО заказчика заново:',
        'Brief_maker:customers_tg': 'Введите tg заказчика заново:',
        'Brief_maker:faculty': 'Введите факультет заново:',
        'Brief_maker:num_of_people': 'Введите количество людей заново:',
        'Brief_maker:date': 'Введите желаемую дату заново:'
    }



@sh_router.callback_query(lambda c: c.data == 'shelters_brief_pressed')
async def add_customer(callback:types.CallbackQuery, state:FSMContext):
    await callback.message.answer('Студенческая группа отвечает за:\n\n' \
    '- явку участников и соблюдение правил.\n\n' \
    'УСК отвечает за:\n\n' \
    '- инструктаж и контроль соблюдения правил;\n' \
    '- выделение сопровождение;\n' \
    '- финальную отчётность и общую координацию.\n\n' \
    'Сбор и закупку помощи (корм, вещи и т.д.) осуществляется совместно')
    await callback.message.answer('Введите ФИО заказчика: ')
    await state.set_state(Brief_maker.customer)

@sh_router.message(Brief_maker.customer, F.text)
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(customer=message.text)
    await message.answer('Сохранено!\nВведите tg заказчика: ', reply_markup=uni_keyboard)
    await state.set_state(Brief_maker.customers_tg)

@sh_router.message(Brief_maker.customers_tg, F.text!="Назад")
async def set_department(message:types.Message, state:FSMContext):
    kb = [
        [types.KeyboardButton(text='ВШУ')],
        [types.KeyboardButton(text='ИТиАБД')],
        [types.KeyboardButton(text='ФЭБ')],
        [types.KeyboardButton(text='МЭО')],
        [types.KeyboardButton(text='СНиМК')],
        [types.KeyboardButton(text='НАБ')],
        [types.KeyboardButton(text='Финфак')],
        [types.KeyboardButton(text='Юрфак')],
        [types.KeyboardButton(text='Назад')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)
    await state.update_data(customers_tg=message.text)
    await message.answer('Сохранено!\nВыберите факультет: ', reply_markup=keyboard)
    await state.set_state(Brief_maker.faculty)

@sh_router.message(Brief_maker.faculty, F.text!="Назад")
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(faculty=message.text)
    await message.answer('Сохранено!\nВведите количество людей в группе: ', reply_markup=uni_keyboard)
    await state.set_state(Brief_maker.num_of_people)

@sh_router.message(Brief_maker.num_of_people, F.text!="Назад")
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(num_of_people=message.text)
    await message.answer('Сохранено!\nВведите желаемую дату выезда (в формате ДД.ММ): ', reply_markup=uni_keyboard)
    await state.set_state(Brief_maker.date)

@sh_router.message(Brief_maker.date, F.text!="Назад")
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(date=message.text)
    kb = [
        [types.KeyboardButton(text='Да')],
        [types.KeyboardButton(text='Нет')],
        [types.KeyboardButton(text='Назад')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)
    await message.answer('Сохранено!\nВы хотите ввести дополнительную информацию?', reply_markup=keyboard)
    await state.set_state(Brief_maker.state_of_add)

@sh_router.message(Brief_maker.state_of_add, F.text!="Назад")
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(state_of_add=message.text)
    if message.text == 'Да':
        await message.answer('Введите дополнительную информацию: ', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Brief_maker.additional)
    if message.text == 'Нет':
        await message.answer('Сохранено! Напишите любое сообщение для отправки запроса: ', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Brief_maker.rts)

@sh_router.message(Brief_maker.additional, F.text)
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(additional=message.text)
    await message.answer('Сохранено! Напишите любое сообщение для отправки запроса: ')
    await state.set_state(Brief_maker.rts)

@sh_router.message(Brief_maker.rts, F.text)
async def add_customer(message:types.Message, state:FSMContext):
    await state.update_data(rts=True)
    await message.answer('Запрос сохранен!')
    data = await state.get_data()
    if data.get('additional') == None:
        request = (f'<b>Заявка на выезд в приют:</b>\n\nФИО заказчика: {data.get('customer')}\n\nTG: {data.get('customers_tg')}\n\n'
        f'Факультет: {data.get('faculty')}\n\nКоличество людей в группе: {data.get('num_of_people')}\n\n'
        f'Дата: {data.get('date')}')
    else:
        request = (f'<b>Заявка на выезд в приют:</b>\n\nФИО заказчика: {data.get('customer')}\n\nTG: {data.get('customers_tg')}\n\n'
        f'Факультет: {data.get('faculty')}\n\nКоличество людей в группе: {data.get('num_of_people')}\n\n'
        f'Дата: {data.get('date')}\n\nДополнительная информация: {data.get('additional')}')
    async for session in get_session():
        for user_id in responsible_dep:
            try:
                await message.bot.send_message(chat_id=user_id, text=request, parse_mode=ParseMode.HTML)
            except Exception as e:
                await message.reply(f'Ошибка у {user_id}: {e}')
            await asyncio.sleep(0.05)

        await message.reply('Ваша заявка на выезд в приют отправлена!')
        await state.clear()

# @sh_router.message(StateFilter('*'), Command("Назад"))
@sh_router.message(StateFilter('*'), F.text == 'Назад')
async def back_step_handler(message:types.Message, state:FSMContext):
    current_state = await state.get_state()

    if current_state == Brief_maker.customer:
        await state.clear()
        await message.answer('Студенческая группа отвечает за:\n\n' \
        '- явку участников и соблюдение правил.\n\n' \
        'УСК отвечает за:\n\n' \
        '- инструктаж и контроль соблюдения правил;\n' \
        '- выделение сопровождение;\n' \
        '- финальную отчётность и общую координацию.\n\n' \
        'Сбор и закупку помощи (корм, вещи и т.д.) осуществляется совместно')
        await message.answer('Введите ФИО заказчика: ')
        return

    previous = None
    for step in Brief_maker.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"Предыдущий шаг отменен\n{Brief_maker.texts[previous.state]}")
            return
        previous = step