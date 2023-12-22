import sqlite3
import os
import tabulate


class FunctionDB:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_name)
            print(f"Connected to the database: {self.database_name}")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        else:
            print("No active connection to close.")

    # For clear console
    def clear_console(self):
        _ = os.system('clear')

    # Register record
    def option_one(self):
        name = input("Ingrese nombre: ")
        lastname = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        birthday = input("Ingrese fecha de nacimiento: (DD/MM/YYYY) ")

        if not dni.isnumeric():
            print("DATOS INCORRECTOS, INGRESE LOS DATOS DE NUEVO!")
            return False

        data = (name, lastname, dni, birthday)

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO person (name, lastName, dni, birthday) VALUES (?, ?, ?, ?)", data)

        self.connection.commit()

        return True

    # Get by id person
    def option_two(self):
        id = input("Ingrese el ID: ")

        if not id.isnumeric():
            print("DATOS INCORRECTOS, INGRESE LOS DATOS DE NUEVO!")
            return False

        id = int(id)

        cursor = self.connection.cursor()

        data = cursor.execute(f"SELECT * FROM person WHERE id = {id}")

        print(data.fetchone())

        return True

    # Get all records
    def option_three(self):
        cursor = self.connection.cursor()

        data = cursor.execute(f"SELECT * FROM person")
        rows = data.fetchall()

        for row in rows:
            print(row)

        return True

    # Update record
    def option_four(self):
        id = input("Ingrese el id del cual quiere actualizar: ")
        name = input("Ingrese nombre: ")
        lastname = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        birthday = input("Ingrese fecha de nacimiento: (DD/MM/YYYY) ")

        if not dni.isnumeric() or not id.isnumeric():
            print("DATOS INCORRECTOS, INGRESE LOS DATOS DE NUEVO!")
            return False

        cursor = self.connection.cursor()
        data = (name, lastname, dni, birthday, id)
        cursor.execute("UPDATE person SET name = ?, lastName = ?, birthday = ?, dni = ? WHERE id = ?", data)

        self.connection.commit()

        return True

    # Delete record
    def option_five(self):
        id = input("Ingrese el id del cual quiere eliminar: ")

        cursor = self.connection.cursor()

        cursor.execute(f"DELETE FROM person WHERE id = {id}")

        self.connection.commit()