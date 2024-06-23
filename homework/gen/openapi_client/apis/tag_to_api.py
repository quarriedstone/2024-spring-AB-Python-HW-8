import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.cart_api import CartApi
from openapi_client.apis.tags.products_api import ProductsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CART: CartApi,
        TagValues.PRODUCTS: ProductsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CART: CartApi,
        TagValues.PRODUCTS: ProductsApi,
    }
)
