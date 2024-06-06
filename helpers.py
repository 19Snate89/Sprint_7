from faker import Faker
import random

class StaticData:


    COURIER = {
        "already_exist": "Этот логин уже используется. Попробуйте другой.",
        "wrong_data": "Недостаточно данных для входа",
        "invalid_logpass": "Учетная запись не найдена"
    }

class Generator:

    def generate_auth_data(self):
        data = Faker()
        login = data.user_name()
        password = data.password()
        first_name = data.first_name()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    def generate_order_data(self):
        data = Faker("RU")
        first_name = data.first_name()
        last_name = data.last_name()
        address = data.address()
        metro = random.randint(1, 20)
        phone = data.phone_number()
        rent = random.randint(1, 5)
        date = data.date()
        comment = data.text()

        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro,
            "phone": phone,
            "rentTime": rent,
            "deliveryDate": date,
            "comment": comment,
            }

        return payload
