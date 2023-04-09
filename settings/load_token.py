import json
from settings.setting import dir_api_token

def read_token(filename : str = dir_api_token):
    with open(filename, 'r') as file:
        data = json.load(file)
        token = data['token']

    return token