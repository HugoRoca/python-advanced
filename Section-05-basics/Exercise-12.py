# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo

number = int(input("Ingrese número: "))
tri = "*"

for rep in range(number):
    print(rep * tri)

aux = 0
while aux <= number:
    print(aux * tri)
    aux += 1