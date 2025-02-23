import httpx
import allure
import datetime

from jsonschema import validate

from core.contracts import UPDATE_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
SINGLE_USER = 'api/users/2'
UNKNOWN_USER = 'api/users/23'


@allure.suite('Проверка запроса полного обновления пользователя')
@allure.title('Проверка запроса полного обновления пользователя со всеми ключ-значения')
def test_put_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.put(BASE_URL + SINGLE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200

    response_json = response.json()
    with allure.step('Переменной update_date присваиваем значение updatedAt, в полученной вместо "Т" ставим Пробел'):
        update_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с update_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа JOB равняется значению ключа JOB указанного в BODY'):
        assert response_json['job'] == body['job']
    with allure.step('Проверка что значение созданного ключа NAME равняется значению ключа NAME указанного в BODY'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса полного обновления пользователя')
@allure.title('Проверка запроса полного обновления пользователя без ключ-значения NAME')
def test_put_user_without_name():
    body = {
        "job": "zion resident"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.put(BASE_URL + SINGLE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200

    response_json = response.json()
    with allure.step('Переменной update_date присваиваем значение updatedAt, в полученной вместо "Т" ставим Пробел'):
        update_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с update_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа JOB равняется значению ключа JOB указанного в BODY'):
        assert response_json['job'] == body['job']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса полного обновления пользователя')
@allure.title('Проверка запроса полного обновления пользователя без ключ-значения JOB')
def test_put_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.put(BASE_URL + SINGLE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200

    response_json = response.json()
    with allure.step('Переменной update_date присваиваем значение updatedAt, в полученной вместо "Т" ставим Пробел'):
        update_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с update_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа NAME равняется значению ключа NAME указанного в BODY'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert update_date[0:16] == current_date[0:16]
    print(response_json)


@allure.suite('Проверка запроса частичного обновления пользователя')
@allure.title('Проверка запроса частичного обновления пользователя со всеми ключ-значения')
def test_patch_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.patch(BASE_URL + SINGLE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200

    response_json = response.json()
    with allure.step('Переменной update_date присваиваем значение updatedAt, в полученной вместо "Т" ставим Пробел'):
        update_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с update_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа JOB равняется значению ключа JOB указанного в BODY'):
        assert response_json['job'] == body['job']
    with allure.step('Проверка что значение созданного ключа NAME равняется значению ключа NAME указанного в BODY'):
        assert response_json['name'] == body['name']
    with allure.step(
            'Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса частичного обновления пользователя')
@allure.title('Проверка запроса частичного обновления пользователя без ключ-значения NAME')
def test_patch_user_without_name():
    body = {
        "job": "zion resident"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.patch(BASE_URL + SINGLE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200

    response_json = response.json()
    with allure.step('Переменной update_date присваиваем значение updatedAt, в полученной вместо "Т" ставим Пробел'):
        update_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с update_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа JOB равняется значению ключа JOB указанного в BODY'):
        assert response_json['job'] == body['job']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса частичного обновления пользователя')
@allure.title('Проверка запроса частичного обновления пользователя без ключ-значения JOB')
def test_patch_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.patch(BASE_URL + SINGLE_USER, json=body)
    with allure.step('Проверка получения статус кода ответа: 200'):
        assert response.status_code == 200

    response_json = response.json()
    with allure.step('Переменной update_date присваиваем значение updatedAt, в полученной вместо "Т" ставим Пробел'):
        update_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step('Приводим значение в String для дальнейшего сравнения current_date с update_date'):
        current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверка что значение созданного ключа NAME равняется значению ключа NAME указанного в BODY'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка что дата создания ресурса равняется текущей дате в момент создания, для точности делается выборка из первых 15-ти символов'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Проверка запроса удаления пользователя')
@allure.title('Проверка запроса удаления пользователя')
def test_delete_user():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.delete(BASE_URL + SINGLE_USER)
    with allure.step('Проверка получения статус кода ответа: 204'):
        assert response.status_code == 204
