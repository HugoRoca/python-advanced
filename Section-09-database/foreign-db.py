import sqlite3

db = sqlite3.connect("data-py.db")

cursor = db.cursor()

data = cursor.execute("SELECT * FROM Child")

print(data.fetchall())

cursor.close()