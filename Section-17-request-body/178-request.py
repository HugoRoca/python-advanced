from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, StrictStr, StrictInt
from typing import Optional, List, Union


class Test(BaseModel):
    listEmpty: List[Union[StrictStr, StrictInt]] = []


class Image(BaseModel):
    url: str


class Product(BaseModel):
    name: str
    brand: str
    photo: Optional[Image] = {}


class ModelPerson(BaseModel):
    name: str
    last_name: str
    age: Optional[int]


class UserModel(BaseModel):
    username: str = Field(
        default=...,
        title="User name",
        description="The username of user",
        max_length=20,
        min_length=5
    )
    email: str


app = FastAPI()


@app.post("/product/add")
async def add_product(product: Product = Body(...)):
    return product.dict()


@app.post("/person/get")
async def add_person(test: Test = Body(...)):
    return test.dict()


@app.post("/person/add")
async def add_person(person: ModelPerson):
    return person.dict()


@app.post("/person/add_2")
async def add_person(person: ModelPerson, user: UserModel, param1: int = Body(...)):
    return {"person": person.dict(), "user": user.dict()}


@app.put("/person/edit/{id}")
async def edit_person(person: ModelPerson, id: int = Path(...)):
    return {"id": id, "person": person.dict()}


@app.put("/person/edit_2/{id}")
async def edit_2_person(person: ModelPerson, id: int = Path(...), without_id: bool = Query(False)):
    return {"id": id, "person": person.dict(), "without_id": without_id}