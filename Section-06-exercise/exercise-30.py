"""
Dada una tabla que contiene los artículos y precios de un negocio y cantidad de stock, simular generar una factura de
a lo sumo 6 articulos, en la cual el usuario solo debe ingresar el artículo y la cantidad (revisar que el artículo
tenga cantidad). El programa debería calcular los subtotales y el total general de la factura.
"""
from tabulate import tabulate

matriz = [
    ["Artículos", "Precios", "Stock"],
    ["Celulares IPhone", 400, 20],
    ["Sillas gamer ergonómica", 200, 200],
    ["Laptop DELL Core i7 11va Gen", 1700, 20],
    ["Mouse gamer HP", 50, 30],
    ["Monitores 4k", 400, 12]
]

print(tabulate(matriz, headers='firstrow'))

n = len(matriz) # cantidad filas
m = len(matriz[0]) ## cantidad columnas
carrito = [
    ["Artículos", "Precios", "Stock", "Subtotal"]
]

while True:
    print(""" --- Selecciona una opción ---
    [1] Seleccionar artículo
    [2] Mostrar artículos en el carrito
    [3] Realizar venta
    [4] Mostrar productos
    [5] Salir
    """)

    opcion = input("Inrese opción: ")

    if opcion.isnumeric():
        if opcion == "1":
            articulo = input("Ingresar nombre del artículo: ")
            cantidad = int(input("Ingresar cantidad: "))

            if cantidad <= 0:
                print("Debe ingresar una cantidad mayor que cero!")
                pass

            for fila in range(1, n):
                if matriz[fila][0].lower() == articulo.lower():
                    if int(matriz[fila][2]) >= cantidad:
                        matriz[fila][2] -= cantidad
                        carrito.append([matriz[fila][0], matriz[fila][1], cantidad, matriz[fila][1] * cantidad])
                    else:
                        print("El stock es menor que la cantidad, no se puede vender.")
        elif opcion == "2":
            print(tabulate(carrito, headers='firstrow'))
        elif opcion == "3":
            if len(carrito) <= 1:
                print("Carrito no tiene producto!")
                pass

            total = 0

            for fila in range(1, len(carrito)):
                total += carrito[fila][3]

            print("El total es: ", total)

        elif opcion == "4":
            print(tabulate(matriz, headers='firstrow'))
        elif opcion == "5":
            break
        else:
            print("Ingrese una opción correcta!")
    else:
        print("Ingresa una opción correcta!")