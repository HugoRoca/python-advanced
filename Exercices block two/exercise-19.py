# Dado un número natural, calcular su factorial.

number = int(input("Ingrese número: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("El factorial es: ", factorial)