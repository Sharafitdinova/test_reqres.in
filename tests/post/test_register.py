import requests
import pytest
import json

url = 'https://reqres.in/api/register'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
class TestRegister:

    @pytest.mark.parametrize('data', [
        {'email': 'sydney@fife', 'password': 'pistol'},
        {'email': 1, "password": 2}
    ])
    def test_register_success(self, data):
        """
        :data: входной набор
        """
        resp = requests.request("POST", url=url, data=data)
        assert resp.status_code == 201
        assert 'token' in resp.json()

    @pytest.mark.parametrize('data, error', [
        ({'email': 'sydney@fife'}, 'Missing password'),
        ({}, 'Missing email or username'),
        ({'password': 'password'}, 'Missing email or username'),
    ])
    def test_register_failure(self, data, error):
        """
        Попытки с неполными или пуcтыми парами логин/пароль
        :data: входной набор
        :error: ответ с ошибкой
        """
        resp = requests.request("POST", url=url, data=data)
        assert resp.status_code == 400
        assert 'error' in resp.json()
        assert resp.json()['error'] == error
