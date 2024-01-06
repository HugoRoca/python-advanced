import time
import requests


def sumar(n1: int, n2: int) -> int:
    if isinstance(n1, int) and isinstance(n2, int):
        return n1 + n2
    else:
        raise TypeError(n1, n2, "Error: los números no son enteros")


def magic() -> str:
    time.sleep(5)
    return "magic"


def exec_magic():
    return magic()


def get_games():
    response = requests.get("https://www.freetogame.com/api/games")

    if response.ok:
        return response


class Calc:
    def suma(self, n1: int, n2: int) -> int:
        return n1 + n2