import sqlite3

db = sqlite3.connect("data-py.db")

cursor = db.cursor()

cursor.execute("DELETE FROM Person WHERE id = 1")

cursor.close()

db.commit()