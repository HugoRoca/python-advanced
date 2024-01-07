"""
Generar los primeros h números primos (un número es primo si solo es divisible por si mismo y por la unidad)
"""

h = int(input("Ingresar H: "))

for numero in range(1, h + 1):
    c = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            c += 1

    if c <= 2:
        print("Numero primo: ", numero)