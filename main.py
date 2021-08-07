import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token='41f09080cb1af69a2d297b4452558b4c40615070d2c3faca34881fc3d0da57466abf92fc1edbdf8cc1826')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def base_keyboard():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Доходы', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Расходы', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Казна', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Счастье', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Миссии', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Досье', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Вызвать секретаря', color=VkKeyboardColor.POSITIVE)
    return keyboard


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.from_user:
            base_keyboard()
            vk.messages.send(
                user_id=event.user_id,
                message='a',
                random_id=random.randint(0, 1000000),
                keyboard=base_keyboard().get_keyboard(),
            )
