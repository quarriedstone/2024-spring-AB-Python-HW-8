from fastapi import FastAPI

from homework.app.presentation import cart
from homework.app.presentation import products


def get_app() -> FastAPI:
    """Создание экземпляра FastAPI"""
    app = FastAPI()
    app.include_router(cart.router)
    app.include_router(products.router)

    return app
