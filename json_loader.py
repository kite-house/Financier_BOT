import json

# Токен
def read_token(file_name : str = 'token.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
        token = data['token']

    return token

# Ставка

def read_bet(file_name: str = 'data.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
        bet = data['bet']

    return bet

def editing_bet(file_name: str = 'data.json', value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        data['bet'] = value

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    return 


# Часы

def read_hours(file_name: str = 'data.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
        hours = data['hours']

    return hours
    

def write_hours(file_name: str = 'data.json', value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        data['hours'] = data['hours'] + value
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    return 

def del_hours(file_name: str = 'data.json', value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        data['hours'] = data['hours'] - value
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Штраф

def read_penalties(file_name: str = 'data.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
        hours = data['penalties']

    return hours
    

def write_penalties(file_name: str = 'data.json', value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        data['penalties'] = data['penalties'] + value
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    return 

def del_penalties(file_name: str = 'data.json', value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        data['penalties'] = data['penalties'] - value
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# ПОД ЗП

def write_under_salary(file_name: str = 'data.json', item: str = None , value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        if item == 'cofe':
            data['under_salary']['cofe'] = data['under_salary']['cofe'] + 75

        elif item == 'food':
            data['under_salary']['food'] = data['under_salary']['food'] + value

        else:
            raise SystemError

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def read_under_salary(file_name: str = 'data.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
        cofe, food = data['under_salary']['cofe'], data['under_salary']['food']

    return cofe, food

def del_under_salary(file_name: str = 'data.json', item: str = None , value: int = 0):
    with open(file_name, 'r') as file:
        data = json.load(file)
        if item == 'cofe':
            data['under_salary']['cofe'] = data['under_salary']['cofe'] - value

        elif item == 'food':
            data['under_salary']['food'] = data['under_salary']['food'] - value

        else:
            raise SystemError

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# salary

def load_selery(file_name: str = 'data.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
    hours, bet, penalties, cofe, food = data['hours'], data['bet'],data['penalties'], data['under_salary']['cofe'], data['under_salary']['food']

    return hours, bet, penalties, cofe, food