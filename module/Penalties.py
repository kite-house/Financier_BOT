from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import penalties_json

async def penalties(message):
    button1,button2,button3 = KeyboardButton('Добавить штраф.'), KeyboardButton('Посмотреть штрафы.'), KeyboardButton('Удалить штраф.')
    key_board_mark = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=key_board_mark)


async def add_penalties(message, value):
    try:
        penalties_json.add_penalties(username=message['from']['username'],value = value)
        await message.reply(f'Записал! добавлено в штраф: {value}р.')

    except IndexError or ValueError:
        await message.reply('Введите значение!')

async def read_penalties(message):
    value = penalties_json.read_penalties(username=message['from']['username'])
    await message.reply(f"Сумма штрафов: {value}р.")

async def del_penalties(message, value):
    try:
        penalties_json.del_penalties(username=message['from']['username'],value=value)
        await message.reply(f'Записал! Удалено из штрафа: {value}р.')

    except IndexError or ValueError:
        await message.reply('Введите значение!')