import json

def read_token(file_name : str = 'settings/token.json'):
    with open(file_name, 'r') as file:
        data = json.load(file)
        token = data['token']

    return token