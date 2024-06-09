import allure
import requests
from data import URL
from data import Endpoint



class TestPostCreateCourier:

    @allure.title('Тест: создание курьера')
    def test_create_courier_shows_code_201(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'ok': True}
        assert response.status_code == 201

    @allure.title('Тест: нельзя создать 2 одинаковых курьеров')
    @allure.description('Сгенерировал курьера методом helpers.register_new_courier_and_return_login_password(), передал данные курьера в параметр теста')
    def test_create_identical_couriers_shows_code_409(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Тест: нельзя создать курьера c пустым значением обязательного поля login')
    def test_create_courier_with_empty_value_login_shows_code_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": '', "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: нельзя создать курьера c пустым значением обязательного поля password')
    def test_create_courier_with_empty_value_password_shows_code_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": "", "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: можно создать курьера c пустым значением необязательного поля firstName')
    def test_create_courier_with_empty_value_first_name_shows_code_201(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": ""}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'ok': True}
        assert response.status_code == 201

    @allure.title('Тест: нельзя создать курьера без обязательного поля login')
    def test_create_courier_without_field_login_shows_code_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: нельзя создать курьера без обязательного поля password')
    def test_create_courier_without_field_password_shows_code_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: нельзя создать курьера без обязательных полей login, password')
    def test_create_courier_without_fields_login_and_password_shows_code_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        assert response.status_code == 400

    @allure.title('Тест: можно создать курьера без поля firstname')
    def test_create_courier_without_field_first_name_shows_code_201(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1]}
        response = requests.post(f'{URL}{Endpoint.courier}', data=payload)
        assert response.json() == {'ok': True}
        assert response.status_code == 201