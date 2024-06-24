import logging
import uuid
from typing import List, Optional, Dict

from app.domain.services.interfaces.product import ProductInterface
from app.domain.entities.product import Product

logger = logging.getLogger(__name__)


class ProductAdapter(ProductInterface):
    """Адаптер для работы с продуктами."""

    _products: Dict[str, Product]

    def __init__(self):
        self._products = {}

    def create(self, name: str, price: float) -> Product:
        """Создать продукт."""
        product = Product(id=str(uuid.uuid4()), name=name, price=price)
        self._products[product.id] = product
        logger.info(f"Created new product with id: {product.id}")
        return product

    def get(self, id_: str) -> Optional["Product"]:
        """Получить продукт"""
        product = self._products.get(id_)
        if product:
            logger.info(f"Retrieved product with id: {id_}")
        else:
            logger.info(f"Product with id {id_} not found")
        return product

    def delete(self, id_: str) -> Optional[Product]:
        """Удалить продукт."""
        product = self._products.pop(id_, None)
        if product:
            logger.info(f"Deleted product with id: {id_}")
        else:
            logger.info(f"Product with id {id_} not found for deletion")
        return product

    def get_all(self) -> List[Product]:
        """Получить все доступные продукты."""
        logger.info("Retrieved all products")
        return list(self._products.values())

    def update_name(self, id_: str, name: str) -> Product:
        """Обновить имя продукта."""
        product = self._products[id_]
        product.name = name
        logger.info(f"Updated name of product {id_} to {name}")
        return product

    def update_price(self, id_: str, price: float) -> Product:
        """Обновить цену продукта."""
        product = self._products[id_]
        product.price = price
        logger.info(f"Updated price of product {id_} to {price}")
        return product
