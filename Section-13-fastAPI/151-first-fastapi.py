from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def index():
    return { "message": "Hello world" }


@app.post("/endpoint")
async def request_inf(request: Request):
    data = await request.json()
    return data

"""
For exec: uvicorn 151-first-fastapi:app --reload
"""