import pytest
import requests


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
class TestDelete:
    url = "https://reqres.in/api/users"

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus', 'job': 'leader', 'id': '557'}
    ])
    @pytest.mark.parametrize('test', [-1, 0, 2, 100, ''])
    def test_delete_with_success(self, data, test):
        """
        :data: входной набор
        :test: id для подстановки в url
        """
        if test == '':
            resp = requests.request("DELETE", url=self.url, data=data)
        else:
            resp = requests.request("DELETE", url='{0}/{1}'.format(self.url, str(test)), data=data)
        assert resp.status_code == 204

