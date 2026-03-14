from aiogram.types import InputMediaPhoto

from keyboards.inline import get_user_faq_btns, faq_all


async def faq_menu(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fberchem.brussels%2Fwp-content%2Fuploads%2F2020%2F10%2FFAQ-1.png&lr=21651&pos=6&rpt=simage&text=faq', caption='FAQ')

    kbds = get_user_faq_btns(level=level)

    return image, kbds

async def first_faq(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fu.livelib.ru%2Falbum%2F1000010253%2Fo%2Fxefynkho%2Fo-o.jpeg&lr=49&pos=7&rpt=simage&text=faq', caption='Инфа')

    kbds = faq_all(level=level)

    return image, kbds


async def get_faq_menu_content(
    level: int
):
    if level == 0:
        return await faq_menu(level)
    elif level == 1:
        return await first_faq(level)