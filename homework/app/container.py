from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.settings.app import AppSettings

from app.infrastracture.pg_adapter.cart import CartAdapter
from app.infrastracture.pg_adapter.product import ProductAdapter


class AppContainer(DeclarativeContainer):
    app_settings: Singleton["AppSettings"] = Singleton(AppSettings)
    product_adapter: Singleton["ProductAdapter"] = Singleton(ProductAdapter)
    cart_adapter: Singleton["CartAdapter"] = Singleton(CartAdapter)


APP_CONTAINER = AppContainer()
