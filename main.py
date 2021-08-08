import random

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='41f09080cb1af69a2d297b4452558b4c40615070d2c3faca34881fc3d0da57466abf92fc1edbdf8cc1826')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
base_keyboard = VkKeyboard(one_time=True)
base_keyboard.add_button('Доходы', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Расходы', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Казна', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_line()
base_keyboard.add_button('Счастье', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Желания', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Досье', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_line()
base_keyboard.add_button('Вызвать секретаря', color=VkKeyboardColor.PRIMARY)
admin_keyboard = VkKeyboard(one_time=True)
admin_keyboard.add_button('Формат запроса', color=VkKeyboardColor.SECONDARY)
admin_keyboard.add_button('Досье', color=VkKeyboardColor.SECONDARY)
admin_keyboard.add_line()
admin_keyboard.add_button('Стоп', color=VkKeyboardColor.NEGATIVE)
admin_keyboard.add_button('Вердить', color=VkKeyboardColor.POSITIVE)
admin_keyboard.add_button('Пропустить', color=VkKeyboardColor.PRIMARY)
time_of_day = ['Доброе утро', 'Добрый день', 'Добрый вечер']
secretary_phrases = ['Звали?', 'Чем могу быть полезна?', 'Чем могу помочь?', 'Что-то случилось?',
                     'Извините, замешкалась. Чем могу помочь?',
                     'Кофейку?', 'Чем могу служить?', 'Что приключилось на этот раз?']

ADMIN_ID = 184272849


def send_income(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message='Суммарный приток в казну Вашей страны за год:\n'
                '\n'
                'Составляющие дохода:\n'
                'Государственные предприятия: (%)\n'
                'НДФЛ: (%)\n'
                'Налог на прибыль организаций: (%)\n'
                'Акцизы: (%)\n'
                'Налоги на имущество: (%)\n'
                'Другие доходы: (%)\n',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_expenses(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message='Суммарный отток из казны Вашей страны за год:\n'
                '\n'
                'Составляющие расхода:\n'
                'Социальная политика: (%)\n'
                'Оборона: (%)\n'
                'Поддержка экономики: (%)\n'
                'Государственный аппарат: (%)\n'
                'Здравоохранение: (%)\n'
                'Образование: (%)\n'
                'Другие расходы: (%)\n',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_treasury(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message='Суммарный бюджет Вашей страны в данный момент эквивалентен\n\n'
                'Тратьте его с осторожностью! Кто знает, какую психосвинью подкинет другой игрок...',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_happiness(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message='Уровень личного счастья Вашего персонажа:\n'
                '\n'
                'Уровень счастья влияет на Вашу харизму, горячность речей и удачу. Каждый день уровень счастья'
                ' снижается, для его увеличения нужно выполнять собственные желания.',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_wishes(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message='Желания Вашего персонажа:\n'
                '\n',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_dossier(user_id=ADMIN_ID):
    vk.messages.send(
        user_id=event.user_id,
        message='Вы открыли папку с досье на каждого персонажа, кого Вы встречали или видели. '
                'Введите имя или прозвище того, чьё досье хотите прочитать:',
        random_id=random.randint(0, 1000000),
        keyboard=(base_keyboard if user_id != ADMIN_ID else admin_keyboard).get_keyboard(),
    )


def call_secretary(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message=f'Секретарь:\n{random.choice(time_of_day)}, правитель! {random.choice(secretary_phrases)}',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_format():
    vk.messages.send(
        user_id=ADMIN_ID,
        message='Формат запроса:\n\n'
                'Страна величина — возвращает значение величины\n'
                'Страна величина +-значение — увеличивает/уменьшает величину на значение\n'
                'Страна величина +-число% — увеличивает/уменьшает величину на число процентов',
        random_id=random.randint(0, 1000000),
        keyboard=admin_keyboard.get_keyboard(),
    )


def send_next():
    # не забудь учесть удаление сообщений игроками
    vk.messages.send(
        user_id=ADMIN_ID,
        message='Щаща',
        random_id=random.randint(0, 1000000),
        keyboard=admin_keyboard.get_keyboard(),
    )


def stop_verding():
    vk.messages.send(
        user_id=ADMIN_ID,
        message='Режим выдачи вердов остановлен.',
        random_id=random.randint(0, 1000000),
        keyboard=admin_keyboard.get_keyboard(),
    )


def start_verding():
    vk.messages.send(
        user_id=ADMIN_ID,
        message='Режим выдачи вердов включен.',
        # добавить правильное обращение. Направляющая и прочее
        random_id=random.randint(0, 1000000),
        keyboard=admin_keyboard.get_keyboard(),
    )


user_actions = {'Доходы': send_income, 'Расходы': send_expenses, 'Казна': send_treasury, 'Счастье': send_happiness,
                'Желания': send_wishes, 'Досье': send_dossier, 'Вызвать секретаря': call_secretary}
admin_actions = {'Формат запроса': send_format, 'Досье': send_dossier, 'Пропустить': send_next, 'Стоп': stop_verding,
                 'Вердить': start_verding}


def user_handler(event):
    if event.text in user_actions:
        user_actions[event.text](event.user_id)
    elif event.text == "Начать":
        vk.messages.send(
            user_id=event.user_id,
            message='Добро пожаловать в Extraterrestrial:Reload! Интересной и приятной игры!',
            random_id=random.randint(0, 1000000),
            keyboard=base_keyboard.get_keyboard(),
        )
    # elif персонаж
    else:
        vk.messages.send(
            user_id=ADMIN_ID,
            message='Тут будет название страны или персонажа',
            random_id=random.randint(0, 1000000),
            keyboard=base_keyboard.get_keyboard(),
            forward_messages=event.message_id,
        )


def admin_handler(event):
    if event.text in admin_actions:
        admin_actions[event.text]()
    elif event.text == "Начать":
        vk.messages.send(
            user_id=event.user_id,
            message='Добро пожаловать в Extraterrestrial:Reload! Интересной и приятной игры!',
            random_id=random.randint(0, 1000000),
            keyboard=admin_keyboard.get_keyboard(),
        )


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
                if event.user_id == ADMIN_ID:
                    admin_handler(event)
                else:
                    user_handler(event)
    except Exception as e:
        print(e)
