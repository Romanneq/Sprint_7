import allure
import requests
from data import URL
from helpers import fake_data_courier
from helpers import register_new_courier_and_return_login_password



class TestPostCreateCourier:
    ENDPOINT = '/api/v1/courier'
    create_courier = register_new_courier_and_return_login_password()

    @allure.title('Тест: создание курьера')
    def test_create_courier_shows_code_201(self):
        login, password, first_name = fake_data_courier()
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'ok': True}
        assert response.status_code == 201

    @allure.title('Тест: нельзя создать 2 одинаковых курьеров')
    @allure.description('Сгенерировал курьера методом helpers.register_new_courier_and_return_login_password(), передал данные курьера в параметр теста')
    def test_create_identical_couriers_shows_code_409(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Тест: нельзя создать курьера c пустым значением обязательного поля login')
    def test_create_courier_with_empty_value_login_shows_code_400(self):
        login, password, first_name = fake_data_courier()
        payload = {"login": '', "password": password, "firstName": first_name}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: нельзя создать курьера c пустым значением обязательного поля password')
    def test_create_courier_with_empty_value_password_shows_code_400(self):
        login, password, first_name = fake_data_courier()
        payload = {"login": login, "password": "", "firstName": first_name}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: можно создать курьера c пустым значением необязательного поля firstName')
    def test_create_courier_with_empty_value_first_name_shows_code_201(self):
        login, password, first_name = fake_data_courier()
        payload = {"login": login, "password": password, "firstName": ""}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'ok': True}
        assert response.status_code == 201

    @allure.title('Тест: нельзя создать курьера без обязательного поля login')
    def test_create_courier_without_field_login_shows_code_400(self):
        login, password, first_name = fake_data_courier()
        payload = {"password": password, "firstName": first_name}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: нельзя создать курьера без обязательного поля password')
    def test_create_courier_without_field_password_shows_code_400(self):
        login, password, first_name = fake_data_courier()
        payload = {"login": login, "firstName": first_name}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: нельзя создать курьера без обязательных полей login, password')
    def test_create_courier_without_fields_login_and_password_shows_code_400(self):
        login, password, first_name = fake_data_courier()
        payload = {"firstName": first_name}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: можно создать курьера без поля firstname')
    def test_create_courier_without_field_first_name_shows_code_201(self):
        login, password, first_name = fake_data_courier()
        payload = {"login": login, "password": password}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'ok': True}
        assert response.status_code == 201