# Escribir un programa que pida al usuario una palabra y la muestra por pantalla 10 veces

word = input("Ingrese palabra para repetir: ")

rep = 0
while rep < 10:
    print(word)
    rep += 1

for rep in range(10):
    print(word)