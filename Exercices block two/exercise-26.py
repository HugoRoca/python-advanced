"""
Dada una lista de palabras, contar cuantas
vocales y consonantes tiene cada palabra
"""

texto = input("Ingrese un texto: ")
palabras = texto.split()

for palabra in palabras:
    cv = 0
    cc = 0

    for letra in palabra:
        if letra.lower() in ["a", "e", "i", "o", "u"]:
            cv += 1
        else:
            cc += 1

    print(f"{palabra} tiene {cv} vocales y {cc} consonantes.")
