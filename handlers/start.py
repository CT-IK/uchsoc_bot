from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

from database.crud import get_or_create_user
from database.engine import get_session

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message:types.Message):
    await message.answer('Привет! Это бот Учебно-социального комитета.\n' \
            '/make_request - отправьте запрос или жалобу\n' \
                '/faq - просмотреть FAQ\n' \
                    '/broadcast - анонсировать мероприятия\n' \
                        '/urgent_messages - опубликовать срочные сообщения\n' \
                            '/shelters_brief - заполнить бриф на выезды в приюты\n'\
                            '/request_status - оповестить студента о статусе его запроса или жалобы\n'\
                            '/npb_update - предупредить об изменениях в НПБ')
    user_id = message.from_user.id
    async for session in get_session():
        user = await get_or_create_user(session, user_id)
        if user:
            await message.answer('Ваш Telegram ID записан в базу данных!')
        else:
            await message.answer('Ваш ID уже в нашей базе данных!')