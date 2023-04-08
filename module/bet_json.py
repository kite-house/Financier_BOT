import json
from DataBase import db

# Часовая ставка


# Прочитать из бд
def read_bet(username: str):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        bet = data['bet']

    return bet


# Записать в бд
def editing_bet(username: str, value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        data['bet'] = value

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    return 