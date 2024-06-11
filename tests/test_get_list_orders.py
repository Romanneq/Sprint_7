import allure
import requests
from data import URL
from data import Endpoint



class TestGetListOrders:

    @allure.title('Тест: получение списка заказов')
    @allure.description('Сначала сгенерировали данные для создания курьера, получили его id, получили список заказов')
    def test_get_list_orders_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        courier_login = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        courier_id = courier_login.json()['id']
        response = requests.get(f'{URL}{Endpoint.list_orders}{courier_id}')
        assert response.json()['orders'].__class__ == list
        assert response.status_code == 200
