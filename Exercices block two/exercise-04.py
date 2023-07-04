# Dado un número natural x, sumar todos sus dígitos. Mostrar la suma obtenida

# method 1
number = input("Ingrese un número: ")
suma = 0

for digit in number:
    suma += int(digit)

print("La suma de sus dígitos es: ", suma)

# method 2
number_int = int(number)
suma = 0

while number_int > 0:
    digit = number_int % 10
    suma += digit
    number_int = number_int // 10

print("La suma de sus dígitos es: ", suma)

# method 3
lista = []

for digit in number:
    lista.append(int(digit))

print("La suma de sus dígitos es: ", sum(lista))