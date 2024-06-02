import allure
import requests
from data import URL
from helpers import fake_create_order



class TestGetOrder:
    ENDPOINT = '/api/v1/orders/track?t='

    @allure.title('Тест: успешное получение заказа по его номеру')
    def test_get_order_code_200(self):
        payload_order = fake_create_order()
        res_cr_ord = requests.post(f'{URL}/api/v1/orders', data=payload_order)
        id_order = res_cr_ord.json()['track']
        response = requests.get(f'{URL}{self.ENDPOINT}{id_order}')
        assert response.status_code == 200
        assert id_order == response.json()['order']["track"]

    @allure.title('Тест: запрос без номера заказа возвращает ошибку')
    def test_get_order_without_number_order_code_400(self):
        response = requests.get(f'{URL}{self.ENDPOINT}')
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Тест: запрос с несуществующим заказом возвращает ошибку')
    def test_get_order_with_non_existent_number_order_code_400(self):
        response = requests.get(f'{URL}{self.ENDPOINT}00000')
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Заказ не найден'}