# Dado un número natural x, mostrar todos sus divisores

x = int(input("Ingrese número: "))

if x <= 0:
    print("Debe ingresar un número mayor que cero.")
else:
    count = 1

    print("Divisores: ", end=" ")
    while count < x:
        if x % count == 0:
            print(count, end=" ")

        count += 1

    for c in range(1, x):
        if x % c == 0:
            print(c, end=" ")
