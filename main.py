import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token='41f09080cb1af69a2d297b4452558b4c40615070d2c3faca34881fc3d0da57466abf92fc1edbdf8cc1826')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
base_keyboard = VkKeyboard(one_time=True)
base_keyboard.add_button('Доходы', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Расходы', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Казна', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_line()
base_keyboard.add_button('Счастье', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Миссии', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_button('Досье', color=VkKeyboardColor.SECONDARY)
base_keyboard.add_line()
base_keyboard.add_button('Вызвать секретаря', color=VkKeyboardColor.PRIMARY)
time_of_day = ['Доброе утро', 'Добрый день', 'Добрый вечер']
secretary_phrases = ['Звали?', 'Чем могу быть полезна?', 'Чем могу помочь?', 'Что-то случилось?',
                     'Извините, замешкалась. Чем могу помочь?',
                     'Кофейку?', 'Чем могу служить?', 'Что приключилось на этот раз?']


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


def send_happiness(user_id):
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


def send_missions(user_id):
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


def send_dossier(user_id):
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


def call_secretary(user_id):
    vk.messages.send(
        user_id=event.user_id,
        message=f'Секретарь:\n{random.choice(time_of_day)}, правитель! {random.choice(secretary_phrases)}',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


actions = {'Доходы': send_income, 'Расходы': send_expenses, 'Казна': send_treasury, 'Счастье': send_happiness,
           'Миссии': send_missions, 'Досье': send_dossier, 'Вызвать секретаря': call_secretary}
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
        if event.text in actions:
            actions[event.text](event.user_id)
        elif event.text == "Начать":
            vk.messages.send(
                user_id=event.user_id,
                message='Добро пожаловать в Extraterrestrial:Reload! Интересной и приятной игры!',
                random_id=random.randint(0, 1000000),
                keyboard=base_keyboard.get_keyboard(),
            )
