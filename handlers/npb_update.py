import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import Message
from database.engine import get_session
from database.models import User
from database.crud import get_all_users

npb_router = Router()
admin_list = ['2131378607', '2011316482']

class Npb_upd(StatesGroup):
    content = State()

@npb_router.callback_query(lambda c: c.data == 'npb_update_pressed')
async def set_recipient(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer('Введите содержание изменения в НПБ: ')
    await state.set_state(Npb_upd.content)

@npb_router.message(Npb_upd.content, F.text)
async def add_content(message:types.Message, state:FSMContext):
    await state.update_data(content=message.text)
    user_id = message.from_user.id
    data = await state.get_data()
    message_for_users = (f'<b>Оповещение об изменениях в НПБ!</b>\n\n{data.get('content')}')
    
    if str(user_id) not in admin_list:
        await message.reply('Извините, Вы не админ!')
        return
    
    async for session in get_session():
        users = await get_all_users(session)
        sent_count = 0
        failed_count = 0

        for user_id in users:
            try:
                await message.bot.send_message(chat_id=user_id, text=message_for_users, parse_mode=ParseMode.HTML)
                sent_count += 1
            except Exception as e:
                await message.reply(f"Ошибка у {user_id} : {e}")
                failed_count += 1
            await asyncio.sleep(0.05)

        await message.reply(f'Рассылка завершена!\n\n'
                            f'Успешно разослано: {sent_count}\n'
                            f'Не получилось разослать: {failed_count}')
        await state.clear()