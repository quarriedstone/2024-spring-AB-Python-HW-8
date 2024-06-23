# Определение класса корневой мутации
from typing import Optional, List

from fastapi import APIRouter

from homework.app.container import APP_CONTAINER
from homework.app.domain.entities.product import Product, ProductInput
from homework.app.infrastructure.adapter.exceptions import ProductNotFound


router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get('/')
def get_products() -> List[Product]:
    """Логика для получения списка товаров"""
    product_adapter = APP_CONTAINER.product_adapter()
    return product_adapter.get_all()


@router.post('/')
def create_product(product_info: ProductInput) -> Product:
    """Логика создания продукта"""
    product_adapter = APP_CONTAINER.product_adapter()
    return product_adapter.create(
        name=product_info.name,
        price=float(product_info.price) if product_info.price else 0,
    )


@router.put('/{product_id}')
def update_product_info(product_id: str, product_info: ProductInput) -> Optional[Product]:
    """Обновить данные о продукте."""
    product_adapter = APP_CONTAINER.product_adapter()
    try:
        product_adapter.update_name(product_id, product_info.name)
        product_adapter.update_price(product_id, product_info.price)
    except ProductNotFound:
        return None
    updated_product = product_adapter.get_product_by_id(product_id)
    return updated_product
