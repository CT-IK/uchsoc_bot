from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    page: int = 1

def get_user_faq_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "1 вопрос": "first_faq",
    }
    for text, menu_name in btns.items():
        if menu_name == 'first_faq':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+1).pack()))
            
    return keyboard.adjust(*sizes).as_markup()

def faq_all(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {'Назад': 'back'}
    for text, menu_name in btns.items():
        keyboard.add(InlineKeyboardButton(text=text,
                callback_data=MenuCallBack(level=level*0).pack()))
    return keyboard.adjust(*sizes).as_markup()