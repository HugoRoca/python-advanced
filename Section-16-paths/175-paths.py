from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()


@app.get("/items/{item}")
async def get_item(item: int = Path(...)):
    return item


@app.get("/itm/{itm}")
async def get_itm(q: Optional[str] = Query(None), itm: int = Path(...)):
    return itm

"""
only for int
gt: greater than => mayor que
ge: greater than or equal => mayor o igual que
lt: less than => menor que
le: less than or equal => menor o igual o que
"""
