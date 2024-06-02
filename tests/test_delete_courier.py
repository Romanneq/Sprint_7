import allure
from helpers import register_new_courier_and_return_login_password
import requests
from data import URL



class TestDeleteCourier:
    ENDPOINT = '/api/v1/courier/'
    create_courier = register_new_courier_and_return_login_password()

    @allure.title('Тест: курьера можно удалить')
    @allure.description('Сначала генерирую login, password, firstname курьера, затем получаю его id, далее id передаем в ручку delete. Проверяю, что учетная запись с таким id не существует')
    def test_delete_courier_shows_code_200(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response_login_courier = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_courier = response_login_courier.json()['id']
        res_del_cour = requests.delete(f'{URL}{self.ENDPOINT}{id_courier}')
        assert requests.post(f'{URL}/api/v1/courier/login', data=payload).json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert res_del_cour.status_code == 200
        assert res_del_cour.json() == {'ok': True}

    @allure.title('Тест: нельзя дважды удалить курьера')
    def test_delete_courier_twice_shows_code_404(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response_login_courier = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_courier = response_login_courier.json()['id']
        requests.delete(f'{URL}{self.ENDPOINT}{id_courier}')
        res_del_cour = requests.delete(f'{URL}{self.ENDPOINT}{id_courier}')
        assert res_del_cour.status_code == 404
        assert res_del_cour.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

    @allure.title('Тест: проверка удаления курьера без id')
    def test_delete_courier_without_id_shows_code_400(self):
        res_del_cour = requests.delete(f'{URL}{self.ENDPOINT}{''}')
        assert res_del_cour.status_code == 400
        assert res_del_cour.json() == {'code': 400, "message":  "Недостаточно данных для удаления курьера"}

    @allure.title('Тест: запрос с несуществующим "id" курьера')
    def test_delete_courier_with_non_existent_id_shows_code_404(self):
        payload = {"login": self.create_courier[0], "password": self.create_courier[1], "firstName": self.create_courier[2]}
        response_login_courier = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_courier = response_login_courier.json()['id'] + 123
        res_del_cour = requests.delete(f'{URL}{self.ENDPOINT}{id_courier}')
        assert res_del_cour.status_code == 404
        assert res_del_cour.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}
