# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CART_CART_ID = "/cart/{cart_id}"
    CART_ = "/cart/"
    PRODUCTS_ = "/products/"
    PRODUCTS_PRODUCT_ID = "/products/{product_id}"
