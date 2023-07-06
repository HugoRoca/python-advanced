# Dados dos números naturales A y B, mostrar sus divisores comúnes

number_a = int(input("Ingrese primer número: "))
number_b = int(input("Ingrese segundo número: "))

if number_a <= 0 or number_b <= 0:
    print("Debe ingresar número mayores que cero.")
else:
    big_number = number_a

    if number_b > number_a:
        big_number = number_b

    count = 1
    while count < big_number:
        if number_a % count == 0 and number_b % count == 0:
            print(count)

        count += 1

print("Option 2: Set and list")
list_a = []
list_b = []

for i in range(1, number_a):
    if number_a % i == 0:
        list_a.append(i)

for i in range(1, number_b):
    if number_b % i == 0:
        list_b.append(i)

intersection = list(set(list_a) & set(list_b))

print("Divisores comúnes: ", intersection)