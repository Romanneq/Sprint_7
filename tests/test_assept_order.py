import json
import allure
from helpers import fake_data_order
import requests
from data import URL
from data import Endpoint



class TestAsseptOrder:

    @allure.title('Тест: Заказ можно принять курьером')
    @allure.description('Генерирую даные курьера и заказа, получаю id курьера, id заказа. Принимаю заказ курьером, ввожу id курьера и track заказа в query-параметры, проверяю код 200, и тело ответа')
    def test_assept_order_shows_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        resp_log_cour = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = resp_log_cour.json()['id']
        order = fake_data_order()
        create_order = requests.post(f'{URL}{Endpoint.create_order}', json.dumps(order))
        id_order = create_order.json()['track']
        put_order = requests.put(f'{URL}{Endpoint.assept_order}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 200
        assert put_order.json() == {'ok': True}

    @allure.title('Тест: если не передать id курьера, запрос вернет ошибку')
    @allure.description('Генерирую данные заказа, получаю track заказа. Принимаю заказ курьером, ввожу track заказа и пустой id курьера в query-параметры, проверяю код 400, и тело ответа')
    def test_assept_order_with_empty_query_parameter_id_courier_shows_code_400_conflict(self):
        id_courier = ''
        order = fake_data_order()
        create_order = requests.post(f'{URL}{Endpoint.create_order}', json.dumps(order))
        id_order = create_order.json()['track']
        put_order = requests.put(f'{URL}{Endpoint.assept_order}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 400
        assert put_order.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Тест: при неправильном передаче id курьера, запрос вернет ощибку')
    @allure.description('Генерирую данные заказа, получаю track заказа. Принимаю заказ курьером, ввожу track заказа и несуществующий id курьера в query-параметры, проверяю код 404, и тело ответа')
    def test_assept_order_with_incorrect_query_parameter_id_courier_shows_code_404_not_found(self):
        id_courier = '000000'
        order = fake_data_order()
        create_order = requests.post(f'{URL}{Endpoint.create_order}', json.dumps(order))
        id_order = create_order.json()['track']
        put_order = requests.put(f'{URL}{Endpoint.assept_order}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 404
        assert put_order.json() == {'code': 404, 'message': 'Курьера с таким id не существует'}

    @allure.title('Тест: если не передать номер заказа, запрос вернет ошибку')
    @allure.description('Генерирую даные курьера, получаю его id. Принимаю заказ курьером, ввожу id курьера и пустой track заказа в query-параметры, проверяю код 404, и тело ответа')
    def test_assept_order_with_empty_query_parameter_id_order_shows_code_400_conflict(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        resp_log_cour = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = resp_log_cour.json()['id']
        id_order = ''
        put_order = requests.put(f'{URL}{Endpoint.assept_order}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 404
        assert put_order.json() == {'code': 404, 'message': 'Заказа с таким id не существует'}


    @allure.title('Тест: при неправильном передаче номера заказа, запрос вернет ощибку')
    @allure.description('Генерирую даные курьера, получаю его id. Принимаю заказ курьером, ввожу id курьера и несуществующий track заказа в query-параметры, проверяю код 404, и тело ответа')
    def test_assept_order_with_incorrect_query_parameter_id_order_shows_code_400_conflict(self, generating_the_cour_and_delete_the_cour):
        payload = {"login": generating_the_cour_and_delete_the_cour[0], "password": generating_the_cour_and_delete_the_cour[1], "firstName": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.courier}', data=payload)
        resp_log_cour = requests.post(f'{URL}{Endpoint.login_courier}', data=payload)
        id_courier = resp_log_cour.json()['id']
        id_order = '00000'
        put_order = requests.put(f'{URL}{Endpoint.assept_order}{id_order}?courierId={id_courier}')
        assert put_order.status_code == 404
        assert put_order.json() == {'code': 404, 'message': 'Заказа с таким id не существует'}

