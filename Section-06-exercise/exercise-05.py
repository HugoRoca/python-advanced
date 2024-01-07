# Dado un número natural x, determinar si es capicúa
x = input("Ingresar número natural: ")
number = int(x)

aux = number
capicua = 0

print("Method 1")
while number > 0:
    last = number % 10
    capicua = (capicua * 10) + last
    number = number // 10

if aux == capicua:
    print("Es capicúa!")
else:
    print("NO es capicúa!")

# Method 2
print("Method 2")
print("Dado vuelta", x[::-1])

if x == x[::-1]:
    print("Es capicúa!")
else:
    print("NO es capicúa!")

# Method 3
print("Method 3")
lista = []

for digit in range(len(x)-1, -1, -1):
    lista.append(x[digit])

print(lista)
capicua = "".join(lista)

if x == capicua:
    print("Es capicúa!")
else:
    print("NO es capicúa!")