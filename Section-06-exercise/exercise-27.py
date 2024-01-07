"""
Dada un matriz NxM elementos, calcular el promedio de cada fila y de cada columna.
Mostrar en pantalla la matriz cargada y los promedios correspondientes.
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

# Promedio
c = 1
for fila in matriz:
    sumador = sum(fila)
    largo = m
    resultado = sumador / largo

    print(f"Promedio de la fila {c} es: ", resultado)
    c += 1

# Promedio col
for col in range(m):
    sumador = 0

    for row in matriz:
        sumador += row[col]

    promedio = sumador / n

    print(f"Promedio de la columna {col + 1}: ", promedio)


# Mostrar matriz
for i in matriz:
    print(*i)