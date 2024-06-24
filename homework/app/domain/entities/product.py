# Определение класса товара
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Product(BaseModel):
    id: UUID
    name: str
    price: float = 0.


class ProductInput(BaseModel):
    """
    Хорошим тоном является
    использование таких Input классов.
    Отделяем сущность бизнес-логики Product от сущности,
    которую присылает пользователь.
    """
    name: str
    price: Optional[float] = None


class ProductQuantity(BaseModel):
    product: Product
    quantity: int
