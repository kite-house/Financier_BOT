import json

from DataBase import db


def admin_database_json():
    database = db.laod_full_database()
    return database

def admin_user_database_json(user):
    database = db.laod_full_database()
    for find_user in database:
        if find_user == user:
            user = db.conductor(find_user)
            with open(user,'r+') as file:
                user = json.load(file)
                
            return user
        
    return False
        
