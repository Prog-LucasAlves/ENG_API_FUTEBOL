import requests

from datetime import date, timedelta

from connectdb import in_dados

import os
import dotenv

PATH = '../Docker/.env'

# Carrega as variáveis de ambiente do projeto
dotenv.load_dotenv(dotenv_path=PATH, verbose=True)
KEY = os.getenv('KEY')


def Previousdate():
    data_atual = date.today()
    data_ontem = data_atual + timedelta(-1)
    return data_ontem


def Conectapi():
    diaAnterior = Previousdate()
    key = KEY
    url = f'https://apiv3.apifootball.com/?action=get_predictions&from={diaAnterior}&to={diaAnterior}&APIkey={key}'
    response = requests.get(url)
    return response.json()


def Collectdata():
    data = Conectapi()
    for game in data:
        print(game['match_id'])
        match_id = game['match_id']

        queryInsert = f"INSERT INTO infomatches VALUES ( \
            '{match_id}')"

        in_dados(queryInsert)
    print('============================')
    print('Dados inseridos com sucesso!')
    print('============================')


if __name__ == '__main__':
    Collectdata()
    print('Conectado com sucesso!')
