import json
import allure
import pytest
import requests
from data import URL
from helpers import fake_create_order



class TestPostCreateOrder:
    ENDPOINT = '/api/v1/orders'

    @allure.title('Тест: создание заказа c разными входными параметрами color: только "Black", только "Grey", "Black" и "Grey", пустое значение')
    @pytest.mark.parametrize('color', [['Black'], ['Grey'], ['Black', 'Grey'], []])
    def test_create_order_code_201(self, color):
        payload = fake_create_order()
        color_samokat = payload['color'] = color
        response = requests.post(f'{URL}{self.ENDPOINT}', json.dumps(payload))
        assert response.json() == {'track': response.json()['track']}
        assert response.status_code == 201