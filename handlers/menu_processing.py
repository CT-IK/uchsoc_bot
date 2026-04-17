from aiogram.types import InputMediaPhoto

from keyboards.inline import get_user_faq_btns, faq_all, soc_menu, stud_menu, schoolarship, faq_schoolarship


async def faq_menu(level):
    image = InputMediaPhoto(media='https://i.ytimg.com/vi/YjOI4owwGR4/maxresdefault.jpg', caption='Выберите раздел вопросов:')

    kbds = get_user_faq_btns(level=level)

    return image, kbds

async def soc_quest(level):
    image = InputMediaPhoto(media='https://bcagl.org/wp-content/uploads/2020/01/faq-banner.jpg', caption='В данном разделе представлены основные социальные вопросы ')

    kbds = soc_menu(level=level)

    return image, kbds

async def stud_quest(level):
    image = InputMediaPhoto(media='https://img.freepik.com/premium-photo/high-angle-view-text-paper_1048944-18304189.jpg?semt=ais_hybrid&w=740&q=80', caption='В данном разделе представлены основные учебные вопросы')

    kbds = stud_menu(level=level)

    return image, kbds

async def soc_1(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Да. Обратиться по данному вопросу можно в Управление социальной работой (напрямую или через деканат). 

Кто отвечает:
    В структуре университета есть Управление социальной работы, которое курирует вопросы поддержки студентов с инвалидностью и ОВЗ. Непосредственно за сопровождение отвечает специалист по сопровождению инвалидов. 

Что входит в сопровождение: 

    1)Помощь в передвижении по территории и внутри корпусов 

    2)Содействие в адаптации к учебному процессу 

    3)Консультирование по вопросам получения социальных выплат и льгот 

    4)Организация помощи ассистентов при необходимости 

  ''')

    kbds = faq_all(level=level)

    return image, kbds

async def soc_2(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Можно, но только в период объявленных акций.
                            
Сбор макулатуры проводится один раз в семестр.
                            
Следите за анонсами в телеграм-канале Учебно-социального комитета.''')

    kbds = faq_all(level=level)

    return image, kbds

async def soc_3(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Ближайший День донора в 2026 году — 6 октября. Акция проходит в главном корпусе (Ленинградский пр-т, 49, холл 1 этажа, клиника "Универсум"). При себе: паспорт и СНИЛС. После сдачи крови полагается день отдыха. 

Основные даты Дней донора: 4 марта и 6 октября. 

Ссылка на пост УСК, посвященный дню донора: https://vk.com/wall-235640835_35  

Как подготовиться и записаться: 

    Перед донацией рекомендуется ознакомиться с рекомендациями (достаточный сон, лёгкий завтрак, исключение алкоголя за 48 часов).
                            
    Запись на День донора обычно открывается за несколько дней до акции — следите за объявлениями в телеграм-канале Учебно-социального комитета и на сайте университета.''')

    kbds = faq_all(level=level)

    return image, kbds

async def soc_4(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Да. Учебно-социальный комитет регулярно организует выезды в приюты. Чтобы присоединиться, заполните бриф.''')

    kbds = faq_all(level=level)

    return image, kbds

async def soc_5(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Что хотите узнать о социальной стипендии?''')

    kbds = schoolarship(level=level)

    return image, kbds

async def schoolarship_1(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Государственная социальная стипендия назначается студентам очной бюджетной формы обучения, которые относятся к одной из категорий: 

    1)Дети-сироты и дети, оставшиеся без попечения родителей (до 23 лет); 

    2)Инвалиды I и II групп, инвалиды с детства; 

    3)Лица, пострадавшие от радиационных катастроф (Чернобыль, Семипалатинск и др.); 

    4)Ветераны боевых действий; 

    5)Студенты, получающие государственную социальную помощь (малообеспеченные семьи) — для этого нужна справка из органов соцзащиты''')

    kbds = faq_schoolarship(level=level)

    return image, kbds

async def schoolarship_2(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Размер стипендии:
    Базовая государственная академическая стипендия составляет 2419 ₽ для студентов на «хорошо» и 3629 ₽ для отличников.
    
    Для студентов 1–2 курсов, имеющих право на соцстипендию, предусмотрена повышенная стипендия, суммарный размер которой должен быть не менее прожиточного минимума (в 2025–2026 учебном году — порядка 14 000–16 000 ₽ в месяц).''')

    kbds = faq_schoolarship(level=level)

    return image, kbds

async def schoolarship_3(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Как оформить: 

    1)Собрать документы: 

        a)Справка из соцзащиты о признании семьи малообеспеченной (для тех, кто претендует по этому основанию); 

        б)Или документы, подтверждающие льготную категорию (удостоверение инвалида, справка об участии в боевых действиях, справка из органов опеки и т.д.); 

        в)Паспорт, студенческий билет 

    2)Написать заявление в деканат своего факультета 

    3)Деканат передаёт документы в Стипендиальную комиссию, которая принимает решение о назначении выплаты 

Стипендия назначается с момента подачи заявления и выплачивается ежемесячно в течение семестра. При необходимости продления на следующий семестр нужно обновить документы.''')

    kbds = faq_schoolarship(level=level)

    return image, kbds

async def stud_1(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''В главном меню сайта необходимо нажать кнопку «Студентам». 

Ссылка: https://www.fa.ru/for-students/''')

    kbds = faq_all(level=level)

    return image, kbds

async def stud_2(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''В главном меню сайта нужно нажать кнопку «Библиотека» и выбрать необходимый материал. 

Ссылка: http://www.library.fa.ru ''')

    kbds = faq_all(level=level)

    return image, kbds

async def stud_3(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Электронная карта студента используется для доступа на объекты Финансового университета в соответствии с установленным графиком посещения зданий. 

Для прохода через турникеты, установленные на входе в здания университета, необходимо: 

    - поднести карту параллельно считывающему устройству; 

    - дождаться появления зелёного сигнала; 

    - после этого пройти через турникет. 

Время входа и выхода фиксируется системой. При проходе через турникет на мониторе поста охраны отображается фотография владельца карты. 

Передача карты другим лицам (проход по чужой карте) запрещена и влечёт применение административных мер, вплоть до отчисления или увольнения.''')

    kbds = faq_all(level=level)

    return image, kbds

async def stud_4(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Для этого необходимо прокрутить главную страницу сайта вниз до раздела с контактной информацией. 

Ссылка: https://www.fa.ru/university/contacts/''')

    kbds = faq_all(level=level)

    return image, kbds

async def stud_5(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Необходимо перейти:

Меню → Студентам → Оплата обучения и общежития. 

Ссылка: https://www.fa.ru/for-students/oplata/''')

    kbds = faq_all(level=level)

    return image, kbds

async def stud_6(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Студенческий совет — крупнейшая общественная студенческая организация университета, созданная с целью формирования активной гражданской позиции студентов, развития их самостоятельности, навыков самоорганизации и саморазвития. 

Ежегодно Студенческий совет организует более 100 досуговых, образовательных, социальных и спортивных мероприятий и проектов, среди которых: 

    - проект адаптации первокурсников «Координаторство»; 

    - «Квест первокурсника»; 

    - обучающие программы по развитию навыков самоуправления («Школа актива», «Школа актива Второго уровня»); 

    - Большой студенческий бал; 

    - городской фестиваль уличной культуры «Urban Culture Fest»; 

    - и прочие, ссылка для ознакомления: https://www.fa.ru/for-students/sst/''')

    kbds = faq_all(level=level)

    return image, kbds

async def stud_7(level):
    image = InputMediaPhoto(media='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FNc0R_uiJpyU%2Fmaxresdefault.jpg&lr=21651&p=3&pos=7&rpt=simage&text=ответы%20фото', caption='''Перевод на бюджет — это конкурсная процедура. Чтобы не запутаться, есть официальный алгоритм: 

    Шаг 1. Обратитесь в деканат. Это самая главная инстанция. Сотрудники деканата скажут, есть ли свободные бюджетные места на вашем направлении. 

    Шаг 2. Изучите официальный документ. Вся процедура регламентирована Приказом Финуниверситета. Найдите документ «О порядке перехода с платного обучения на бесплатное» на сайте fa.ru в разделе «Сведения об образовательной организации» → «Документы» → «Локальные нормативные акты». 

    Шаг 3. Подайте заявление. Напишите заявление на имя ректора и приложите копию зачётной книжки. 

Кто может претендовать? Студенты без «троек», долгов и взысканий при наличии свободного бюджетного места.''')

    kbds = faq_all(level=level)

    return image, kbds


async def get_faq_menu_content(
    level: int
):
    if level == 0:
        return await faq_menu(level)
    elif level == 1:
        return await soc_quest(level)
    elif level == 2:
        return await stud_quest(level)
    elif level == 3:
        return await soc_1(level)
    elif level == 4:
        return await soc_2(level)
    elif level == 5:
        return await soc_3(level)
    elif level == 6:
        return await soc_4(level)
    elif level == 7:
        return await soc_5(level)
    elif level == 8:
        return await stud_1(level)
    elif level == 9:
        return await stud_2(level)
    elif level == 10:
        return await stud_3(level)
    elif level == 11:
        return await stud_4(level)
    elif level == 12:
        return await stud_5(level)
    elif level == 13:
        return await stud_6(level)
    elif level == 14:
        return await stud_7(level)
    elif level == 15:
        return await schoolarship_1(level)
    elif level == 16:
        return await schoolarship_2(level)
    elif level == 17:
        return await schoolarship_3(level)