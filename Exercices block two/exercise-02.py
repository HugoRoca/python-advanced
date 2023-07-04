# Dado un número natural x, contar la cantidad de dígitos que posee

x = int(input("Ingresar un número natural: "))
count = 0

# logic
if x >= 0 or x < 10:
    print("Cantidad de dígitos: 1")
else:
    while x > 0:
        count += 1
        x = x // 10

    print("Cantidad de dígitos: ", count)

# python functions
x = input("Ingresar un número natural: ")

if x.isnumeric():
    print("Cantidad de dígitos: ", len(x))
