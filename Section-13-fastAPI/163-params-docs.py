from enum import Enum
from fastapi import FastAPI


class ModelLanguages(str, Enum):
    python = "python"
    java = "java"
    golang = "golang"


app = FastAPI()


@app.get("/lang/{name}")
async def languages(name: ModelLanguages):
    if name == ModelLanguages.python:
        return {"message": "Es un buen lenguage de programación."}
    