from vk_api.longpoll import VkEventType

from actions import *

user_actions = {'Доходы': send_income, 'Расходы': send_expenses, 'Казна': send_treasury, 'Счастье': send_happiness,
                'Желания': send_wishes, 'Досье': send_dossier, 'Вызвать секретаря': call_secretary}
admin_actions = {'Формат запроса': send_format, 'Досье': send_dossier, 'Пропустить': send_next, 'Стоп': stop_verding,
                 'Вердить': start_verding, 'Добавить персонажа': add_character}


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
