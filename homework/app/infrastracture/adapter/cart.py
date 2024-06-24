import logging
import uuid
from typing import Optional, Dict

from app.domain.entities.product import ProductQuantity
from app.domain.services.interfaces.cart import CartInterface
from app.domain.entities.cart import Cart

logger = logging.getLogger(__name__)


class CartAdapter(CartInterface):
    """Адаптер для работы с продуктами."""

    _carts: Dict[str, Cart]

    def __init__(self):
        self._carts = {}

    def create(self) -> "Cart":
        """Создать корзину."""
        cart = Cart(id=str(uuid.uuid4()), products=[])
        self._carts[cart.id] = cart
        logger.info(f"Created new cart with id: {cart.id}")
        return cart

    def get(self, id_: str) -> Optional["Cart"]:
        """Получить корзину."""
        cart = self._carts.get(id_)
        if cart:
            logger.info(f"Retrieved cart with id: {id_}")
        else:
            logger.info(f"Cart with id {id_} not found")
        return cart

    def delete(self, id_: str) -> Optional["Cart"]:
        """Удалить корзину."""
        return self._carts.pop(id_)

    def add_product(self, id_: str, product_id: str) -> "Cart":
        """Добавить продукт в корзину."""
        cart = self.get(id_)
        if cart:
            for product in cart.products:
                if product.product_id == product_id:
                    logger.warning(f"Product with id {product_id} already exists in cart {id_}")
                    return cart
            product_quantity = ProductQuantity(product_id=product_id, quantity=1)
            cart.products.append(product_quantity)
            logger.info(f"Added product with id {product_id} to cart {id_}")
        return cart

    def change_product_quantity(self, id_: str, product_id: str, quantity: int) -> "Cart":
        """Изменить кол-во товаров в корзине."""
        cart = self.get(id_)
        if cart:
            for product_quantity in cart.products:
                if product_quantity.product_id == product_id:
                    product_quantity.quantity = quantity
                    logger.info(f"Changed quantity of product {product_id} in cart {id_} to {quantity}")
                    break
        return cart
