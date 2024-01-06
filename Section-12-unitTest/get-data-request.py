import requests, json

datos = requests.get("https://www.freetogame.com/api/games")

with open("data.txt", "w") as file:
    file.write(json.dumps(datos.json()))