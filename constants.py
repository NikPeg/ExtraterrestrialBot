import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll

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
admin_keyboard.add_button('Добавить персонажа', color=VkKeyboardColor.SECONDARY)
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
