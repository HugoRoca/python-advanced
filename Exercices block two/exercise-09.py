# Dado un número natural x, contar todos sus divisores

number = int(input("Ingrese número: "))

if number <= 0:
    print("Debe ingresar un número mayor que cero.")
else:
    count = 1
    divisores = 0

    while count < number:
        if number % count == 0:
            divisores += 1

        count += 1

    print("(While) Total de divisores: ", divisores)

    divisores = 0
    for c in range(1, number):
        if number % c == 0:
            divisores += 1

    print("(For) Total de divisores: ", divisores)
