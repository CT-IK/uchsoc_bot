from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


class MenuCallBack(CallbackData, prefix="menu"):
    level: int

def get_user_faq_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Социальные вопросы": "soc_quest",
        "Учебные вопросы": "stud_quest",
    }
    for text, menu_name in btns.items():
        if menu_name == 'soc_quest':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+1).pack()))
        elif menu_name == 'stud_quest':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+2).pack()))
            
    return keyboard.adjust(*sizes).as_markup()

def soc_menu(*, level: int, sizes: tuple[int] = (1,)):
    keyboard = InlineKeyboardBuilder()
    btns = {'Сопровождение студентов с инвалидностью': 'quest_1',
            'Сбор макулатуры: можно ли и когда': 'quest_2',
            'Даты дней донора': 'quest_3',
            'Волонтёрство в приюте': 'quest_4',
            'Соц. стипендия: кто и как оформить': 'quest_5',
            'Назад': 'back',
            }
    for text, menu_name in btns.items():
        if menu_name == 'quest_1':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+2).pack()))
        elif menu_name == 'quest_2':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+3).pack()))
        elif menu_name == 'quest_3':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+4).pack()))
        elif menu_name == 'quest_4':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+5).pack()))
        elif menu_name == 'quest_5':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+6).pack()))
        elif menu_name == 'back':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level*0).pack()))
    return keyboard.adjust(*sizes).as_markup()

def schoolarship(*, level:int, sizes: tuple[int] = (1,)):
    keyboard = InlineKeyboardBuilder()
    btns = {'Для кого соц. стипендия?': 'quest_1',
            'Размер стипендии': 'quest_2',
            'Как оформить?': 'quest_3',
            'Назад': 'back',
            }
    for text, menu_name in btns.items():
        if menu_name == 'quest_1':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+8).pack()))
        elif menu_name == 'quest_2':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+9).pack()))
        elif menu_name == 'quest_3':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+10).pack()))
        elif menu_name == 'back':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level*0).pack()))
    return keyboard.adjust(*sizes).as_markup()

def stud_menu(*, level: int, sizes: tuple[int] = (1,)):
    keyboard = InlineKeyboardBuilder()
    btns = {'Учебный процесс: где смотреть': 'quest_1',
            'Учебные материалы и библиотеки': 'quest_2',
            'Как пользоваться картой студента?': 'quest_3',
            'Контакты университета': 'quest_4',
            'Оплата обучения и общежития': 'quest_5',
            'Студенческий совет': 'quest_6',
            'Перевод и восстановление на бюджет': 'quest_7',
            'Назад': 'back',
            }
    for text, menu_name in btns.items():
        if menu_name == 'quest_1':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+6).pack()))
        elif menu_name == 'quest_2':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+7).pack()))
        elif menu_name == 'quest_3':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+8).pack()))
        elif menu_name == 'quest_4':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+9).pack()))
        elif menu_name == 'quest_5':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+10).pack()))
        elif menu_name == 'quest_6':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+11).pack()))
        elif menu_name == 'quest_7':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level+12).pack()))
        elif menu_name == 'back':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level*0).pack()))
    return keyboard.adjust(*sizes).as_markup()

def faq_all(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {'Назад': 'back'}
    for text, menu_name in btns.items():
        if level in (3,4,5,6,7):
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level*0+1).pack()))
        elif level in (8,9,10,11,12,13,14):
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level*0+2).pack()))
        elif level in (15,16,17):
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallBack(level=level*0+7).pack()))
    return keyboard.adjust(*sizes).as_markup()

def faq_schoolarship(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {'Назад': 'back'}
    for text, menu_name in btns.items():
        keyboard.add(InlineKeyboardButton(text=text,
                callback_data=MenuCallBack(level=(level*0+7)).pack()))
    return keyboard.adjust(*sizes).as_markup()

def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Написать запрос/жалобу", callback_data="make_request_pressed")],
        [InlineKeyboardButton(text="FAQ", callback_data="faq_pressed")],
        [InlineKeyboardButton(text="Бриф на выезды в приюты", callback_data="shelters_brief_pressed")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_start_keyboard_full():
    adm_buttons = [
        [InlineKeyboardButton(text="Написать запрос/жалобу", callback_data="make_request_pressed")],
        [InlineKeyboardButton(text="FAQ", callback_data="faq_pressed")],
        [InlineKeyboardButton(text="Бриф на выезды в приюты", callback_data="shelters_brief_pressed")],
        [InlineKeyboardButton(text="Сделать анонс", callback_data="broadcast_pressed")],
        [InlineKeyboardButton(text="Срочное сообщение", callback_data="urgent_messages_pressed")],
        [InlineKeyboardButton(text="Оповестить студента о статусе запроса/жалобы", callback_data="request_status_pressed")],
        [InlineKeyboardButton(text="Предупредить об изменениях в НПБ", callback_data="npb_update_pressed")]
    ]
    keyboard_adm = InlineKeyboardMarkup(inline_keyboard=adm_buttons)
    return keyboard_adm

def back_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Назад в начальное меню', callback_data='back_start_pressed')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard