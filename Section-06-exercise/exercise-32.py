"""
Solicitar números al usuario hasta que ingrese cero. Por cada uno, mostrar la suma de sis digitos.
"""
import re


def sum_digits(num):
    num = re.sub("[.-]", "", num)

    if not num.isnumeric() or num == "0":
        print("Debe ingresar un número mayor que cero!")
        return 0

    sumador = 0

    for n in num:
        sumador += int(n)

    print(f"La suma de sus dígitos es: {sumador}")


num = -1

while num != "0":
    num = input("Ingrese número: ")

    sum_digits(num)

# num = -1
#
# while num != "0":
#     num = input("Ingrese número: ")
#     num = re.sub("[.-]", "", num)
#
#     if not num.isnumeric() or num == "0":
#         print("Debe ingresar un número mayor que cero!")
#         continue
#
#     sumador = 0
#
#     for n in num:
#         sumador += int(n)
#
#     print(f"La suma de sus dígitos es: {sumador}")

