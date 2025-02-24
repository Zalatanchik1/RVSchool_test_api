import httpx
import allure

from core.contracts import UPDATE_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
SINGLE_USER = 'api/users/2'
UNKNOWN_USER = 'api/users/23'

@allure.suite('Проверка запроса удаления пользователя')
@allure.title('Проверка запроса удаления пользователя')
def test_delete_user():
    with allure.step(f'Выполняем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.delete(BASE_URL + SINGLE_USER)
    with allure.step('Проверка получения статус кода ответа: 204'):
        assert response.status_code == 204