import sqlite3

# Si no existe la base de datos, sqlite lo crea
db = sqlite3.connect("data-py.db")

cursor = db.cursor()

data = cursor.execute("SELECT * FROM Person")

# Obtiene el primer registro
# print(data.fetchone())

# Obtiene todos los registro
print(data.fetchall())

cursor.close()