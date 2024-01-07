# Escribir un programa que pregunte el nombre del usuario en la consola
# y un número entero e imprima por pantalla en líneas distintas el nombre
# del usuario tantas veces como el número introducido.

name = input("Ingrese nombre: ")
repeat = int(input("Ingrese número: "))

# concat
print((name + "\n") * repeat)

# while
print("Cycle while")
repeat_aux = repeat
while repeat_aux > 0:
    print(name)
    repeat_aux -= 1

# for
print("Cycle for")
for rep in range(repeat):
    print(name)


