# Dada una lista de N números x, indicar si la misma viene ordenada ascendente

number = int(input("Ingrese N: "))
lista = []

for i in range(number):
    x = int(input("Ingrese número: "))
    lista.append(x)

aux = False
for i in range(0, number - 1):
    if lista[i] > lista[i + 1]:
        aux = True
        break

if aux:
    print("No esta ordenada ascendente.")
else:
    print("Ya esta ordenada ascendente.")