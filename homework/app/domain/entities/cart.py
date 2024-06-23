from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel
from homework.app.domain.entities.product import ProductQuantity


# Определение класса корзины
class Cart(BaseModel):
    id: UUID
    products: List[Optional[ProductQuantity]]
