import allure
import pytest
from src.http_client import HttpMethods
from json import dumps
from helpers import Generator

ORDER = '/orders'
TRACK = '/orders/track'

class TestPostOrders:

    @allure.title('Тест создания заказа')
    @pytest.mark.parametrize("color", ["", ["Grey"], ["Black"], ["Grey", "Black"]])
    def test_create_order(self, http_client, color):
        gen = Generator()
        payload = gen.generate_order_data()
        payload["color"] = color
        response = http_client.send_request(HttpMethods.POST, ORDER, data=dumps(payload))
        assert response.status_code == 201, 'Wrong code'
        assert response.json()['track'] is not None


class TestGetOrder:
    @allure.title('Тест получения списка заказов')
    def test_get_orders(self, http_client):
        response = http_client.send_request(HttpMethods.GET, ORDER, data=None)
        assert response.json()['orders'] is not None