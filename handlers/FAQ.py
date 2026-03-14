from aiogram import Bot, types, Router, F
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession

from handlers.menu_processing import get_faq_menu_content

from keyboards.inline import MenuCallBack


faq_router = Router()

@faq_router.callback_query(MenuCallBack.filter())
async def faq_menu(callback: types.CallbackQuery, callback_data: MenuCallBack):

    media, reply_markup = await get_faq_menu_content(
        level=callback_data.level
    )

    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()