import pytest
import requests
import allure


class TestConnection:
    url = "https://reqres.in/api/users"

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_connection_success(self):
        with allure.step("Проверка соединения"):
            resp = requests.request("GET", url=self.url)
            allure.attach("expected status code", 200)
            allure.attach("real status code", resp.status_code)
            assert resp.status_code == 200
