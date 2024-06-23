# Определение класса корневого запроса
from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from homework.app.container import APP_CONTAINER
from homework.app.domain.entities.cart import Cart
from homework.app.infrastructure.adapter.exceptions import CartNotFound, ProductNotFound

router = APIRouter(
    prefix="/cart",
    tags=["cart"],
)


@router.get('/{cart_id}')
def get_cart_by_id(cart_id: str) -> Optional[Cart]:
    """Логика для получения корзины товаров по id"""
    cart_adapter = APP_CONTAINER.cart_adapter()
    try:
        cart = cart_adapter.get_cart_by_id(cart_id)
    except CartNotFound:
        return None
    return cart


@router.post('/')
def create_cart() -> Cart:
    """Логика создания корзины"""
    cart_adapter = APP_CONTAINER.cart_adapter()
    return cart_adapter.create()


@router.put('/{cart_id}', response_class=PlainTextResponse)
def add_to_cart(cart_id: str,  product_name: str, quantity: int) -> str:
    """Метод добавления товара в корзину"""
    product_adapter = APP_CONTAINER.product_adapter()
    cart_adapter = APP_CONTAINER.cart_adapter()
    product_id: Optional[str] = None
    all_products = product_adapter.get_all()
    for product in all_products:                # считаем, что имя
        if product.name == product_name:        # однозначно задаёт ID.
            product_id = product.id
            break
    try:
        cart_adapter.add_product(cart_id, product_id)
        cart_adapter.change_product_quantity(cart_id, product_id, quantity)
    except (CartNotFound, ProductNotFound) as e:
        raise HTTPException(status_code=404, detail=str(e))
    return f'Product {product_name} added to cart {cart_id}'
