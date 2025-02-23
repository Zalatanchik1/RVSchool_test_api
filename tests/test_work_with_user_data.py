import httpx
import datetime

from jsonschema import validate
from core.contracts import CREATED_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
CREATE_USER = 'api/users'

def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    assert response.status_code == 201
    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEMA)
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEMA)
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEMA)
    assert response_json['name'] == body['name']
    assert creation_date[0:16] == current_date[0:16]
