from fastapi import FastAPI
from pydantic import BaseModel


class ModelPerson(BaseModel):
    name: str
    last_name: str
    age: int


app = FastAPI()


@app.post("/person/add")
async def add_person(person: ModelPerson):
    return person.dict()