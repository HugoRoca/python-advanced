# Dado un número natural x, mostrar su último dígito.

# sol 1
number = input("Ingrese número natural: ")
number_int = int(number)

if number_int < 0:
    print("Debe ingresar un número entero!")
else:
    # sol 1
    for item in range(len(number)):
        if (item + 1) == len(number):
            print("El último dígito es: ", number[item])

    # sol 2
    print("El último dígito es: ", number[-1])
