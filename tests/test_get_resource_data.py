import allure
import httpx
from jsonschema import validate

from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_RESOURCE = 'api/unknown/23'
DASH = '-'
OCTOTHORPE = '#'


@allure.suite('Проверка запроса данных ресурсов')
@allure.title('Проверка запроса получения данных списка ресурсов')
def test_list_resource():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Проверка элемента из списка'):
            validate(item, RESOURCE_DATA_SCHEMA)
            with allure.step(f'Проверка что в начале значения ключа COLOR отображается {OCTOTHORPE}'):
                assert item['color'].startswith(OCTOTHORPE)
            with allure.step('Проверка наличия "-" в ссылке на аватарку'):
                assert DASH in item['pantone_value']


@allure.suite('Проверка запроса данных ресурсов')
@allure.title('Проверка запроса получения данных одного ресурса')
def test_single_resource():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step(f'Проверка что в начале значения ключа COLOR отображается {OCTOTHORPE}'):
        assert data['color'].startswith(OCTOTHORPE)
    with allure.step('Проверка наличия "-" в ссылке на аватарку'):
        assert DASH in data['pantone_value']


@allure.suite('Проверка запроса данных ресурсов')
@allure.title('Проверка запроса получения ошибки в случае отсутствия данных ресурса')
def test_resource_not_found():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + NOT_FOUND_RESOURCE}'):
        response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)
    with allure.step('Проверка получения статус кода ответа: 404'):
        assert  response.status_code == 404
