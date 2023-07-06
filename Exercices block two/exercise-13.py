# Dada una lista de N números enteros x, calcular su promedio. Mostrar el resultado

number = int(input("Ingrese N: "))
aux = 0

for i in range(number):
    x = int(input("Ingrese número: "))
    aux += x

print("El promedio es: ", aux / number)