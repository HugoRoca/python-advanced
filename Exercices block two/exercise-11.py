# Dado una lista de N números naturales x, mostrar el mayor de ellos

number = int(input("Ingrese N: "))
aux = -1

for i in range(number):
    x = int(input("Ingrese número: "))

    if x > aux:
        aux = x

print("El mayor número es: ", aux)
print("Option 2")

lista = []

for i in range(number):
    x = int(input("Ingrese número: "))
    lista.append(x)

aux = -1
for i in lista:
    if i > aux:
        aux = i

print("El mayor número es: ", aux)