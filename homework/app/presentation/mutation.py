# Определение класса корневой мутации
import logging

import strawberry

from app.container import APP_CONTAINER
from app.domain.entities.cart import Cart
from app.domain.entities.product import Product, ProductInput, ProductUpdate, ProductQuantityInput

logger = logging.getLogger(__name__)


@strawberry.type
class Mutation:
    # Метод для создания продукта
    @strawberry.mutation
    def create_product(self, product_info: ProductInput) -> Product:
        """Логика создания продукта"""
        logger.info("Creating product")
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.create(
            name=product_info.name, price=float(product_info.price) if product_info.price else 0
        )

    @strawberry.mutation
    def update_product_info(self, id_: str, product_update: ProductUpdate) -> Product:
        """Обновить данные о продукте."""
        logger.info(f"Updating product with id: {id_}")
        product_adapter = APP_CONTAINER.product_adapter()
        if product_update.name:
            product_adapter.update_name(id_=id_, name=product_update.name)
        if product_update.price:
            product_adapter.update_price(id_=id_, price=float(product_update.price))
        return product_adapter.get(id_=id_)

    @strawberry.mutation
    def create_cart(self) -> Cart:
        """Логика создания корзины"""
        logger.info("Creating cart")
        cart_adapter = APP_CONTAINER.cart_adapter()
        return cart_adapter.create()

    @strawberry.mutation
    def add_to_cart(self, cart_id: str, product_quantity_input: ProductQuantityInput) -> Cart:
        """Метод добавления товара в корзину"""
        logger.info(f"Adding product to cart with id: {cart_id}")
        cart_adapter = APP_CONTAINER.cart_adapter()
        cart_adapter.add_product(id_=cart_id, product_id=product_quantity_input.product_id)
        cart_adapter.change_product_quantity(
            id_=cart_id, product_id=product_quantity_input.product_id, quantity=product_quantity_input.quantity
        )
        return cart_adapter.get(id_=cart_id)
