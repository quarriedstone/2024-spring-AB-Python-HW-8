from pydantic import BaseModel, UUID4


class UserModel(BaseModel):
    name: str
    login: str
    password: str


class UserId(BaseModel):
    user_id: UUID4


class UserModelId(UserModel):
    user_id: UUID4
