# Dadas dos listas de números A y B, indicar si el mayor de la lista A se encuentra en la lista B

number = int(input("Ingrese N de A: "))
lista_a = []

for i in range(number):
    x = int(input("Ingrese número: "))
    lista_a.append(x)

number = int(input("Ingrese N de B: "))
lista_b = []

for i in range(number):
    x = int(input("Ingrese número: "))
    lista_b.append(x)

# Option 1
mayor_a = -9999999
aux = False

for i in lista_a:
    if i > mayor_a:
        mayor_a = i

for i in lista_b:
    if i > mayor_a:
        aux = True
        break

if aux:
    print("El número mayor de A si esta en B: ", mayor_a)
else:
    print("El número mayor de A NO esta en B: ", mayor_a)

# Option 2
mayor_a = max(lista_a)
if mayor_a in lista_b:
    print("El número mayor de A si esta en B: ", mayor_a)
else:
    print("El número mayor de A NO esta en B: ", mayor_a)
