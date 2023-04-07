import logging
from aiogram import Bot, Dispatcher, types, executor, filters
import json_loader

print("BOT-START: LOADING..")

logging.basicConfig(level=logging.INFO)

bet = json_loader.read_bet()

bot = Bot(token=json_loader.read_token())
dp = Dispatcher(bot)



ALL_COMMANDS = ['/start - Приветствие', 
                '/help - Помощь',
                '/write_hours - Добавить часы', 
                '/read_hours - Посмотреть часы', 
                '/del_hours - Удалить часы', 
                '/write_penalties - Добавить штраф', 
                '/read_penalties - Посмотреть штрафы', 
                '/del_penalties - Удалить штрафы', 
                '/write_under_salary - Добавить под зп', 
                '/read_under_salary - Посмотреть все под зп', 
                '/del_under_salary - Удалить из под зп', 
                '/salary - Посмотреть расчёт зарплаты',
                '/bet - Ввести часовую ставку']

HELP = ''
for com in ALL_COMMANDS:
    HELP = HELP + com + '\n'


print("BOT-START: COMPLETED")

# команды
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который может помочь тебе с расчётом зарплаты!. Используй /help для просмотра всех команд!")


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply(HELP)

# Часы

@dp.message_handler(commands='write_hours')
async def write_hours(message: types.Message):
    try:
        value = int(message.text.split()[1])
        json_loader.write_hours(value = value)
        await message.reply(f'Записал! Количество отработаных часов: {value}, заработано денег: {value * bet}р.')

    except IndexError:
        await message.reply("Используйте /write_hours value(Кол-во часов).")

    except ValueError:
        await message.reply("Введите число после команды!")

@dp.message_handler(commands='read_hours')
async def read_hours(message: types.Message):
    value = json_loader.read_hours() # ДОПИШИ СУКА
    await message.reply(f"Количество всего отработаных часов: {value}, всего заработано денег {value * bet}р.")

@dp.message_handler(commands='del_hours')
async def del_hours(message: types.Message):
    try:
        value = int(message.text.split()[1])
        json_loader.del_hours(value=value)
        await message.reply(f'Записал! Удалено часов: {value}.')

    except IndexError:
        await message.reply("Используйте /del_hours value(Кол-во часов).")

    except ValueError:
        await message.reply("Введите число после команды!")

# Штраф

@dp.message_handler(commands='write_penalties')
async def write_penalties(message: types.Message):
    try:
        value = int(message.text.split()[1])
        json_loader.write_penalties(value = value)
        await message.reply(f'Записал! добавлено в штраф: {value}р.')

    except IndexError:
        await message.reply("Используйте /write_penalties value(Штраф).")

    except ValueError:
        await message.reply("Введите число после команды!")

@dp.message_handler(commands='read_penalties')
async def read_penalties(message: types.Message):
    value = json_loader.read_penalties() # ДОПИШИ СУКА
    await message.reply(f"Сумма штрафов: {value}р.")

@dp.message_handler(commands='del_penalties')
async def del_penalties(message: types.Message):
    try:
        value = int(message.text.split()[1])
        json_loader.del_penalties(value=value)
        await message.reply(f'Записал! Удалено из штрафа: {value}р.')

    except IndexError:
        await message.reply("Используйте /del_penalties value(Штраф)!")

    except ValueError:
        await message.reply("Введите число после команды!")    


# Под ЗП

@dp.message_handler(commands='write_under_salary')
async def write_under_salary(message: types.Message):
    try:
        item = str(message.text.split()[1]).lower()
        
        if item == 'cofe' or item == 'кофе':
            value = 75
            json_loader.write_under_salary(item = 'cofe', value = value)
            await message.reply(f'Записал! Кофе, {value}р под зп.')

        elif item == 'food' or item == 'еда':
            value = int(message.text.split()[2])
            json_loader.write_under_salary(item = 'food', value = value)
            await message.reply(f'Записал! Еда, {value}р под зп.')

        else: 
            raise IndexError    
    except IndexError:
        await message.reply('Используйте /write_sunder_salary (cofe/food) value!')

    except ValueError:
        await message.reply("Используйте /write_sunder_salary (cofe/food) value!")


@dp.message_handler(commands='read_under_salary')
async def read_under_salary(message: types.Message):
    cofe, food = json_loader.read_under_salary()
    await message.reply(f'Всего потрачено {cofe+food}р под зп, из который {cofe}р на кофе и {food}р на еду')


@dp.message_handler(commands='del_under_salary')
async def del_under_salary(message: types.Message):
    try:
        item = str(message.text.split()[1]).lower()
        
        if item == 'cofe' or item == 'кофе':
            value = 75
            json_loader.del_under_salary(item = 'cofe', value = value)
            await message.reply(f'Записал! Удалено кофе из, {value}р под зп.')

        elif item == 'food' or item == 'еда':
            value = int(message.text.split()[2])
            json_loader.del_under_salary(item = 'food', value = value)
            await message.reply(f'Записал! Удалена еда из, {value}р под зп.')

        else: 
            raise IndexError    
        
    except IndexError:
        await message.reply('Используйте /del_sunder_salary (cofe/food) value!')

    except ValueError:
        await message.reply("Используйте /del_sunder_salary (cofe/food) value!")


# Изменение ставки

@dp.message_handler(commands='bet')
async def salary(message: types.Message):
    try:
        value = int(message.text.split()[1])
        json_loader.editing_bet(value=value)
        await message.reply(f"Ставка изменена на {value}р в час")
    except IndexError:
        await message.reply('Используйте /bet value')

    except ValueError:
        await message.reply("Введите число после команды!")


# Зарплата

@dp.message_handler(commands='salary')
async def salary(message: types.Message):
    hours, bet, penalties, cofe, food= json_loader.load_selery()
    salary = (hours * bet) - (penalties + cofe + food)
    await message.reply(f"Отработана часов: {hours}, заработана за часы {hours * bet}р, при ставке {bet}р в час.\nШтраф на сумму: {penalties}р.\nПотрачено всего под зп: {cofe+food}р, из которых {cofe}р на кофе и {food}р на еду.\nОбщая сумма: {salary}р")


@dp.message_handler()
async def unknow_commands(message: types.Message):
    await message.reply("Данной команды не существует, используйте /help для просмотра команд")

if __name__ == '__main__':
    # Запускаем цикл обработки входящих сообщений
    executor.start_polling(dp, skip_updates=True)