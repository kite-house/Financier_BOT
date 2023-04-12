from module import salary_json
from Logging.logging import Logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime

month_str = {
    "1" : 'Январь',
    '2' : 'Февраль',
    '3' : 'Март',
    '4' : 'Апрель',
    '5' : 'Май', 
    '6' : 'Июнь',
    '7' : 'Июль',
    '8' : 'Август', 
    '9' : 'Сентябрь',
    '10' : 'Октябрь',
    '11' : 'Ноябрь',
    '12' : 'Декабрь'
    }

async def hi_salary(message):
    button1,button2 = KeyboardButton('Зарплата за текущий месяц.'), KeyboardButton('Зарплата за прошлый месяц.')
    key_board_mark = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2)
    await message.answer('Что сделаем?', reply_markup=key_board_mark)


async def salary(message, value, datetime = datetime):
    if value == 0:
        datetime = str(datetime.now().month)
    elif datetime != 0:
        datetime = str(value)
    try:
        hours, bet, penalties, cofe, food = salary_json.load_selery(username=message['from']['username'], datetime = datetime)
        salary = (hours * bet) - (penalties + cofe + food)
        await message.reply(f"Зарплата за {month_str[datetime]}: \
                            \n=========================================================\
                            \nОтработана часов: {hours}, заработана за часы {hours * bet}р, при ставке {bet}р в час. \
                            \nШтраф на сумму: {penalties}р.\nПотрачено всего под зп: {cofe+food}р, из которых {cofe}р на кофе и {food}р на еду. \
                            \nОбщая сумма: {salary}р \
                            \n=========================================================")
        Logging.action("WATCH", 'SALARY', 'SUCCES')
    except Exception:
        await message.reply("Данные не найдены!")