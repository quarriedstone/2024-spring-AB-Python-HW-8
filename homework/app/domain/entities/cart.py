from typing import List, Optional

from pydantic import BaseModel
from homework.app.domain.entities.product import ProductQuantity


# Определение класса корзины
class Cart(BaseModel):
    id: str
    products: List[Optional[ProductQuantity]]
