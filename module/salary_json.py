import json
from DataBase import db
# ЗП


# Прочитать из бд
def load_selery(username: str, datetime):
    filename = db.conductor(username)
    if bool(filename) == True:
        with open(filename, 'r') as file:
            data = json.load(file)
        hours, bet, penalties, cofe, food = data[datetime]['hours'], data[datetime]['bet'],data[datetime]['penalties'], data[datetime]['under_salary']['cofe'], data[datetime]['under_salary']['food']

        return hours, bet, penalties, cofe, food
    
    elif filename == False:
        load_selery(username=username)