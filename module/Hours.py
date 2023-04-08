from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import hours_json, bet_json

async def hours(message):
    button1 = KeyboardButton('Добавить часов.')
    button2 = KeyboardButton('Посмотреть кол-во часов.')
    button3 = KeyboardButton('Удалить часы')
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=kb)


async def write_hours(message):
    try:
        value = int(message.text.split()[1])
        hours_json.write_hours(username=message['from']['username'],value = value)
        bet = bet_json.read_bet(username=message['from']['username'])
        await message.reply(f'Записал! Количество отработаных часов: {value}, заработано денег: {value * bet}р.')
        
    except IndexError or ValueError:
        await message.reply('Введите значение!')


async def read_hours(message):
    value = hours_json.read_hours(username=message['from']['username'])
    bet = bet_json.read_bet(username=message['from']['username'])
    await message.reply(f"Количество всего отработаных часов: {value}, всего заработано денег {value * bet}р.")


async def del_hours(message):
    try:
        value = int(message.text.split()[1])
        hours_json.del_hours(username=message['from']['username'],value=value)
        await message.reply(f'Записал! Удалено часов: {value}.')

    except IndexError or ValueError:
        await message.reply('Введите значение!')