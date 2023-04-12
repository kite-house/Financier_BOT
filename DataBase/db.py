import json
import os
from settings.setting import DEBUG, data, dir_database
from Logging.logging import Logging

def create_new_user_database(username:str):
    database = os.listdir(path=dir_database)
    for file in database:
        if file == f'{username}.json':
            return 0
    
    with open(f'{dir_database}/{username}.json', 'w+') as file:
        json.dump(data, file, indent=4)
    
    Logging.system('CREATE_NEW_USER', 'DATABASE', 'SUCCES')

def conductor(username):
    if DEBUG == True:
        username = 'DEBUG_TEST_BD'

    filename = f'{username}.json'
    database = os.listdir(path=dir_database)
    for file in database:
        if file == filename:
            filename = f'{username}.json'
            return filename

    create_new_user_database(username=username)
    return False

def laod_full_database():
    database = os.listdir(path=dir_database)
    full_database = []
    for file in database:
        file_find_json = file.split('.')
        try:
            if file_find_json[1] == 'json':
                file = file.replace('.json','')
                full_database.append(file)
        except IndexError: pass
    return full_database

def add_new_month_in_db():
    database = os.listdir(path=dir_database)
    for file in database:
        file_find_json = file.split('.')
        try:
            if file_find_json[1] == 'json':
                filename = f'{dir_database}\{file}'
                with open(filename, 'r') as file:
                    data_file = json.load(file)
                    data_file.update(data)

                with open(filename, 'w') as file:
                    json.dump(data_file,file,indent=4)

        except IndexError:
            pass
    Logging.system('ADD_NEW_MONTH', 'DATABASE', 'SUCCES')
