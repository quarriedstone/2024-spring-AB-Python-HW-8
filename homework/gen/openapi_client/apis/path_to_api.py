import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.cart_cart_id import CartCartId
from openapi_client.apis.paths.cart_ import Cart
from openapi_client.apis.paths.products_ import Products
from openapi_client.apis.paths.products_product_id import ProductsProductId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CART_CART_ID: CartCartId,
        PathValues.CART_: Cart,
        PathValues.PRODUCTS_: Products,
        PathValues.PRODUCTS_PRODUCT_ID: ProductsProductId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CART_CART_ID: CartCartId,
        PathValues.CART_: Cart,
        PathValues.PRODUCTS_: Products,
        PathValues.PRODUCTS_PRODUCT_ID: ProductsProductId,
    }
)
