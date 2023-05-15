# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
# todos los números impares desde 1 hasta ese número separados por comas.

number = int(input("Ingrese número: "))

if number > 0:
    for rep in range(number):
        if rep % 2 != 0:
            print(rep, end=", ")

    aux = 0
    while aux <= number:
        if aux % 2 != 0:
            print(aux)
        aux += 1
else:
    print("Ingrese un número mayor que cero.")

