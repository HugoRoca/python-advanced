"""
Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número.
"""


def count_digits(_num: int, _digit: int):
    if not isinstance(_num, int) or not isinstance(_digit, int):
        print("Ingrese un número y un dígito que sean entero!")
        return

    _num = str(_num)
    _digit = str(_digit)

    repeat = _num.count(_digit)

    print(f"El dígito {_digit} se repite {repeat} veces en el número {_num}")


num = int(input("Ingrese númer: "))
digit = int(input("Ingrese dígito: "))

count_digits(num, digit)