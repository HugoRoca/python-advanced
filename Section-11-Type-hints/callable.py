from typing import Callable


def func_1(other_func: Callable[[str], str], argumento: str) -> str:
    return other_func(argumento)


def func_2(name: str) -> str:
    return "Hello " + name


print(func_1(func_2, "Hugo"))
