import pytest
import requests


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
class TestPatch:
    url = "https://reqres.in/api/users"

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus'},
    ])
    @pytest.mark.parametrize('test', [-1, 0, 1, 100, ''])
    def test_patch_success(self, data, test):
        """
        :data: входной набор
        :test: id для подстановки в url
        """
        resp = requests.request("PATCH", url='{0}/{1}'.format(self.url, str(test)), data=data)
        assert resp.status_code == 200
        assert resp.json()['name'] == data['name']
        assert 'updatedAt' in resp.json()