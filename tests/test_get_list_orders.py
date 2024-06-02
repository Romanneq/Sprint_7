import allure
import requests
from data import URL
from helpers import register_new_courier_and_return_login_password



class TestGetListOrders:
    ENDPOINT = '/api/v1/orders?courierId='

    @allure.title('Тест: получение списка заказов')
    @allure.description('Сначала сгенерировали данные для создания курьера, получили его id, получили список заказов')
    def test_get_list_orders_code_200(self):
        create_courier = register_new_courier_and_return_login_password()
        payload = {"login": create_courier[0], "password": create_courier[1], "firstName": create_courier[2]}
        courier_login = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        courier_id = courier_login.json()['id']
        response = requests.get(f'{URL}{self.ENDPOINT}{courier_id}')
        assert response.json()['orders'].__class__ == list
        assert response.status_code == 200
