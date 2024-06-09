import allure
import requests
from data import URL
from data import Endpoint



class TestDeleteCourier:

    @allure.title('Тест: курьера можно удалить')
    @allure.description('Сначала генерирую login, password, firstname курьера, затем получаю его id, далее id передаем в ручку delete. Проверяю, что учетная запись с таким id не существует')
    def test_delete_courier_shows_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response_login_courier = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = response_login_courier.json()['id']
        res_del_cour = requests.delete(f'{URL}{Endpoint.courier}/{id_courier}')
        assert requests.post(f'{URL}{Endpoint.login_courier}', data=payload).json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        assert res_del_cour.status_code == 200
        assert res_del_cour.json() == {'ok': True}

    @allure.title('Тест: нельзя дважды удалить курьера')
    def test_delete_courier_twice_shows_code_404(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response_login_courier = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = response_login_courier.json()['id']
        requests.delete(f'{URL}{Endpoint.courier}/{id_courier}')
        res_del_cour = requests.delete(f'{URL}{Endpoint.courier}/{id_courier}')
        assert res_del_cour.status_code == 404
        assert res_del_cour.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

    @allure.title('Тест: проверка удаления курьера без id')
    def test_delete_courier_without_id_shows_code_400(self):
        res_del_cour = requests.delete(f'{URL}{Endpoint.courier}/')
        assert res_del_cour.status_code == 400
        assert res_del_cour.json() == {'code': 400, "message":  "Недостаточно данных для удаления курьера"}

    @allure.title('Тест: запрос с несуществующим "id" курьера')
    def test_delete_courier_with_non_existent_id_shows_code_404(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        response_login_courier = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = response_login_courier.json()['id'] + 123
        res_del_cour = requests.delete(f'{URL}{Endpoint.courier}/{id_courier}')
        assert res_del_cour.status_code == 404
        assert res_del_cour.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}
