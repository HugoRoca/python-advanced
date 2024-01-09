from fastapi import FastAPI, Response, status
from typing import Optional
from copy import copy

app = FastAPI()

fake_db = [
    {"item": "First"},
    {"item": "second"},
    {"item": "third"}
]


@app.get("/items/{index}")
async def query_params(index: int = 0, mayus: Optional[bool] = False, minus: Optional[bool] = False):
    if mayus and minus:
        return Response(content="Ambos parametros no pueden estar como verdadero al mismo tiempo", status_code=status.HTTP_400_BAD_REQUEST)

    if mayus:
        item_copy = copy(fake_db[index])
        item_copy["item"] = item_copy["item"].upper()
        return item_copy
    elif minus:
        item_copy = copy(fake_db[index])
        item_copy["item"] = item_copy["item"].lower()
        return item_copy


    return fake_db[index]
