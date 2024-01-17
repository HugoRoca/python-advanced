from fastapi import FastAPI, Body, status, Query, Response, Path
from models import BaseProduct
from db import Cart
from typing import Optional

app = FastAPI()
cart = Cart()


def product_not_exists():
    return Response(content="Product not exists!", status_code=status.HTTP_404_NOT_FOUND)


@app.post("/cart", status_code=status.HTTP_201_CREATED)
async def index(product: BaseProduct):
    cart.add_to_cart(product)

    return {"message": "Created product"}


@app.get("/cart", status_code=status.HTTP_200_OK)
async def get_cart(id: Optional[int] = Query(default=None)):
    if id:
        product = cart.get_cart(id=id)

        if product:
            return product.dict()

        return product_not_exists()

    return cart.get_cart()


@app.put("/cart/edit/{id}", status_code=status.HTTP_200_OK)
async def edit_cart(id: int = Path(...), new_data: BaseProduct = Body(...)):
    product = cart.get_cart(id=id)

    if product:
        cart.edit_cart(old_product=product, new_product=new_data)
        return {"message": "Successfully edited!"}

    return product_not_exists()


@app.delete("/cart/{id}")
async def delete_product(id: int = Path(...)):
    product = cart.get_cart(id=id)

    if product:
        cart.delete_product(product)
        return {"message": "Successfully deleted!"}

    return product_not_exists()
