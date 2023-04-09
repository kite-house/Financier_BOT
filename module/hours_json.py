import json
from DataBase import db

# Часы

# Прочитать из бд
def read_hours(username: str):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            hours = data['hours']

        return hours
    if filename == False:
        read_hours(username=username)
    
# Запись в бд
def add_hours(username: str, value: int = 0):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            data['hours'] = data['hours'] + value
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    elif filename == False:
        add_hours(username=username, value=value)

# Удаление из бд
def del_hours(username: str, value: int = 0):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            data['hours'] = data['hours'] - value
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    if filename == False:
        del_hours(username=username, value=value)