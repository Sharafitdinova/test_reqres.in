import requests
import pytest
import json
from requests_toolbelt.utils import dump

url = "https://reqres.in/api/"


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
class SingleGet:

    @pytest.mark.parametrize('test', [-1, 0, 23])
    def test_not_found_digit(self, test):
        """
            :test: тестовый id для подстановки в url
        """
        resp = requests.request("GET", url=url + self.url + str(test))
        assert resp.status_code == 404

    @pytest.mark.parametrize('test', ["some", "word"])
    def test_not_found_string(self, test):
        resp = requests.request("GET", url=url + self.url + str(test))
        assert resp.status_code == 404

    @pytest.mark.parametrize('test', [1, 10])
    def test_found(self, test):
        resp = requests.request("GET", url=url + self.url + str(test))
        assert resp.status_code == 200
        assert resp.json()['data']['id'] == test


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
class ListGet:

    @pytest.mark.parametrize('page', [-1, 0, 2, 4])
    def test_list_found_page_digit(self, page):
        """
            :page: page для подстановки в url
        """
        resp = requests.request("GET", url=url + self.url + str(page), params={'page': page})
        assert resp.status_code == 200
        if page == 0:
            assert int(resp.json()['page']) == 1
        else:
            assert int(resp.json()['page']) == page

    @pytest.mark.parametrize('page', ['some', 'word'])
    def test_list_found_page_string(self, page):
        resp = requests.request("GET", url=url + self.url + page, params={'page': page})
        assert resp.status_code == 200
        assert int(resp.json()['page']) == 1

    def test_list_found_page_no_params(self):
        resp = requests.request("GET", url=url + self.url)
        assert resp.status_code == 200
        assert int(resp.json()['page']) == 1

    @pytest.mark.parametrize('page', [7, 77777])
    def test_list_not_found_data(self, page):
        resp = requests.request("GET", url=url + self.url, params={'page': page})
        assert resp.status_code == 200
        print(json.dumps(resp.json(), indent=3))
        assert resp.json()['data'] == []
