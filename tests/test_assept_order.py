import json
import allure
from helpers import fake_create_order
from helpers import register_new_courier_and_return_login_password
import requests
from data import URL



class TestAsseptOrder:
    ENDPOINT = '/api/v1/orders/accept/'

    @allure.title('Тест: Заказ можно принять курьером')
    @allure.description('Генерирую даные курьера и заказа, получаю id курьера, id заказа. Принимаю заказ курьером, ввожу id курьера и track заказа в query-параметры, проверяю код 200, и тело ответа')
    def test_assept_order_shows_code_200(self):
        create_courier = register_new_courier_and_return_login_password()
        payload = {"login": create_courier[0], "password": create_courier[1], "firstName": create_courier[2]}
        resp_log_cour = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_courier = resp_log_cour.json()['id']
        order = fake_create_order()
        create_order = requests.post(f'{URL}/api/v1/orders', json.dumps(order))
        id_order = create_order.json()['track']
        put_order = requests.put(f'{URL}{self.ENDPOINT}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 200
        assert put_order.json() == {'ok': True}

    @allure.title('Тест: если не передать id курьера, запрос вернет ошибку')
    @allure.description('Генерирую данные заказа, получаю track заказа. Принимаю заказ курьером, ввожу track заказа и пустой id курьера в query-параметры, проверяю код 400, и тело ответа')
    def test_assept_order_with_empty_query_parameter_id_courier_shows_code_400_conflict(self):
        id_courier = ''
        order = fake_create_order()
        create_order = requests.post(f'{URL}/api/v1/orders', json.dumps(order))
        id_order = create_order.json()['track']
        put_order = requests.put(f'{URL}{self.ENDPOINT}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 400
        assert put_order.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Тест: при неправильном передаче id курьера, запрос вернет ощибку')
    @allure.description('Генерирую данные заказа, получаю track заказа. Принимаю заказ курьером, ввожу track заказа и несуществующий id курьера в query-параметры, проверяю код 404, и тело ответа')
    def test_assept_order_with_incorrect_query_parameter_id_courier_shows_code_404_not_found(self):
        id_courier = '000000'
        order = fake_create_order()
        create_order = requests.post(f'{URL}/api/v1/orders', json.dumps(order))
        id_order = create_order.json()['track']
        put_order = requests.put(f'{URL}{self.ENDPOINT}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 404
        assert put_order.json() == {'code': 404, 'message': 'Курьера с таким id не существует'}

    @allure.title('Тест: если не передать номер заказа, запрос вернет ошибку')
    @allure.description('Генерирую даные курьера, получаю его id. Принимаю заказ курьером, ввожу id курьера и пустой track заказа в query-параметры, проверяю код 404, и тело ответа')
    def test_assept_order_with_empty_query_parameter_id_order_shows_code_400_conflict(self):
        create_courier = register_new_courier_and_return_login_password()
        payload = {"login": create_courier[0], "password": create_courier[1], "firstName": create_courier[2]}
        resp_log_cour = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_courier = resp_log_cour.json()['id']
        id_order = ''
        put_order = requests.put(f'{URL}{self.ENDPOINT}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 404
        assert put_order.json() == {'code': 404, 'message': 'Заказа с таким id не существует'}


    @allure.title('Тест: при неправильном передаче номера заказа, запрос вернет ощибку')
    @allure.description('Генерирую даные курьера, получаю его id. Принимаю заказ курьером, ввожу id курьера и несуществующий track заказа в query-параметры, проверяю код 404, и тело ответа')
    def test_assept_order_with_incorrect_query_parameter_id_order_shows_code_400_conflict(self):
        create_courier = register_new_courier_and_return_login_password()
        payload = {"login": create_courier[0], "password": create_courier[1], "firstName": create_courier[2]}
        resp_log_cour = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_courier = resp_log_cour.json()['id']
        id_order = '00000'
        put_order = requests.put(f'{URL}{self.ENDPOINT}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 404
        assert put_order.json() == {'code': 404, 'message': 'Заказа с таким id не существует'}

