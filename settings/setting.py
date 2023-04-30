import datetime

DEBUG = False

SUPER_USER = ['']


data = {
    datetime.datetime.now().month : {
            "hours": 0,
            "under_salary": {
                "cofe": 0,
                "food": 0
            },
            "penalties": 0,
            "bet": 0
        }
    }


dir_database = 'DataBase'

dir_api_token = 'settings/token.json'

logfile = 'Logging/logfile.txt'
