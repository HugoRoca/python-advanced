import sqlite3
from function_db import FunctionDB

db = sqlite3.connect("data-py.db")
cursor = db.cursor()

print("--- System CRUD ---")

functions = FunctionDB("data-py.db")
functions.connect()

option = ""

while True:
    if option == "":
        print("""
        [1] Crear un registro
        [2] Obtener un registro
        [3] Obtener todos los registros
        [4] Actualizar un registro
        [5] Borrar un registro
        [6] Salir
        """)

        option = input("Ingresar una opción: ")

    if option == "1":
        if not functions.option_one():
            option = "1"
            continue
    elif option == "2":
        if not functions.option_two():
            option = 2
            continue
    elif option == "3":
        functions.option_three()
    elif option == "4":
        if not functions.option_four():
            option = "4"
            continue
    elif option == "5":
        functions.option_five()
    elif option == "6":
        break
    else:
        print("!!!! INGRESE UNA OPCION VALIDA!!!!")

    option = ""


functions.close_connection()

