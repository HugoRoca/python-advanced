from typing import Optional


def func(name: str, lastname: Optional[str] = 'Default') -> str:
    return f"Hello {name} {lastname}"


print(func("Hugo"))
print(func("Hugo", "Roca"))