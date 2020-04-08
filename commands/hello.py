import command_system
from messageHandler import state

def hello(user_id):
    message = 'Привет, я Сашка. Че хотел?'
    state[user_id] = 0
    return message, ''

hello_command = command_system.Command()

hello_command.keys = ['Привет']
hello_command.process = hello
