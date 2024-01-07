import sqlite3

db = sqlite3.connect("data-py.db")

cursor = db.cursor()

cursor.execute("UPDATE Person SET name = 'Hugo', lastName = 'Roca' WHERE id = 4")

cursor.close()

db.commit()
