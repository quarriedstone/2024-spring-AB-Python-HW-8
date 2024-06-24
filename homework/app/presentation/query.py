# Определение класса корневого запроса
import logging
from typing import List, Optional

import strawberry

from app.container import APP_CONTAINER
from app.domain.entities.cart import Cart
from app.domain.entities.product import Product

logger = logging.getLogger(__name__)


@strawberry.type
class Query:
    # Метод для получения списка товаров
    @strawberry.field
    def products(self) -> List[Product]:
        """Логика для получения списка товаров"""
        logger.info("Fetching products")
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.get_all()

    # Метод для получения товара по id
    @strawberry.field
    def product(self, id_: str) -> Optional[Product]:
        """Логика для получения списка товаров"""
        logger.info(f"Fetching product with id: {id_}")
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.get(id_=id_)

    # Метод для получения корзины по id
    @strawberry.field
    def cart(self, id_: str) -> Cart:
        """Логика для получения корзины товаров по id"""
        logger.info(f"Fetching cart with id: {id_}")
        cart_adapter = APP_CONTAINER.cart_adapter()
        return cart_adapter.get(id_=id_)
