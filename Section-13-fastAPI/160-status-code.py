from fastapi import FastAPI, Response, status

app = FastAPI()

listUser = []


@app.get(path="/", status_code=status.HTTP_200_OK)
async def ger_user():
    if listUser:
        return listUser

    return Response(content="Not exists users!", status_code=status.HTTP_404_NOT_FOUND)