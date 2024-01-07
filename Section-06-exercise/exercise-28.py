"""
dada una matriz de caracteres, ordenar cada columna alfabeticamente
"""
n = int(input("Ingresar N: "))
m = int(input("Ingresar M: "))

# Cargar matriz
matriz = []

for fila in range(n):
    matriz.append([])

    for columna in range(m):
        numero = input(f"Ingrese character en la fila {fila + 1} columna {columna + 1}: ")
        matriz[fila].append(numero)

# Mostrar matriz
for i in matriz:
    print(*i)

# Algoritmo
for col in range(n):
    fila_aux = []

    for row in matriz:
        fila_aux.append(row[col])

    fila_aux = sorted(fila_aux)
    f = 0

    for row in matriz:
        row[col] = fila_aux[f]
        f += 1

# Mostrar matriz
print("-- matriz nueva")
for i in matriz:
    print(*i)