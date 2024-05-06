import uuid
from http import HTTPStatus
from typing import Dict, Optional, List

import uvicorn as uvicorn
from fastapi import FastAPI

from class_content.domain import UserModelId, UserModel, UserId

app = FastAPI()

users: Dict[str, UserModelId] = {}


@app.post("/users")
def create_user(user: UserModel) -> UserId:
    new_user = UserModelId(**user.model_dump(), user_id=uuid.uuid4())
    users[str(new_user.user_id)] = new_user
    return UserId(user_id=new_user.user_id)


@app.get("/users")
def get_user() -> List[UserModelId]:
    return users.values()


@app.get("/users/{user_id}")
def get_user_by_id(user_id: str):
    if user := users.get(user_id):
        return user
    return HTTPStatus.NOT_FOUND


@app.put("/users/{user_id}")
def update_user_by_id(user: UserModel, user_id: str):
    if old_user := users.get(user_id):
        old_user.login = user.login
        old_user.name = user.name
        old_user.password = user.password
    else:
        return HTTPStatus.NOT_FOUND

    return HTTPStatus.OK


@app.delete("/users/{user_id}")
def update_user_by_id(user_id: str):
    if users.get(user_id):
        del users[user_id]
    else:
        return HTTPStatus.NOT_FOUND

    return HTTPStatus.OK


if __name__ == '__main__':
    uvicorn.run(app)
