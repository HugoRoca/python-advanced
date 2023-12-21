"""
Crear una funcieon que reciba por parámetro una lista con número y pr paso por referencia multiplique todos los
valores por 2.
"""


def mult_values(list):
    for posicion, elemento in enumerate(list):
        list[posicion] *= 2


lista = [1, 2, 3, 4, 5]
print("Antes", lista)
mult_values(lista)
print("Despues", lista)