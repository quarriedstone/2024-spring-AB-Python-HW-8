from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.domain.entities.cart import Cart


class CartInterface(Protocol):
    """Интерфейс для работы с корзиной."""

    @abstractmethod
    def create(self) -> "Cart":
        """Создать корзину."""

    @abstractmethod
    def get(self, id_: str) -> Optional["Cart"]:
        """Получить корзину."""

    @abstractmethod
    def delete(self, id_: str) -> Optional["Cart"]:
        """Удалить корзину."""

    @abstractmethod
    def add_product(self, id_: str, product_id: str) -> "Cart":
        """Добавить продукт в корзину."""

    @abstractmethod
    def change_product_quantity(self, id_: str, product_id: str, quantity: int) -> "Cart":
        """Изменить кол-во товаров в корзине."""
