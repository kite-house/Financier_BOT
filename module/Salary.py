from module import salary_json

async def salary(message):
    hours, bet, penalties, cofe, food = salary_json.load_selery(username=message['from']['username'])
    salary = (hours * bet) - (penalties + cofe + food)
    await message.reply(f"Отработана часов: {hours}, заработана за часы {hours * bet}р, при ставке {bet}р в час.\nШтраф на сумму: {penalties}р.\nПотрачено всего под зп: {cofe+food}р, из которых {cofe}р на кофе и {food}р на еду.\nОбщая сумма: {salary}р")