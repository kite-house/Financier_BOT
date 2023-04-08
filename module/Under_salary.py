from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import under_salary_json

async def under_salary(message):
    button1 = KeyboardButton('Добавить под зп.')
    button2 = KeyboardButton('Просмотреть все под зп')
    button3 = KeyboardButton('Удалить из под зп')
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=kb)



async def add_under_salary(message, item : str, value: int = 0):
    try:
        if item == 'cofe' or item == 'кофе':
            value = 75
            under_salary_json.write_under_salary(username=message['from']['username'],item = 'cofe', value = value)
            await message.reply(f'Записал! Кофе, {value}р под зп.')

        elif item == 'food' or item == 'еда':
            under_salary_json.write_under_salary(username=message['from']['username'],item = 'food', value = value)
            await message.reply(f'Записал! Еда, {value}р под зп.')

        else: 
            raise IndexError    
    except IndexError or ValueError:
        await message.reply('Введите значение!')


async def read_under_salary(message):
    cofe, food = under_salary_json.read_under_salary(username=message['from']['username'])
    await message.reply(f'Всего потрачено {cofe+food}р под зп, из который {cofe}р на кофе и {food}р на еду')


async def del_under_salary(message):
    try:
        item = str(message.text.split()[1]).lower()
        
        if item == 'cofe' or item == 'кофе':
            value = 75
            under_salary_json.del_under_salary(username=message['from']['username'],item = 'cofe', value = value)
            await message.reply(f'Записал! Удалено кофе из, {value}р под зп.')

        elif item == 'food' or item == 'еда':
            value = int(message.text.split()[2])
            under_salary_json.del_under_salary(username=message['from']['username'],item = 'food', value = value)
            await message.reply(f'Записал! Удалена еда из, {value}р под зп.')

        else: 
            raise IndexError    
        
    except IndexError or ValueError:
        await message.reply('Введите значение!')
