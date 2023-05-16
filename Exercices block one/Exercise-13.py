# Esriir un programa que muestre por antalla la tabla de multiplicar de 1 al 10

number = int(input("Ingrese número: "))

for rep in range(10):
    print(f"{rep} x 10 = {rep * number}")
    