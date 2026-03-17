from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.inline import get_start_keyboard, get_start_keyboard_full

from database.crud import get_or_create_user
from database.engine import get_session

start_router = Router()
# full_access_list = [2131378607,]
full_access_list = []

@start_router.callback_query(lambda c: c.data == 'back_start_pressed')
async def start_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id in full_access_list:
        await callback.message.answer(
            "Выберите подходящую функцию ниже:",
            reply_markup=get_start_keyboard_full()
        )
    else:
        await callback.message.answer(
            "Выберите подходящую функцию ниже:",
            reply_markup=get_start_keyboard()
        )

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    async for session in get_session():
        user = await get_or_create_user(session, user_id)
        if user:
            await message.answer('Ваш Telegram ID записан в базу данных!')
        else:
            await message.answer('Ваш ID уже в нашей базе данных!')
    if user_id in full_access_list:
        await message.answer(
            "Привет! Это бот Учебно-социального комитета!",
            reply_markup=get_start_keyboard_full()
        )
    else:
        await message.answer(
            "Привет! Это бот Учебно-социального комитета!",
            reply_markup=get_start_keyboard()
        )