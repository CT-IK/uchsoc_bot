from aiogram import Bot, types, Router
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession

from handlers.menu_processing import get_faq_menu_content

command_faq_router = Router()

@command_faq_router.callback_query(lambda c: c.data == "faq_pressed")
async def faq_cmd(callback: types.CallbackQuery):
    media, reply_markup = await get_faq_menu_content(level=0)

    await callback.message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)