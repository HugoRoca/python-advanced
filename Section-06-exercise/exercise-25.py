"""
Generar los n primeros números de la lista fibonacci.
Además debe contar cuantos números primos existen en la serie
"""
k = int(input("Ingrese N: "))
a = 0
b = 1
c_primos = 0

while a < k:
    cx = 0

    if a != 0:
        for divisor in range(1, a + 1):
            if a % divisor == 0:
                cx += 1

        if cx <= 2:
            c_primos += 1

    print(a)
    a, b = b, a + b

print('Cantidad de primos: ', c_primos)