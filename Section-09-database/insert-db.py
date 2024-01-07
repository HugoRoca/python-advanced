import sqlite3

db = sqlite3.connect("data-py.db")

cursor = db.cursor()

record = [
    ('Maria', 'Bastolo', '91928374', '20/12/1994'),
    ('Rosa', 'la rosa', '78326522', '22/11/1992'),
    ('Candy', 'Roca', '27918273', '10/04/1994')
]

# Execute only is for a record
cursor.executemany("INSERT INTO Person (name, lastname, dni, birthday) VALUES (?, ?, ?, ?)", record)

db.commit()