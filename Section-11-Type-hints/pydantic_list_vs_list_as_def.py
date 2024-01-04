from typing import List
from pydantic import BaseModel, StrictStr


class Lists(BaseModel):
    simple_list: list = None
    typing_list: List = None


print(
    Lists(simple_list = [1, 2, 3])
)