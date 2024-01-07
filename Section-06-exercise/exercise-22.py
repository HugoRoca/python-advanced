"""
Determinar si un número X es perfecto, un número es perfecto si la suma de sus divisores es el mismo número.
6 es perfecto ya que 1+2+3=6
"""

x = int(input("Ingresar número: "))

sumador = 0

for c in range(1, x):
    if x % c == 0:
        sumador += c

if x == sumador:
    print("Es un número perfecto")
else:
    print("NO es un número perfecto")