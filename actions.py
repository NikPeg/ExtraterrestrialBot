import random
from constants import *


def send_income(user_id):
    vk.messages.send(
        user_id=user_id,
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
        user_id=user_id,
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
        user_id=user_id,
        message='Суммарный бюджет Вашей страны в данный момент эквивалентен\n\n'
                'Тратьте его с осторожностью! Кто знает, какую психосвинью подкинет другой игрок...',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_happiness(user_id):
    vk.messages.send(
        user_id=user_id,
        message='Уровень личного счастья Вашего персонажа:\n'
                '\n'
                'Уровень счастья влияет на Вашу харизму, горячность речей и удачу. Каждый день уровень счастья'
                ' снижается, для его увеличения нужно выполнять собственные желания.',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_wishes(user_id):
    vk.messages.send(
        user_id=user_id,
        message='Желания Вашего персонажа:\n'
                '\n',
        random_id=random.randint(0, 1000000),
        keyboard=base_keyboard.get_keyboard(),
    )


def send_dossier(user_id=ADMIN_ID):
    vk.messages.send(
        user_id=user_id,
        message='Вы открыли папку с досье на каждого персонажа, кого Вы встречали или видели. '
                'Введите имя или прозвище того, чьё досье хотите прочитать:',
        random_id=random.randint(0, 1000000),
        keyboard=(base_keyboard if user_id != ADMIN_ID else admin_keyboard).get_keyboard(),
    )


def call_secretary(user_id):
    vk.messages.send(
        user_id=user_id,
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


def add_character():
    vk.messages.send(
        user_id=ADMIN_ID,
        message='Введите информацию о персонаже в формате:\n'
                'name, age, description, personality, marriage, post, country',
        random_id=random.randint(0, 1000000),
        keyboard=admin_keyboard.get_keyboard(),
    )
