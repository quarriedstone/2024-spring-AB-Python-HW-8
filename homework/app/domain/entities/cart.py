from typing import List, Optional

import strawberry

from app.domain.entities.product import ProductQuantity


# Определение класса корзины
@strawberry.type
class Cart:
    id: str
    products: List[Optional[ProductQuantity]]
