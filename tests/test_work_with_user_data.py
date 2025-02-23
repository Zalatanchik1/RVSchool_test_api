import httpx
import datetime
import allure

from jsonschema import validate
from core.contracts import CREATED_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
CREATE_USER = 'api/users'


@allure.suite('Проверка запроса создания пользователя')
@allure.title('Проверка запроса создания пользователя со всеми ключ-значения')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 201'):
        assert response.status_code == 201
    response_json = response.json()
    with allure.step('Переменной creation_date присваиваем значение createdAt, в полученной вместо "Т" ставим Пробел'):
        creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с creation_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа NAME равняется значению ключа NAME указанного в BODY'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка что значение созданного ключа JOB равняется значению ключа JOB указанного в BODY'):
        assert response_json['job'] == body['job']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса создания пользователя')
@allure.title('Проверка запроса создания пользователя без ключ-значения NAME')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 201'):
        assert response.status_code == 201

    response_json = response.json()
    with allure.step('Переменной creation_date присваиваем значение createdAt, в полученной вместо "Т" ставим Пробел'):
        creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с creation_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа JOB равняется значению ключа JOB указанного в BODY'):
        assert response_json['job'] == body['job']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса создания пользователя')
@allure.title('Проверка запроса создания пользователя без ключ-значения JOB')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 201'):
        assert response.status_code == 201

    response_json = response.json()
    with allure.step('Переменной creation_date присваиваем значение createdAt, в полученной вместо "Т" ставим Пробел'):
        creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с creation_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа NAME равняется значению ключа NAME указанного в BODY'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert creation_date[0:16] == current_date[0:16]
