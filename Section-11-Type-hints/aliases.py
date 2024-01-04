from typing import List, Dict, Union


class Person:
    pass


Personas = List[Person]


def show_person(lista: Personas) -> None:
    for persona in lista:
        print(persona)


# --------------------

JSONLogin = Dict[str, Union[str, int]]
login_example: JSONLogin = {
    "username": "hroca",
    "pass": 123
}