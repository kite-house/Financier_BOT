import json

from DataBase import db
# Штрафы


#Прочитать из бд
def read_penalties(username: str):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            hours = data['penalties']

        return hours
    
    elif bool(filename) == False:
        read_penalties(username=username)
    
# Запись в бд
def add_penalties(username: str, value: int = 0):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            data['penalties'] = data['penalties'] + value
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    elif filename == False:
        add_penalties(username=username, value=value)

#Удаление из бд
def del_penalties(username: str, value: int = 0):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
            data['penalties'] = data['penalties'] - value
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    elif filename == False:
        del_penalties(username=username, value=value)
