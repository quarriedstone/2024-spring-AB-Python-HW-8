# Определение класса товара
from typing import Optional

import strawberry


@strawberry.type
class Product:
    id: str
    name: str
    price: float = 0.0


@strawberry.input
class ProductInput:
    name: str
    price: Optional[float] = None


@strawberry.input
class ProductUpdate:
    name: Optional[str] = None
    price: Optional[float] = None


@strawberry.type
class ProductQuantity:
    product_id: str
    quantity: int


@strawberry.input
class ProductQuantityInput:
    product_id: str
    quantity: int
