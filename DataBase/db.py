import json
import os


data = {
    "hours": 0,
    "under_salary": {
        "cofe": 0,
        "food": 0
    },
    "penalties": 0,
    "bet": 110
}


dir_database = 'DataBase'

def create_new_user_database(username:str):
    file = os.listdir(path="DataBase")
    for i in file:
        if i == f'{username}.json':
            return 0
    
    with open(f'{dir_database}/{username}.json', 'w+') as file:
        json.dump(data, file, indent=4)

def conductor(username):
    filename = f'{username}.json'
    file = os.listdir(path="DataBase")
    for i in file:
        if i == filename:
            filename = f'DataBase\{username}.json'
            return filename

    return False
            

'''with open('DataBase/xxxkite.json', 'r') as file:
    data = json.load(file)
    print(data)'''