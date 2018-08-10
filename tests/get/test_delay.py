import time
import pytest
import requests
import math


class TestDelay:
    url = "https://reqres.in/api/users"

    @pytest.mark.parametrize('params', [{'delay': -1}, {'delay': 0}, {'delay': 3}, ])
    def test_delay(self, params):
        start = time.time()
        resp = requests.request("GET", url=self.url, params=params)
        end = time.time()
        result = math.trunc(end - start)
        if params['delay'] >= 0:
            assert result == params['delay']

        assert resp.status_code == 200
        assert len(resp.json()['data']) > 0
