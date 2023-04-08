from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import penalties_json

async def penalties(message):
    button1 = KeyboardButton('Добавить штраф.')
    button2 = KeyboardButton('Посмотреть штрафы.')
    button3 = KeyboardButton('Удалить штраф.')
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=kb)


async def write_penalties(message):
    try:
        value = int(message.text.split()[1])
        penalties_json.write_penalties(username=message['from']['username'],value = value)
        await message.reply(f'Записал! добавлено в штраф: {value}р.')

    except IndexError or ValueError:
        await message.reply('Введите значение!')

async def read_penalties(message):
    value = penalties_json.read_penalties(username=message['from']['username'])
    await message.reply(f"Сумма штрафов: {value}р.")

async def del_penalties(message):
    try:
        value = int(message.text.split()[1])
        penalties_json.del_penalties(username=message['from']['username'],value=value)
        await message.reply(f'Записал! Удалено из штрафа: {value}р.')

    except IndexError or ValueError:
        await message.reply('Введите значение!')