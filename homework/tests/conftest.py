import pytest
from openapi_client import ApiClient, Configuration
from openapi_client.apis.tags.cart_api import CartApi
from openapi_client.apis.tags.products_api import ProductsApi


@pytest.fixture(scope="module")
def api_client():
    config = Configuration(host="http://localhost:8000")
    with ApiClient(configuration=config) as api_client:
        yield api_client


@pytest.fixture(scope="module")
def cart_api(api_client):
    return CartApi(api_client)


@pytest.fixture(scope="module")
def products_api(api_client):
    return ProductsApi(api_client)
