import httpx

from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
SINGLE_USER = 'api/users/2'
NOT_FOUND_USER = 'api/users/23'
EMAIL_ENDS = '@reqres.in'


def test_list_users():
    response = httpx.get(BASE_URL + LIST_USERS)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEMA)
        assert item['email'].endswith(EMAIL_ENDS)
        assert str(item['id']) in item['avatar']


def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['email'].endswith(EMAIL_ENDS)
    assert str(data['id']) in data['avatar']


def test_user_not_found():
    response = httpx.get(BASE_URL + NOT_FOUND_USER)
    assert  response.status_code == 404