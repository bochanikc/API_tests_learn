import pytest
import requests


class APIClient:
    """
    Client for work with API
    with GET/POST requests
    """

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get(self, path="/", params=None, headers=None):
        url = self.base_url + path
        return requests.get(url, params=params, headers=headers)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_url + path
        return requests.post(url=url, params=params, data=data, headers=headers)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        # default="https://jsonplaceholder.typicode.com",
        # default="https://api.weather.yandex.ru",
        help="Request URL"
    )

    parser.addoption(
        "--token",
        action="store",
        help="Token for yandex API"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    token = request.config.getoption("--token")
    return APIClient(base_url=base_url, token=token)
