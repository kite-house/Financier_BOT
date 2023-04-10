import json
from settings.setting import dir_api_token
from Logging.logging import Logging

def api_token(filename : str = dir_api_token):
    with open(filename, 'r') as file:
        data = json.load(file)
        API_TOKEN = data['token']
    Logging.system('LOADING', 'API-TOKEN', 'SUCCES')
    return API_TOKEN