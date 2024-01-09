from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

fake_db = [
    {"item": "First"},
    {"item": "second"},
    {"item": "third"}
]


@app.get("/items")
async def query_params(q: Optional[List[str]] = Query(
    default=["first", "second"],
    alias="an alias",
    description="a description",
    deprecated=True
)):
    return {"message": q}
