import json

from DataBase import db
# Под зпшки


#Запись в бд
def write_under_salary(username: str, item: str = None , value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        if item == 'cofe':
            data['under_salary']['cofe'] = data['under_salary']['cofe'] + 75

        elif item == 'food':
            data['under_salary']['food'] = data['under_salary']['food'] + value

        else:
            raise SystemError

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Прочитать из бд
def read_under_salary(username: str):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        cofe, food = data['under_salary']['cofe'], data['under_salary']['food']

    return cofe, food


#Удаление из бд
def del_under_salary(username: str, item: str = None , value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        if item == 'cofe':
            data['under_salary']['cofe'] = data['under_salary']['cofe'] - value

        elif item == 'food':
            data['under_salary']['food'] = data['under_salary']['food'] - value

        else:
            raise SystemError

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)