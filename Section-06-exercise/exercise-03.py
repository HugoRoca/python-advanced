# Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.

x = int(input("Ingrese un número natural: "))

pares = 0
impares = 0

while x > 0:
    digit = x % 2

    if digit % 2 == 0:
        pares += 1
    else:
        impares += 1

    x = x // 10

print("Cantidad de número pares: ", pares)
print("Cantidad de números impares: ", impares)

# python methods
x = input("Ingrese un número natural: ")

pares = 0
impares = 0

for digit in x:
    if int(digit) % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de número pares: ", pares)
print("Cantidad de números impares: ", impares)