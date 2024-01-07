from fastapi import FastAPI

app = FastAPI()

# siempre va tipear de acuerdo al tipo de data con el cual se declara en la parametria
@app.get(path="/test/{params}")
async def test(params: int):
    print(params)