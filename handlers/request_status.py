import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from database.engine import get_session
from database.models import User

notif_router = Router()
admin_list = ['2131378607', '2011316482']

class Status_notif(StatesGroup):
    recip_id = State()
    content = State()

@notif_router.message(Command('request_status'))
async def set_recipient(message:types.Message, state:FSMContext):
    await message.answer('Введите ID студента: ')
    await state.set_state(Status_notif.recip_id)

@notif_router.message(Status_notif.recip_id, F.text)
async def add_content(message:types.Message, state:FSMContext):
    await state.update_data(recip_id=message.text)
    await message.answer('Сохранено!\nВведите текст оповещения о статусе запроса: ')
    await state.set_state(Status_notif.content)

@notif_router.message(Status_notif.content, F.text)
async def add_content(message:types.Message, state:FSMContext):
    await state.update_data(content=message.text)
    user_id = message.from_user.id
    data = await state.get_data()
    message_for_user = (f'Оповещение о статусе Вашего запроса!\n\n{data.get('content')}')
    
    if str(user_id) not in admin_list:
        await message.reply('Извините, Вы не админ!')
        return
    
    async for session in get_session():
        try:
            await message.bot.send_message(chat_id=data.get('recip_id'), text=message_for_user)
            await message.reply('Сообщение отправлено!')
        except Exception as e:
            await message.reply(f"Ошибка: {e}")
        await state.clear()
