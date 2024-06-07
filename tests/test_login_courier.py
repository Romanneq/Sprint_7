import allure
import requests
from data import URL
from helpers import register_new_courier_and_return_login_password



class TestPostLoginCourier:
    ENDPOINT = '/api/v1/courier/login'
    create_courier = register_new_courier_and_return_login_password()

    @allure.title('Тест: курьер может авторизоваться, если передать все обязательные поля')
    def test_login_courier_shows_code_200(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'id': response.json()['id']}
        assert response.status_code == 200

    @allure.title('Тест: курьер может авторизоваться, если не передать необязательное поле firstname')
    def test_login_courier_without_field_first_name_shows_code_200(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'id': response.json()['id']}
        assert response.status_code == 200

    @allure.title('Тест: курьер не может авторизоваться, если не передать значение в обязательное поле login')
    def test_login_courier_with_empty_value_login_shows_error_400(self):
        payload = {"login": '', "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать значение в обязательное поле password')
    def test_login_courier_with_empty_value_password_shows_error_400(self):
        payload = {"login": self.create_courier[0], "password": '', "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать значения в обязательные поля login, password')
    def test_login_courier_with_empty_value_login_and_password_shows_error_400(self):
        payload = {"login": '', "password": '', "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: ошибка 404 not found при передаче несуществующего login')
    def test_login_courier_with_non_existent_login_shows_error_404(self):
        payload = {"login": self.create_courier[0] + '123', "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert response.status_code == 404

    @allure.title('Тест: ошибка 404 not found при передаче несуществующего password')
    def test_login_courier_with_non_existent_password_shows_error_404(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1] + '123', "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert response.status_code == 404

    @allure.title('Тест: ошибка 404 not found при передаче несуществующих полей login и password')
    def test_login_courier_with_non_existent_login_and_password_shows_error_404(self):
        payload = {"login": self.create_courier[0] + '123', "password": self.create_courier[1] + '123', "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert response.status_code == 404

    @allure.title('Тест: курьер не может авторизоваться, если не передать обязательное поле login')
    def test_login_courier_without_field_login_shows_error_400(self):
        payload = {"password": self.create_courier[1], "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать обязательное поле password')
    def test_login_courier_without_field_password_shows_error_400(self):
        payload = {"login": self.create_courier[0], "firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать обязательные поля login, password')
    def test_login_courier_without_field_password_and_login_shows_error_400(self):
        payload = {"firstName": self.create_courier[2]}
        response = requests.post(f'{URL}{self.ENDPOINT}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

