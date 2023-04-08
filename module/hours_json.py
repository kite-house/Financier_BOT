import json
from DataBase import db

# Часы

# Прочитать из бд
def read_hours(username: str):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        hours = data['hours']

    return hours
    
# Запись в бд
def write_hours(username: str, value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        data['hours'] = data['hours'] + value
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    return 

# Удаление из бд
def del_hours(username: str, value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        data['hours'] = data['hours'] - value
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)