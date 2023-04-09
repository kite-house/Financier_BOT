import logging
from aiogram import Bot, Dispatcher, types, executor
from module import Bet, Hours, Penalties, Salary, Under_salary
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from settings import load_token
from DataBase import db

print("BOT-START: LOADING..")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=load_token.read_token())
dp = Dispatcher(bot)


ALL_COMMANDS = ['/start - Приветствие', 
                '/help - Помощь',
                '/hours - Часы', 
                '/penalties - Штрафы', 
                '/under_salary - Под зп',
                '/salary - Посмотреть расчёт зарплаты',
                '/bet - часовая ставка']

HELP = ''
for com in ALL_COMMANDS:
    HELP = HELP + com + '\n'


print("BOT-START: COMPLETED")

# команды
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    username = (message['from']['username'])
    db.create_new_user_database(username)
    await message.reply(f"Привет, {message['from']['first_name']}! Я бот, который может помочь тебе с расчётом зарплаты!. Используй /help для просмотра всех команд!")


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply(HELP)

# Часы ++

@dp.message_handler(commands='hours')
async def hours(message: types.Message):
    await Hours.hours(message)


@dp.message_handler(lambda message: message.text == 'Добавить часов.')
async def add_hours_text(message: types.Message):
    await message.reply('Сколько часов добавляем?: (С помощью команды /add_hours value)')

@dp.message_handler(commands = 'add_hours')
async def add_hours_text(message: types.Message):
    await Hours.write_hours(message)


@dp.message_handler(lambda message: message.text == 'Посмотреть кол-во часов.')
async def watch_hours(message: types.Message):
    await Hours.read_hours(message)


@dp.message_handler(lambda message: message.text == 'Удалить часы')
async def del_hours(message: types.Message):
    await message.reply('Сколько часов удаляем?: (С помощью команды /del_hours value)')

@dp.message_handler(commands = 'del_hours')
async def del_hours(message: types.Message):
    await Hours.del_hours(message)

# Штраф

@dp.message_handler(commands='penalties')
async def penalties(message: types.Message):
    await Penalties.penalties(message)


@dp.message_handler(lambda message: message.text == 'Добавить штраф.')
async def add_penalties_text(message):
    await message.reply("Введите сумму: (С помощью команды /add_penal value)")

@dp.message_handler(commands='add_penal')
async def add_penalties(message: types.Message):
    await Penalties.write_penalties(message)



@dp.message_handler(lambda message: message.text == 'Посмотреть штрафы.')
async def watch_penalties(message: types.Message):
    await Penalties.read_penalties(message)
    



@dp.message_handler(lambda message: message.text == 'Удалить штраф.')
async def del_penalties_text(message):
     await message.reply("Введите сумму: (С помощью команды /del_penal value)")

@dp.message_handler(commands='del_penal')
async def add_penalties(message: types.Message):
    await Penalties.write_penalties(message)




# Под ЗП ++

button1 = KeyboardButton('Кофе')
button2 = KeyboardButton('Еда')
cf = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2 )

@dp.message_handler(commands='under_salary')
async def under_salary(message: types.Message):
    await Under_salary.under_salary(message)

##

@dp.message_handler(lambda message: message.text == 'Добавить под зп.')
async def add_under_salary(message: types.Message):
        await message.answer('Кофе/Еда?', reply_markup=cf)

@dp.message_handler(lambda message: message.text == 'Кофе')
async def cofe(message: types.Message):
    await Under_salary.add_under_salary(message, 'кофе')

@dp.message_handler(lambda message: message.text == 'Еда')
async def food(message: types.Message):
        await message.reply("Введите сумму: (С помощью команды /add_food value)")

@dp.message_handler(commands='add_food')
async def sum_food(message: types.Message):
    value = int(message.text.split()[1])
    await Under_salary.add_under_salary(message, 'еда', value=value)

##

@dp.message_handler(lambda message: message.text == 'Просмотреть все под зп')
async def read_under_salary(message: types.Message):
    await Under_salary.read_under_salary(message)

##

@dp.message_handler(lambda message: message.text == 'Удалить из под зп')
async def del_under_salary(message: types.Message):
        await message.answer('Кофе/Еда?', reply_markup=cf)

@dp.message_handler(lambda message: message.text == 'Кофе')
async def cofe(message: types.Message):
    await Under_salary.del_under_salary(message, 'кофе')

@dp.message_handler(lambda message: message.text == 'Еда')
async def food(message: types.Message):
        await message.reply("Введите сумму: (С помощью команды /del_food value)")

@dp.message_handler(commands='del_food')
async def sum_food(message: types.Message):
    value = int(message.text.split()[1])
    await Under_salary.del_under_salary(message, 'еда', value=value)



# Изменение ставки ++

@dp.message_handler(commands='bet')
async def bet(message: types.Message):
    await Bet.bet(message)

@dp.message_handler(lambda message: message.text == "Посмотреть ставку.")
async def watch_bet(message: types.Message):
        await Bet.watch_bet(message)

@dp.message_handler(lambda message: message.text == "Изменить ставку.")
async def edit_bet_text(message: types.Message):
        await message.reply("Введите новую ставку: (С помощью команды /edit_bet value)")

@dp.message_handler(commands='edit_bet')
async def edit_bet(message: types.Message):
        await Bet.editing_bet(message)

# Зарплата +

@dp.message_handler(commands='salary')
async def salary(message: types.Message):
    await Salary.salary(message)


@dp.message_handler()
async def unknow_commands(message: types.Message):
    await message.reply("Данной команды не существует, используйте /help для просмотра команд")

if __name__ == '__main__':
    # Запускаем цикл обработки входящих сообщений
    executor.start_polling(dp)