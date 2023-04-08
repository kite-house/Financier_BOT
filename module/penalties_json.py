import json

from DataBase import db
# Штрафы


#Прочитать из бд
def read_penalties(username: str):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        hours = data['penalties']

    return hours
    
# Запись в бд
def write_penalties(username: str, value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        data['penalties'] = data['penalties'] + value
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    return 

#Удаление из бд
def del_penalties(username: str, value: int = 0):
    filename = db.conductor(username)
    with open(filename, 'r') as file:
        data = json.load(file)
        data['penalties'] = data['penalties'] - value
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
