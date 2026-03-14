import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.engine import create_db
from handlers.start import start_router
from handlers.get_id import command_router
from handlers.make_request import req_router
from handlers.FAQ import faq_router
from handlers.FAQ_command import command_faq_router
from handlers.broadcast import broadcast_router
from handlers.urgent_messages import urgent_messages_router
import database.models

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(command_router)
dp.include_router(req_router)
dp.include_router(faq_router)
dp.include_router(command_faq_router)
dp.include_router(broadcast_router)
dp.include_router(urgent_messages_router)


async def main():
    await create_db()
    await dp.start_polling(bot)
    print('Бот запущен')

if __name__ == '__main__':
    asyncio.run(main())