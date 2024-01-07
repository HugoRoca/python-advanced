# Escribir un programa que pida al usuario un número entero positivo y muestra por pantalla
# la cuenta atrás desde ese número hasta cero separados por coma

number = int(input("Ingrese número: "))

if number <= 0:
    print("Debe de ingresar un número mayor que cero.")
else:
    for rep in range(number, -1, -1):
        print(rep, end=", ")

    print("----")

    aux = number
    while aux >= 0:
        print(aux, end=", ")
        aux -= 1
