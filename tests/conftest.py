import pytest
from src.http_client import HttpClient, HttpMethods
from helpers import Generator

URL = 'https://qa-scooter.praktikum-services.ru/api/v1'

@pytest.fixture()
def http_client():
    return HttpClient(URL)

@pytest.fixture()
def create_courier(http_client):
    gen = Generator()
    payload = gen.generate_auth_data()
    response = http_client.send_request(HttpMethods.POST, "/courier", data=payload)
    return payload