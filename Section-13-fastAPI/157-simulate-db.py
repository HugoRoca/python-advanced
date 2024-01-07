from fastapi import FastAPI, Request
from typing import List, Dict, Any

app = FastAPI()

listModel = List[Dict[Any, Any]]
listUser: listModel = []
id = 1


def update_user(new_data, id_user):
    for user in listUser:
        print(id_user, user["id"])
        if id_user == user["id"]:
            user.update(new_data)
            return "Updated user!"

    return "User not exists!"


@app.get("/")
async def return_users():
    return listUser


@app.post("/add")
async def add_user(request: Request):
    global id

    new_user = await request.json()

    if new_user:
        new_user["id"] = id
        id += 1
        listUser.append(new_user)

        return {"message": "Successfully"}


@app.put("/edit/{id_user}")
async def update_user(request: Request, id_user: int):
    new_data = await request.json()

    if new_data:
        return update_user(new_data, id_user)

    return "Empty body"


@app.patch("/edit/{id_user}")
async def update_user_patch(request: Request, id_user: int):
    new_data = await request.json()

    if new_data:
        return update_user(new_data, id_user)

    return "Empty body"


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for user in listUser:
        if user_id == user["id"]:
            listUser.remove(user)
            return {"message": "User was delete!"}

    return {"message": "User not exists!"}