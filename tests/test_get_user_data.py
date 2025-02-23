import httpx
import allure

from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
SINGLE_USER = 'api/users/2'
NOT_FOUND_USER = 'api/users/23'
EMAIL_ENDS = '@reqres.in'

@allure.suite('Проверка запроса данных пользователя')
@allure.title('Проверка запроса получения списка данных пользователей')
def test_list_users():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Проверка элемента из списка'):
            validate(item, USER_DATA_SCHEMA)
            with allure.step(f'Проверка что в конце значения ключа EMAIL отображается {EMAIL_ENDS}'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step('Проверка наличия ID в ссылке на аватарку'):
                assert str(item['id']) in item['avatar']

@allure.suite('Проверка запроса данных пользователя')
@allure.title('Проверка запроса получения данных одного пользователя')
def test_single_user():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step(f'Проверка что в конце значения ключа EMAIL отображается {EMAIL_ENDS}'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверка наличия ID в ссылке на аватарку'):
        assert str(data['id']) in data['avatar']

@allure.suite('Проверка запроса данных пользователя')
@allure.title('Проверка запроса получения ошибки в случае отсутствия данных пользователя')
def test_user_not_found():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + NOT_FOUND_USER}'):
        response = httpx.get(BASE_URL + NOT_FOUND_USER)
    with allure.step('Проверка получения статус кода ответа: 404'):
        assert  response.status_code == 404