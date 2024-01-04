# una clase concrerta, es que hereda de una clase obstracta, es un subtipo de esa clase abtracta

from typing import Tuple


# supertype
class Animal:
    ...


# subtype
class Dog(Animal):
    ...


class Canguro():
    pass


def animal_corre(animal: Animal) -> None:
    print("")