import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(token='41f09080cb1af69a2d297b4452558b4c40615070d2c3faca34881fc3d0da57466abf92fc1edbdf8cc1826')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': 
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    message='Ваш текст',
                    random_id=random.randint(0, 1000000)
                )
