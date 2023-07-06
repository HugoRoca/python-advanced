# Dado una lista de N números naturales x, mostrar el menor de ellos.

number = int(input("Ingrese N: "))
aux = 9999999999
lista = []

for i in range(number):
    x = int(input("Ingrese número: "))
    lista.append(x)

    if x < aux:
        aux = x

print("El menor número es: ", aux)

aux = 9999999999
for i in lista:
    if i < aux:
        aux = i

print("El menor número es: ", aux)
