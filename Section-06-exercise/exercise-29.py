"""
Dada la matriz de NxM elementos, compuesta de 0 y 1, recorrer cada una de las filas y mostrar el
valor decimal equivalente.

Ejemplo:
(1 1 0 0 0)
(0 1 1 0 1)
(0 0 0 1 1)
"""
n = int(input("Ingresar N: "))
m = int(input("Ingresar M: "))

# Cargar matriz
matriz = []

for fila in range(n):
    matriz.append([])

    for columna in range(m):
        numero = int(input(f"Ingrese numero en la fila {fila + 1} columna {columna + 1}: "))
        matriz[fila].append(numero)

c = 1
for fila in matriz:
    concatenacion = ""

    for col in fila:
        concatenacion += str(col)

    binario = int(concatenacion, 2)
    print(f"Fila {c}: {concatenacion} = {binario}")
    c += 1

# Mostrar matriz
for i in matriz:
    print(*i)