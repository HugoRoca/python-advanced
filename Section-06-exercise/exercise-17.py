# Dado un número natural mostrar el mayor de sus dígitos

aux = -1
inpt = input("Ingrese número: ")
number = int(inpt)

while number > 0:
    if number % 10 > aux:
        aux = number % 10

    number = number // 10

print("El mayor es: ", aux)

print("Option 2")
print("El mayor es: ", max(inpt))
