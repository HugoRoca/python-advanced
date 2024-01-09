from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"item": "First"},
    {"item": "second"},
    {"item": "third"}
]


@app.get("/items/")
async def query_params(index: int = 0, cant: int = 0):
    return fake_db[index: index + cant]