import allure
import requests
from data import URL
from data import Endpoint



class TestPostLoginCourier:

    @allure.title('Тест: курьер может авторизоваться, если передать все обязательные поля')
    def test_login_courier_shows_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'id': response.json()['id']}
        assert response.status_code == 200

    @allure.title('Тест: курьер может авторизоваться, если не передать необязательное поле firstname')
    def test_login_courier_without_field_first_name_shows_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'id': response.json()['id']}
        assert response.status_code == 200

    @allure.title('Тест: курьер не может авторизоваться, если не передать значение в обязательное поле login')
    def test_login_courier_with_empty_value_login_shows_error_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": '', "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать значение в обязательное поле password')
    def test_login_courier_with_empty_value_password_shows_error_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": '', "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать значения в обязательные поля login, password')
    def test_login_courier_with_empty_value_login_and_password_shows_error_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": '', "password": '', "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: ошибка 404 not found при передаче несуществующего login')
    def test_login_courier_with_non_existent_login_shows_error_404(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0] + '123', "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert response.status_code == 404

    @allure.title('Тест: ошибка 404 not found при передаче несуществующего password')
    def test_login_courier_with_non_existent_password_shows_error_404(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1] + '123', "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert response.status_code == 404

    @allure.title('Тест: ошибка 404 not found при передаче несуществующих полей login и password')
    def test_login_courier_with_non_existent_login_and_password_shows_error_404(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0] + '123', "password": generating_the_cour_and_delete_the_cour[1] + '123', "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert response.status_code == 404

    @allure.title('Тест: курьер не может авторизоваться, если не передать обязательное поле login')
    def test_login_courier_without_field_login_shows_error_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать обязательное поле password')
    def test_login_courier_without_field_password_shows_error_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

    @allure.title('Тест: курьер не может авторизоваться, если не передать обязательные поля login, password')
    def test_login_courier_without_field_password_and_login_shows_error_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}
        assert response.status_code == 400

