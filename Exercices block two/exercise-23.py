"""
Calcular cuantos segundos tiene un hora dada.
"""

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

resultado = (hora * 3600) + (minutos * 60) + segundos

print("El resultado es: ", resultado)