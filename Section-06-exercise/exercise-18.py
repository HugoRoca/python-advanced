# Dados 3 números naturales, A, B y C, mostrar los múltiplos de A, menores que B que son divisores de C

number_a = int(input("Ingrese número A: "))
number_b = int(input("Ingrese número B: "))
number_c = int(input("Ingrese número C: "))

for i in range(1, number_a + 1):
    result = number_a % i
    if result == 0 and result < number_b and number_c % i != 0:
        print("Número que cumple las condiciones: ", i)
