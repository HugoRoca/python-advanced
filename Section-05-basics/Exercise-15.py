# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparace la letra en la frase

phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")

count = 0
length = len(phrase)
i = 0

while i < length:
    if phrase[i] == letter:
        count += 1
    i += 1

count = 0

for rep in phrase:
    if rep == letter:
        count += 1

print("La letra ingresada aparace", count, "veces")
