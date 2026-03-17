from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


class MenuCallBack(CallbackData, prefix="menu"):
    level: int

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

def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Запрос или жалоба", callback_data="make_request_pressed")],
        [InlineKeyboardButton(text="FAQ", callback_data="faq_pressed")],
        [InlineKeyboardButton(text="Сделать анонс", callback_data="broadcast_pressed")],
        [InlineKeyboardButton(text="Срочное сообщение", callback_data="urgent_messages_pressed")],
        [InlineKeyboardButton(text="Бриф на выезды в приюты", callback_data="shelters_brief_pressed")],
        [InlineKeyboardButton(text="Оповестить студента о статусе его запроса или жалобы", callback_data="request_status_pressed")],
        [InlineKeyboardButton(text="Предупредить об изменениях в НПБ", callback_data="npb_update_pressed")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def back_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Назад в начальное меню', callback_data='back_start_pressed')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard