from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from settings.setting import SUPER_USER

from module import admin_json
from Logging.logging import Logging
from Logging.logging import logfile

def accept_admin(message):
    accept = False
    for super_user in SUPER_USER:
        if message['from']['username'] == super_user:
            accept = True

    if accept == False:
        return False

async def admin(message):
    accept = accept_admin(message)
    if accept == True:
        await message.reply("Привет любимый!")

    elif accept == False:
        await message.reply("Увы, но ты не наш! Доступ запрещен!")
        return 0

    button1, button2, button3 = KeyboardButton('DataBase'), KeyboardButton('User in DataBase'),\
        KeyboardButton('Log')

    key_board_mark = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=key_board_mark)


async def admin_database(message):
    accept = accept_admin(message)
    if accept == False:
        await message.reply("Доступ запрещен!")
        return 0
    
    database = admin_json.admin_database_json()
    send_database = ''
    for com in database:
        send_database = send_database + com + '\n'
    
    await message.reply(send_database)
    Logging.action('ADMIN_WATCH', 'DATABASE', 'SUCCES')


async def admin_user_database(message, user):
    accept = accept_admin(message)
    if accept == False:
        await message.reply("Доступ запрещен!")
        return 0
    
    user_database = admin_json.admin_user_database_json(user)
    if bool(user_database) == True:
        await message.reply(user_database)
        Logging.action('ADMIN_WATCH_USER', 'DATABASE', 'SUCCES')

    elif user_database == False:
        await message.reply('Пользователь не найден!')
        Logging.action('ADMIN_WATCH_USER', 'DATABASE', 'FAIL')

async def admin_log(message):
    accept = accept_admin(message)
    if accept == False:
        await message.reply("Доступ запрещен!")
        return 0
    
    with open(logfile, 'r') as file:
        data = file.read()
        await message.reply(data)
        file.close()
        Logging.action("ADMIN_WATCH", 'LOG', 'SUCCES')

    
    



