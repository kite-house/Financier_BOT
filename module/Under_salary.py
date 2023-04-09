from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from module import under_salary_json

async def under_salary(message):
    button1, button2,button3 = KeyboardButton('Добавить под зп.'), KeyboardButton('Просмотреть все под зп'), KeyboardButton('Удалить из под зп')
    key_board_mark = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3)
    await message.answer('Что сделаем?', reply_markup=key_board_mark)



async def add_under_salary(message, item : str, value = 0):
    try:
        if item == 'cofe':
            under_salary_json.write_under_salary(username=message['from']['username'],item = 'cofe', value = 75)
            await message.reply(f'Записал! Кофе, {value}р под зп.')

        elif item == 'food':
            under_salary_json.write_under_salary(username=message['from']['username'],item = 'food', value = value)
            await message.reply(f'Записал! Еда, {value}р под зп.')

        else: 
            raise IndexError    
    except IndexError or ValueError:
        await message.reply('Введите значение!')


async def read_under_salary(message):
    cofe, food = under_salary_json.read_under_salary(username=message['from']['username'])
    await message.reply(f'Всего потрачено {cofe+food}р под зп, из который {cofe}р на кофе и {food}р на еду')


async def del_under_salary(message, item : str, value = 0):
    try:
        if item == 'cofe':
            under_salary_json.del_under_salary(username=message['from']['username'],item = 'cofe', value = 75)
            await message.reply(f'Записал! Удалено кофе из, {value}р под зп.')

        elif item == 'food':
            under_salary_json.del_under_salary(username=message['from']['username'],item = 'food', value = value)
            await message.reply(f'Записал! Удалена еда из, {value}р под зп.')

        else: 
            raise IndexError    
        
    except IndexError or ValueError:
        await message.reply('Введите значение!')
