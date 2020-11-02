import pytest
import requests


class APIClient:
    """
    Client for work with API
    with GET/POST requests
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path="/", params=None):
        url = self.base_url + path
        return requests.get(url, params=params)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_url + path
        return requests.post(url=url, params=params, data=data, headers=headers)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="Request URL"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_url=base_url)
