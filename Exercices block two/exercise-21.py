"""
A una fiesta asistieron personas de diferentes edades y sexos. Construir un algoritmo dadas las edades y generos de las
personas:
Calcular:
    - Cantidad de personas que asistieron a la fiesta.
    - Cantidad de hombres y mujeres
    - Promedio de edades por generos.
    - La edad de la persona más joven que asistió
"""
cp = 0
ch = 0
cm = 0
lista_h = []
lista_m = []
mas_joven = 150
edad = 1

while(edad > 0):
    edad = int(input("Ingrese edad: "))

    if edad > 0:
        cp += 1

        if edad < mas_joven:
            mas_joven = edad

        genero = ""

        while (genero not in [ "h", "m"]):
            genero = input("Cuál es tu género? H/M: ")

            if genero.lower() == "h":
                ch += 1
                lista_h.append(edad)
            elif genero.lower() == "m":
                cm += 1
                lista_m.append(edad)
            else:
                print("Ingresa tu genero correctamente")

print("Cantidad de personas: ", cp)
print("Cantidad de hombre: ", ch)
print("Cantidad de mujeres: ", cm)
print("Personas más joven: ", mas_joven)
print("Promedio de edad en hombres: ", sum(lista_h) / len(lista_h))
print("Promedio de edad en mujeres: ", sum(lista_m) / len(lista_m))
