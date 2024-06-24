import logging
import uuid
from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.services.interfaces.product import ProductInterface
from app.domain.entities.product import Product

from app.infrastracture.models import ProductModel
from app.settings.config import get_db

logger = logging.getLogger(__name__)


class ProductAdapter(ProductInterface):
    """Адаптер для работы с продуктами."""

    def __init__(self):
        self.db_session = get_db()

    def create(self, name: str, price: float) -> Product:
        """Создать продукт."""
        product = ProductModel(uuid=uuid.uuid4(), name=name, price=price)
        self.db_session.add(product)
        self.db_session.commit()
        logger.info(f"Created new product with id: {product.uuid}")
        return Product(id=product.uuid, name=product.name, price=product.price)

    def get(self, id_: str) -> Optional[Product]:
        """Получить продукт"""
        product = self.db_session.query(ProductModel).filter_by(uuid=id_).first()
        if product:
            logger.info(f"Retrieved product with id: {id_}")
        else:
            logger.info(f"Product with id {id_} not found")
        return Product(id=product.uuid, name=product.name, price=product.price)

    def delete(self, id_: str) -> Optional[Product]:
        """Удалить продукт."""
        product = self.db_session.query(ProductModel).filter_by(uuid=id_).first()
        if product:
            self.db_session.delete(product)
            self.db_session.commit()
            logger.info(f"Deleted product with id: {id_}")
        return Product(id=product.uuid, name=product.name, price=product.price)

    def get_all(self) -> List[Product]:
        """Получить все доступные продукты."""
        products = self.db_session.query(ProductModel).all()
        logger.info("Retrieved all products")
        return [Product(id=product.uuid, name=product.name, price=product.price) for product in products]

    def update_name(self, id_: str, name: str) -> Product:
        """Обновить имя продукта."""
        product = self.db_session.query(ProductModel).filter_by(uuid=id_).first()
        if product:
            product.name = name
            self.db_session.commit()
            logger.info(f"Updated name of product {id_} to {name}")
        return Product(id=product.uuid, name=product.name, price=product.price)

    def update_price(self, id_: str, price: float) -> Product:
        """Обновить цену продукта."""
        product = self.db_session.query(ProductModel).filter_by(uuid=id_).first()
        if product:
            product.price = price
            self.db_session.commit()
            logger.info(f"Updated price of product {id_} to {price}")
        return Product(id=product.uuid, name=product.name, price=product.price)
