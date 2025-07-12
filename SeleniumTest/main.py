import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1fbe49ac9903ec8f4531f0606602801e'  # Проверьте, что токен действителен
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body = {
    "name": "Meow",
    "photo_id": 36
}

body_change = {
    "pokemon_id": None,
    "name": "New Name",
    "photo_id": 36
}

body_add = {
    "pokemon_id": None
}

# Первый автотест: Создание покемона
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body)
print(response.text)
pokemon_id = response.json()['id']  # Извлекаем id из ответа
body_change['pokemon_id'] = str(pokemon_id)  # Обновляем body_change
body_add['pokemon_id'] = str(pokemon_id)  # Обновляем body_add

# Второй автотест: Обновление покемона
response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print(response_change.text)

# Третий автотест: Добавление покемона в покебол
response_add = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add)
print(response_add.text)