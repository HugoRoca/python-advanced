# Escribir un programa que pida al usuario una palabra y luego muestre por
# pantalla una a una las letras de la palabra introducida empezando por la última

word = input("Ingrese palabra: ")

position = len(word)
while position > 0:
    print(word[position-1])
    position -= 1

for rep in range(len(word), -1, -1):
    print(word[rep - 1])
