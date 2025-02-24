import json
import allure
import httpx
import pytest

from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEMA, ERROR_REGISTERED_USER_SCHEMA, LOGIN_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
REGISTER_USER = 'api/register'
LOGIN_USER = 'api/login'

json_file = open(r'D:\Users\User\PycharmProjects\RVSchool_test_api\core\new_users_data.json')
users_data = json.load(json_file)

json_file_login = open(r'D:\Users\User\PycharmProjects\RVSchool_test_api\core\new_users_login_data.json')
users_data_login = json.load(json_file_login)


@allure.suite('Проверка запроса регистрации пользователя')
@allure.title('Проверка запроса успешной регистрации пользователя')
@pytest.mark.parametrize('users_data', users_data)
def test_successful_register(users_data):
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + REGISTER_USER}'):
        response = httpx.post(BASE_URL + REGISTER_USER, json=users_data)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200
    validate(response.json(), REGISTERED_USER_SCHEMA)


@allure.suite('Проверка запроса авторизации пользователя')
@allure.title('Проверка запроса успешной авторизации пользователя')
@pytest.mark.parametrize('users_data_login', users_data_login)
def test_successful_login(users_data_login):
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + LOGIN_USER}'):
        response = httpx.post(BASE_URL + LOGIN_USER, json=users_data_login)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200
    validate(response.json(), LOGIN_USER_SCHEMA)


@allure.suite('Проверка запроса регистрации пользователя')
@allure.title('Проверка запроса неуспешной регистрации пользователя')
def test_unsuccessful_register():
    body = {
    "email": "sydney@fife"
}
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + REGISTER_USER}'):
        response = httpx.post(BASE_URL + REGISTER_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 400'):
        assert response.status_code == 400
    print(response.json())
    validate(response.json(), ERROR_REGISTERED_USER_SCHEMA)


