# Ingresar dos números y mostrar el menos de ellos.

number_1 = int(input("Ingrese el primer número: "))
number_2 = int(input("Ingrese el segundo número: "))

if number_1 == number_2:
    print("Los números son iguales.")
elif number_1 > number_2:
    print(f"El número {number_1} es mayor")
else:
    print(f"El número {number_2} es mayor.")
