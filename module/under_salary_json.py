import json

from DataBase import db
from datetime import datetime
# Под зпшки


#Запись в бд
def add_under_salary(username: str, item: str = None , value: int = 0):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            if item == 'cofe':
                data[str(datetime.now().month)]['under_salary']['cofe'] = data[str(datetime.now().month)]['under_salary']['cofe'] + 75

            elif item == 'food':
                data[str(datetime.now().month)]['under_salary']['food'] = data[str(datetime.now().month)]['under_salary']['food'] + value

            else:
                raise SystemError

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    elif filename == False:
        add_under_salary(username=username, item=item, value=value)


# Прочитать из бд
def read_under_salary(username: str):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            cofe, food = data[str(datetime.now().month)]['under_salary']['cofe'], data[str(datetime.now().month)]['under_salary']['food']

        return cofe, food

    elif filename == False:
        read_under_salary(username=username)


#Удаление из бд
def del_under_salary(username: str, item: str = None , value: int = 0):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            if item == 'cofe':
                data[str(datetime.now().month)]['under_salary']['cofe'] = data[str(datetime.now().month)]['under_salary']['cofe'] - value

            elif item == 'food':
                data[str(datetime.now().month)]['under_salary']['food'] = data[str(datetime.now().month)]['under_salary']['food'] - value

            else:
                raise SystemError

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    elif filename == False:
        del_under_salary(username=username, item=item, value=value)