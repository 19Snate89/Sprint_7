import allure
import pytest
from src.http_client import HttpMethods
from helpers import Generator, StaticData


COURIER = '/courier'
LOGIN = '/courier/login'

class TestPostCouriers:

    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @allure.title('Тест создания курьера')
    def test_register_new_courier_and_return_login_password(self, http_client):
        with allure.step('Создаем курьера в системе'):
            gen = Generator()
            payload = gen.generate_auth_data()
            response = http_client.send_request(HttpMethods.POST, COURIER, data=payload)
            assert response.status_code == 201
            assert response.json()["ok"] == True


    @allure.title('Тест создания курьера с повторяющимся логином')
    def test_login_courier_with_repeat_login(self, http_client, create_courier):
        with allure.step('Создаем курьера в системе'):
            data = create_courier
            payload = {
                "login": data['login'],
                "password": data['password']
            }
        with allure.step('Проверяем, что возвращается код 409 и сообщение "Этот логин уже используется"'):
            response = http_client.send_request(HttpMethods.POST, COURIER, data=payload)
            assert response.status_code == 409, 'Wrong code'
            assert response.json()['message'] == StaticData.COURIER["already_exist"]


    @allure.title('Тест авторизации курьера с валидными данными')
    def test_login_courier_with_valid_data(self, http_client, create_courier):
        with allure.step('Создаем курьера в системе'):
            data = create_courier
            payload = {
                "login": data['login'],
                "password": data['password']
            }
        with allure.step('Проверяем, что возвращается код 200 и возвращается "id"'):
            response = http_client.send_request(HttpMethods.POST, LOGIN, data=payload)
            assert response.status_code == 200, 'Wrong code'
            assert response.json()['id'] is not None


    @allure.title('Тест авторизации курьера с некорректными данными')
    @pytest.mark.parametrize("log, pas", [("", ""), ("testlogin", ""), ("", "testpass")])
    def test_login_courier_with_invalid_data(self, http_client, log, pas):
        payload = {
            "login":  log,
            "password": pas
        }
        response = http_client.send_request(HttpMethods.POST, LOGIN, data=payload)
        with allure.step('Проверяем, что возвращается код 400 и сообщение "Недостаточно данных для входа"'):
            assert response.status_code == 400
            assert response.json()['message'] == StaticData.COURIER["wrong_data"]



    @allure.title('Тест авторизации курьера с некорректным указанием логина или пароля')
    @pytest.mark.parametrize("log, pas", [("rmbjwooljd", "Ghkqfjmyxn1"), ("Rmbjwooljd", "ghkqfjmyxn")])
    def test_login_courier_with_invalid_para_logpass(self, http_client, log, pas):
        payload = {
            "login":  log,
            "password": pas
        }
        response = http_client.send_request(HttpMethods.POST, LOGIN, data=payload)
        with allure.step('Проверяем, что возвращается код 404 и сообщение "Учетная запись не найдена"'):
            assert response.status_code == 404
            assert response.json()['message'] == StaticData.COURIER["invalid_logpass"]

