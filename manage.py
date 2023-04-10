from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from Logging.logging import Logging

from module import Bet, Hours, Penalties, Salary, Under_salary, Admin
from settings import load_token
from DataBase import db

bot = Bot(token=load_token.api_token())
dp = Dispatcher(bot)

Logging.start()

ALL_COMMANDS = ['/start - Приветствие', 
                '/help - Помощь',
                'Часы - Управление часами(Добавить/посмотреть/удалить)', 
                'Штрафы - Управление штрафом(Добавить/посмотреть/удалить)', 
                'Под зп - Управление подзп(Добавить/посмотреть/удалить)',
                'Зарплата - Посмотреть рассчёт зп',
                'Cтавка - Управление ставкой(Добавить/посмотреть)']

def HELP(ALL_COMMANDS):
    HELP = ''
    for com in ALL_COMMANDS:
        HELP = HELP + com + '\n'
    
    return HELP

# FAST COMMANDS
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    username = (message['from']['username'])
    db.create_new_user_database(username)
    hours,penalties,under_salary,salary,bet = KeyboardButton('Часы'), KeyboardButton('Штрафы'), KeyboardButton('Подзп'), KeyboardButton('Зарплата'), KeyboardButton('Ставка')
    start_rm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(hours,penalties,under_salary,salary,bet)
    await message.reply(f"Привет, {message['from']['first_name']}! Я бот, который может помочь тебе с расчётом зарплаты!. Используй /help для просмотра всех команд!", reply_markup=start_rm)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(HELP(ALL_COMMANDS))


@dp.message_handler(lambda message: message.text == 'Меню')
async def menu(message: types.Message):
    hours,penalties,under_salary,salary,bet = KeyboardButton('Часы'), KeyboardButton('Штрафы'), KeyboardButton('Подзп'), KeyboardButton('Зарплата'), KeyboardButton('Ставка')
    start_rm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(hours,penalties,under_salary,salary,bet)
    await message.reply(f'Что выберим?', reply_markup=start_rm)

# SUPERUSER - ADMIN


@dp.message_handler(lambda message: message.text == 'Админ')
async def admin(message: types.Message):
    await Admin.admin(message)

@dp.message_handler(lambda message: message.text == 'DataBase')
async def admin_database(message: types.Message):
    await Admin.admin_database(message)

@dp.message_handler(lambda message: message.text == 'User in DataBase')
async def admin_user_in_database(message: types.Message):
    await message.reply("Введите username")
    global state
    state = 'ADMIN_user_in_database'

@dp.message_handler(lambda message: message.text == 'Log')
async def admin_log(message: types.Message):
    await Admin.admin_log(message)

@dp.message_handler(lambda message: message.text == 'CrashLog')
async def admin_crashlog(message: types.Message):
    await Admin.admin_crash_log(message)

# ===


# Часы ++

@dp.message_handler(lambda message: message.text == 'Часы')
async def hours(message: types.Message):
    await Hours.hours(message)


@dp.message_handler(lambda message: message.text == 'Добавить часов.')
async def add_hours(message: types.Message):
    await message.reply('Сколько часов добавляем?: ')
    global state
    state = 'add_hours'


@dp.message_handler(lambda message: message.text == 'Посмотреть кол-во часов.')
async def watch_hours(message: types.Message):
    await Hours.read_hours(message)


@dp.message_handler(lambda message: message.text == 'Удалить часы')
async def del_hours(message: types.Message):
    await message.reply('Сколько часов удаляем?: ')
    global state
    state = 'del_hours'

# Штраф

@dp.message_handler(lambda message: message.text == 'Штрафы')
async def penalties(message: types.Message):
    await Penalties.penalties(message)


@dp.message_handler(lambda message: message.text == 'Добавить штраф.')
async def add_penalties_text(message):
    await message.reply("Введите сумму: ")
    global state 
    state = 'add_penalties'



@dp.message_handler(lambda message: message.text == 'Посмотреть штрафы.')
async def watch_penalties(message: types.Message):
    await Penalties.read_penalties(message)
    



@dp.message_handler(lambda message: message.text == 'Удалить штраф.')
async def del_penalties_text(message):
    await message.reply("Введите сумму: ")
    global state
    state = 'del_penalties'




# Под ЗП ++

button_add_cofe,button_add_food = KeyboardButton('Добавить кофе'), KeyboardButton('Добавить еду')
button_del_cofe,button_del_food = KeyboardButton('Удалить кофе'), KeyboardButton('Удалить еду')

add_cofe_food = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_add_cofe, button_add_food)
del_cofe_food = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_del_cofe, button_del_food)

@dp.message_handler(lambda message: message.text == 'Подзп')
async def under_salary(message: types.Message):
    await Under_salary.under_salary(message)

##

@dp.message_handler(lambda message: message.text == 'Добавить под зп.')
async def add_under_salary(message: types.Message):
        await message.answer('Кофе/Еда?', reply_markup=add_cofe_food)

@dp.message_handler(lambda message: message.text == 'Добавить кофе')
async def cofe(message: types.Message):
    await Under_salary.add_under_salary(message, 'cofe')

@dp.message_handler(lambda message: message.text == 'Добавить еду')
async def food(message: types.Message):
    await message.reply("Введите сумму: ")
    global state
    state = 'add_under_salary_food'


##

@dp.message_handler(lambda message: message.text == 'Просмотреть все под зп')
async def read_under_salary(message: types.Message):
    await Under_salary.read_under_salary(message)

##

@dp.message_handler(lambda message: message.text == 'Удалить из под зп')
async def del_under_salary(message: types.Message):
        await message.answer('Кофе/Еда?', reply_markup=del_cofe_food)

@dp.message_handler(lambda message: message.text == 'Удалить кофе')
async def cofe(message: types.Message):
    await Under_salary.del_under_salary(message, 'cofe')

@dp.message_handler(lambda message: message.text == 'Удалить еду')
async def food(message: types.Message):
    await message.reply("Введите сумму: ")
    global state
    state = 'del_under_salary_food'



# Изменение ставки ++

@dp.message_handler(lambda message: message.text == 'Ставка')
async def bet(message: types.Message):
    await Bet.bet(message)

@dp.message_handler(lambda message: message.text == "Посмотреть ставку.")
async def watch_bet(message: types.Message):
    await Bet.watch_bet(message)

@dp.message_handler(lambda message: message.text == "Изменить ставку.")
async def edit_bet_text(message: types.Message):
    await message.reply("Введите новую ставку: )")
    global state
    state = 'edit_bet'


# Зарплата +

@dp.message_handler(lambda message: message.text == 'Зарплата')
async def salary(message: types.Message):
    await Salary.salary(message)


@dp.message_handler()
async def operation_message(message: types.Message):
    try:
        value = int(message.text)
    except ValueError:
        try:
            value= float(message.text)
        except ValueError: 
            pass

    try:
        if type(value) == int or type(value) == float:
            if state == 'edit_bet':
                await Bet.editing_bet(message,value)

            elif state == 'add_hours':
                await Hours.add_hours(message,value)

            elif state =='del_hours':
                await Hours.del_hours(message,value)

            elif state == 'add_penalties':
                await Penalties.add_penalties(message,value)
            
            elif state == 'add_under_salary_food':
                await Under_salary.add_under_salary(message, 'food', value)

            elif state == 'del_under_salary_food':
                await Under_salary.del_under_salary(message, 'food', value)

    except UnboundLocalError:
        try:
            if state == 'ADMIN_user_in_database':
                await Admin.admin_user_database(message, message.text)
            else:
                await message.reply("Данной команды не существует, используйте /help для просмотра команд")
        except NameError: 
            await message.reply("Данной команды не существует, используйте /help для просмотра команд")

if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except Exception as Error:
        Logging.crash_report(Error)
