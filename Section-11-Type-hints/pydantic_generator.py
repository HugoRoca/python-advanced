from typing import Iterable
from pydantic import BaseModel


class Generator(BaseModel):
    generator: Iterable[int]


def generate_number():
    i = 0

    while True:
        yield i
        i += 1


g1 = Generator(generator=generate_number())

for num in g1.generator:
    print(num)

    if num == 50:
        break