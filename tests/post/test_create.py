import requests
import pytest
import json

url = 'https://reqres.in/api/users/'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
class TestCreate:

    @pytest.mark.parametrize('data', [{'name': 'morpheus', 'job': 'leader'}, {'name': '', 'job': ''}])
    def test_create(self, data):
        resp = requests.request("POST", url=url)
        assert resp.status_code == 201
        assert int(resp.json()['id']) > 0
        assert 'createdAt' in resp.json()
