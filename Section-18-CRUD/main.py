from fastapi import FastAPI, Body, status, Query
from models import BaseProduct
from db import Cart
from typing import Optional

app = FastAPI()
cart = Cart()


@app.post("/cart", status_code=status.HTTP_201_CREATED)
async def index(product: BaseProduct):
    cart.add_to_cart(product)

    return {"msg": "Created product"}


@app.get("/cart", status_code=status.HTTP_200_OK)
async def get_cart(id: Optional[int] = Query(default=None)):
    if id:
        return cart.get_cart(id=id)

    return cart.get_cart()
