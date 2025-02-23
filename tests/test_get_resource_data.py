import httpx
from jsonschema import validate

from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URl = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_RESOURCE = 'api/unknown/23'
DASH = '-'
OCTOTHORPE = '#'


def test_list_resource():
    response = httpx.get(BASE_URl + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert item['color'].startswith(OCTOTHORPE)
        assert DASH in item['pantone_value']


def test_single_resource():
    response = httpx.get(BASE_URl + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['color'].startswith(OCTOTHORPE)
    assert DASH in data['pantone_value']


def test_resource_not_found():
    response = httpx.get(BASE_URl + NOT_FOUND_RESOURCE)
    assert  response.status_code == 404
