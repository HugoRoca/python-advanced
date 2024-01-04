from typing import Union
from uuid import UUID
from pydantic import BaseModel


class User(BaseModel):
    id: Union[UUID, str, int, list]
    username: str


print(
    User(id=[], username="Hugo")
)