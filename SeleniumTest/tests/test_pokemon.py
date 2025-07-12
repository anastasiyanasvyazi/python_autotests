import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1fbe49ac9903ec8f4531f0606602801e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '36520'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.json()['data'][0]['trainer_name'] == 'Humanrabies'