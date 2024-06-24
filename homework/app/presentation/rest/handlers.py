import logging

from fastapi import HTTPException, APIRouter
from typing import List

from app.container import APP_CONTAINER
from app.domain.entities.cart import Cart
from app.domain.entities.product import Product

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/products", response_model=List[Product])
def get_products():
    """Endpoint to get the list of products"""
    logger.info("Fetching products")
    product_adapter = APP_CONTAINER.product_adapter()
    return product_adapter.get_all()


@router.get("/products/{id_}", response_model=Product)
def get_product(id_: str):
    """Endpoint to get a product by ID"""
    logger.info(f"Fetching product with id: {id_}")
    product_adapter = APP_CONTAINER.product_adapter()
    product = product_adapter.get(id_=id_)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/carts/{id_}", response_model=Cart)
def get_cart(id_: str):
    """Endpoint to get a cart by ID"""
    logger.info(f"Fetching cart with id: {id_}")
    cart_adapter = APP_CONTAINER.cart_adapter()
    cart = cart_adapter.get(id_=id_)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart


@router.post("/carts", response_model=Cart)
def create_cart():
    """Endpoint to create a new cart"""
    logger.info("Creating a new cart")
    cart_adapter = APP_CONTAINER.cart_adapter()
    return cart_adapter.create()


@router.delete("/carts/{id_}", response_model=Cart)
def delete_cart(id_: str):
    """Endpoint to delete a cart by ID"""
    logger.info(f"Deleting cart with id: {id_}")
    cart_adapter = APP_CONTAINER.cart_adapter()
    cart = cart_adapter.delete(id_=id_)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart


@router.post("/carts/{id_}/products/{product_id}", response_model=Cart)
def add_product_to_cart(id_: str, product_id: str):
    """Endpoint to add a product to a cart"""
    logger.info(f"Adding product with id {product_id} to cart {id_}")
    cart_adapter = APP_CONTAINER.cart_adapter()
    cart = cart_adapter.add_product(id_=id_, product_id=product_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart or Product not found")
    return cart


@router.put("/carts/{id_}/products/{product_id}", response_model=Cart)
def change_product_quantity(id_: str, product_id: str, quantity: int):
    """Endpoint to change the quantity of a product in a cart"""
    logger.info(f"Changing quantity of product {product_id} in cart {id_} to {quantity}")
    cart_adapter = APP_CONTAINER.cart_adapter()
    cart = cart_adapter.change_product_quantity(id_=id_, product_id=product_id, quantity=quantity)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart or Product not found")
    return cart
