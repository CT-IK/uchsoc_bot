from aiogram import Bot, types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State
import asyncio
from aiogram.fsm.state import StatesGroup
from aiogram.fsm.context import FSMContext
from database.crud import get_all_users
from database.engine import get_session
from keyboards.inline import back_start_keyboard

urgent_messages_router = Router()

admins_list = []


class Urgent_messages_maker(StatesGroup): # MessageMaker
    info = State()
    rts = State()


@urgent_messages_router.callback_query(lambda c: c.data == 'urgent_messages_pressed')
async def add_content(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer("Введите текст срочного сообщения: ")
    await state.set_state(Urgent_messages_maker.info)

@urgent_messages_router.message(Urgent_messages_maker.info, F.text)
async def save_content(message:types.Message, state:FSMContext):
    await state.update_data(info=message.text)
    await message.answer("Сообщение сохранено! Напишите любое сообщение для продолжения:")
    await state.set_state(Urgent_messages_maker.rts)

@urgent_messages_router.message(Urgent_messages_maker.rts, F.text)
async def broadcast_cmd(message: types.Message, state:FSMContext):
    await state.update_data(rts=message.text)
    user_id = message.from_user.id
    data = await state.get_data()
    message_for_users = data.get('info')
    
    if str(user_id) not in admins_list:
        await message.reply('Извините, Вы не админ!', reply_markup=back_start_keyboard())
        return
    
    async for session in get_session():
        users = await get_all_users(session)
        sent_count = 0
        failed_count = 0

        for user_id in users:
            try:
                await message.bot.send_message(chat_id=user_id, text=message_for_users)
                sent_count += 1
            except Exception as e:
                await message.reply(f"Ошибка у {user_id} : {e}")
                failed_count += 1
            await asyncio.sleep(0.05)

        await message.reply(f'Рассылка завершена!\n\n'
                            f'Успешно разослано: {sent_count}\n'
                            f'Не получилось разослать: {failed_count}', reply_markup=back_start_keyboard())
        await state.clear()