import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from app.presentation.graphql.mutation import Mutation
from app.presentation.graphql.query import Query
from app.presentation.rest.handlers import router


def _get_graphql_app() -> GraphQL:
    """Создание схемы strawberry с параметрами."""
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQL(schema)
    return graphql_app


def get_app() -> FastAPI:
    """Создание экземпляра FastAPI"""

    graphql_app = _get_graphql_app()

    app = FastAPI()
    app.add_route("/graphql", graphql_app)
    app.add_websocket_route("/graphql", graphql_app)

    app.include_router(router)

    return app
