import vkapi
import os
import importlib

from command_system import command_list
state = dict()

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body, user_id):
    # Сообщение по умолчанию если распознать не удастся
    # message = "Не понимаю тебя. Напишите НАЧАТЬ, что бы узнать, что нужно сделать"
    message = 0
    attachment = ''
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process(user_id)
    if message == 0:
        message = "не понимаю тебя"

    return message, attachment

def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower(), data["user_id"])
   vkapi.send_message(user_id, token, message, attachment)
   
