from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import bet_json

async def bet(message):
    button1,button2 = KeyboardButton('Посмотреть ставку.'), KeyboardButton('Изменить ставку.')
    key_board_mark = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2)
    await message.answer('Что сделаем?', reply_markup=key_board_mark)


async def watch_bet(message):
    value = bet_json.read_bet(username=message['from']['username'])
    await message.reply(f"Ваша часовая ставка: {value}р в час.")


async def editing_bet(message, value):
    try:
        bet_json.editing_bet(username=message['from']['username'], value= value)
        await message.reply(f"Ставка изменена на {value}р в час")
        
    except IndexError or ValueError:
        await message.reply('Введите значение!')