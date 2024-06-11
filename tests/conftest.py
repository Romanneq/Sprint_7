import random
import string
import pytest
import requests
from data import URL
from data import Endpoint



@pytest.fixture
def generating_the_cour_and_delete_the_cour():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    # возвращаем список
    yield login_pass

    # Если запрос возвращает id курьера, курьер удаляется, иначе = pass
    try:
        response_login_courier = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = response_login_courier.json()['id']
    except KeyError:
        pass
    else:
        requests.delete(f'{URL}{Endpoint.courier}/{id_courier}')