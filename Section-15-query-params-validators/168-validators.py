from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()


# "max_length" solo usa para string
# "min_length"
# "regex" => ^pepe$ => debe empezar con la palabra pepe
#
@app.get("/validator")
async def validator(q: Optional[str] = Query(None, min_length=5, max_length=50, regex="^pepe$")):
    return {"q": q}


@app.get("/list")
async def value_list(q: Optional[List[str]] = Query(["first", "second"])):
    return {"q": q}


@app.get("/list_python")
async def list_python(q: list = Query(None)):
    return {1}