# Dado una lista ordenada de N números x, indicar si hay elementos repetidos

number = int(input("Ingrese N: "))
lista = []

for i in range(number):
    x = int(input("Ingrese número: "))
    lista.append(x)

print(lista)
"""
# sorting
for i in range(0, number - 1):
    for j in range(i, number):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
"""
lista.sort()
print(lista)

aux = False
for i in range(0, number - 1):
    for j in range(i + 1, number):
        if lista[i] == lista[j]:
            aux = True
            break

message = "Existen repetidos"
if not aux:
    message = "No existen repetidos!"

print(message)