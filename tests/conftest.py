import requests
import pytest
from src.http_client import HttpClient

@pytest.fixture()
def config():
    url = 'https://qa-scooter.praktikum-services.ru/api/v1'
    return {"url": f"{url}"}

@pytest.fixture()
def http_client(config):
    return HttpClient(config["url"])