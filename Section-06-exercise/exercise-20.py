# Dados 3 dígitos, generar y mostrar el mayor número natural que puede escribirse con ellos.

a = int(input("Ingrese A: "))
b = int(input("Ingrese B: "))
c = int(input("Ingrese C: "))

number = None

if a >= b and a >= c:
    number = a * 100 + (b * 10) + c
elif b >= a and b >= c:
    number = b * 100 + (a * 10) + c
elif c >= a and c >= b:
    number = c * 100 + (a * 10) + b
elif a >= c >= b:
    number = a * 100 + (c * 10) + b
elif b >= c >= a:
    number = b * 100 + (c * 10) + a
elif c >= b >= a:
    number = c * 100 + (b * 10) + a

print("El número mayor es: ", number)