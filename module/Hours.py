from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import hours_json, bet_json
from Logging.logging import Logging

async def hours(message):
    button1, button2, button3 = KeyboardButton('Добавить часов.'), KeyboardButton('Посмотреть кол-во часов.'), KeyboardButton('Удалить часы')
    key_board_mark = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=key_board_mark)


async def add_hours(message, value):
    try:
        hours_json.add_hours(username=message['from']['username'],value = value)
        bet = bet_json.read_bet(username=message['from']['username'])
        await message.reply(f'Записал! Количество отработаных часов: {value}, заработано денег: {value * bet}р.')
        Logging.action('ADD', 'HOURS', 'SUCCES')

    except IndexError or ValueError:
        await message.reply('Введите значение!')
        Logging.action('ADD', 'HOURS', 'FAIL')


async def read_hours(message):
    value = hours_json.read_hours(username=message['from']['username'])
    bet = bet_json.read_bet(username=message['from']['username'])
    await message.reply(f"Количество всего отработаных часов: {value}, всего заработано денег {value * bet}р.")
    Logging.action('WATCH', 'HOURS', 'SUCCES')


async def del_hours(message, value):
    try:
        hours_json.del_hours(username=message['from']['username'],value=value)
        await message.reply(f'Записал! Удалено часов: {value}.')
        Logging.action('DELETE', 'HOURS', 'SUCCES')

    except IndexError or ValueError:
        await message.reply('Введите значение!')
        Logging.action('DELETE', 'HOURS', 'FAIL')