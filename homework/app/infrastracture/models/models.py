from uuid import UUID

from sqlalchemy import Uuid, String, ForeignKey, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastracture.models.base import BaseModel


class CartModel(BaseModel):
    """БД модель для корзины"""

    __tablename__ = "cart"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, unique=True)
    products = relationship("ProductQuantityModel", back_populates="cart", cascade="all, delete-orphan")


class ProductModel(BaseModel):
    """БД модель для продукта"""

    __tablename__ = "product"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float(), default=0.0)
    carts = relationship("ProductQuantityModel", back_populates="product", cascade="all, delete-orphan")


class ProductQuantityModel(BaseModel):
    """БД модель для учёта кол-ва продуктов в корзине"""

    __tablename__ = "product_quantity"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, unique=True)
    product_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey('product.uuid', ondelete="CASCADE"), nullable=False)
    cart_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey('cart.uuid', ondelete="CASCADE"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    cart = relationship("CartModel", back_populates="products")
    product = relationship("ProductModel", back_populates="carts")
