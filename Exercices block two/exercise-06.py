# Dado un número entero x, mostrar sus N primeras potencias

x = int(input("Ingrese un número entero: "))
n = int(input("Ingrese N: "))

count = 0

while count <= n:
    print(f"{x} ** {count} = {x ** count}")
    count += 1

count = 0
for c in range(n+1):
    print(f"{x} ** {count} = {x ** count}")
    count += 1
