from aiogram import Bot, types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State
import asyncio
from aiogram.fsm.state import StatesGroup
from aiogram.fsm.context import FSMContext
from database.crud import get_all_users
from database.engine import get_session

broadcast_router = Router()

admins_list = []


class Messages_maker(StatesGroup): # MessageMaker
    info = State()
    imge = State()
    rts = State()


@broadcast_router.message(Command("broadcast"))
async def add_content(message:types.Message, state:FSMContext):
    await message.answer("Введите текст анонса: ")
    await state.set_state(Messages_maker.info)

@broadcast_router.message(Messages_maker.info, F.text)
async def add_image(message:types.Message, state:FSMContext):
    await state.update_data(info=message.text)
    await message.answer('Текст анонса сохранён! Пришлите картинку для анонса (если картинка не нужна, то напишите "-"):')
    await state.set_state(Messages_maker.imge)

@broadcast_router.message(Messages_maker.imge, F.photo)
async def save_content(message:types.Message, state:FSMContext):
    await state.update_data(imge=message.photo[-1].file_id)
    await message.answer('Сообщение сохранено! Если картинки не было, напишите "-".\n' \
                         'Если была, то любое другое сообщение.')
    await state.set_state(Messages_maker.rts)

@broadcast_router.message(Messages_maker.imge, F.text == '-')
async def save_content(message:types.Message, state:FSMContext):
    await message.answer('Сообщение сохранено! Если картинки не было, напишите "-".\n' \
                         'Если была, то любое другое сообщение.')
    await state.set_state(Messages_maker.rts)

@broadcast_router.message(Messages_maker.rts, F.text == '-')
async def broadcast_cmd(message: types.Message, state:FSMContext):
    await state.update_data(rts=message.text)
    user_id = message.from_user.id
    data = await state.get_data()
    message_for_users = data.get('info')
    
    if str(user_id) not in admins_list:
        await message.reply('Извините, Вы не админ!')
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
                            f'Не получилось разослать: {failed_count}')
        await state.clear()

@broadcast_router.message(Messages_maker.rts, F.text != '-')
async def broadcast_cmd(message: types.Message, state:FSMContext):
    await state.update_data(rts=message.text)
    user_id = message.from_user.id
    data = await state.get_data()
    message_for_users = data.get('info')
    image_for_users = data.get('imge')
    
    if str(user_id) not in admins_list:
        await message.reply('Извините, Вы не админ!')
        return
    
    async for session in get_session():
        users = await get_all_users(session)
        sent_count = 0
        failed_count = 0

        for user_id in users:
            try:
                await message.bot.send_photo(chat_id=user_id, caption=message_for_users, photo=image_for_users)
                sent_count += 1
            except Exception as e:
                await message.reply(f"Ошибка у {user_id} : {e}")
                failed_count += 1
            await asyncio.sleep(0.05)

        await message.reply(f'Рассылка завершена!\n\n'
                            f'Успешно разослано: {sent_count}\n'
                            f'Не получилось разослать: {failed_count}')
        await state.clear()