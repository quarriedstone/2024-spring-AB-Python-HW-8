import logging
import uuid
from typing import Optional, Dict

from sqlalchemy.orm import Session

from app.domain.entities.product import ProductQuantity
from app.domain.services.interfaces.cart import CartInterface
from app.domain.entities.cart import Cart

from app.infrastracture.models import CartModel, ProductModel, ProductQuantityModel
from app.settings.config import get_db

logger = logging.getLogger(__name__)


class CartAdapter(CartInterface):
    """Адаптер для работы с продуктами."""

    def __init__(self):
        self.db_session = get_db()

    def create(self) -> Cart:
        """Создать корзину."""
        cart = CartModel(uuid=uuid.uuid4())
        self.db_session.add(cart)
        self.db_session.commit()
        logger.info(f"Created new cart with id: {cart.uuid}")
        return Cart(id=cart.uuid, products=cart.products)

    def get(self, id_: str) -> Optional[Cart]:
        """Получить корзину."""
        cart = self.db_session.query(CartModel).filter_by(uuid=id_).first()
        if cart:
            logger.info(f"Retrieved cart with id: {id_}")
        else:
            logger.info(f"Cart with id {id_} not found")
        return Cart(id=cart.uuid, products=[ProductQuantity(product_id=product.product_id, quantity=product.quantity) for product in cart.products])

    def delete(self, id_: str) -> Optional[Cart]:
        """Удалить корзину."""
        cart = self.db_session.query(CartModel).filter_by(uuid=id_).first()
        if cart:
            self.db_session.delete(cart)
            self.db_session.commit()
            logger.info(f"Deleted cart with id: {id_}")
        return Cart(id=cart.uuid, products=cart.products)

    def add_product(self, id_: str, product_id: str) -> Cart:
        """Добавить продукт в корзину."""
        cart = self.get(id_)
        if cart:
            product = self.db_session.query(ProductModel).filter_by(uuid=product_id).first()
            if not product:
                logger.warning(f"Product with id {product_id} not found")
                return cart
            product_quantity = self.db_session.query(ProductQuantityModel).filter_by(cart_id=id_, product_id=product_id).first()
            if product_quantity:
                logger.warning(f"Product with id {product_id} already exists in cart {id_}")
                return cart
            product_quantity = ProductQuantityModel(uuid=uuid.uuid4(), cart_id=id_, product_id=product_id, quantity=1)
            self.db_session.add(product_quantity)
            self.db_session.commit()
            logger.info(f"Added product with id {product_id} to cart {id_}")
            return self.get(id_)
        return cart

    def change_product_quantity(self, id_: str, product_id: str, quantity: int) -> Cart:
        """Изменить кол-во товаров в корзине."""
        cart = self.get(id_)
        if cart:
            product_quantity = self.db_session.query(ProductQuantityModel).filter_by(cart_id=id_, product_id=product_id).first()
            if product_quantity:
                product_quantity.quantity = quantity
                self.db_session.commit()
                logger.info(f"Changed quantity of product {product_id} in cart {id_} to {quantity}")
        return self.get(id_)
