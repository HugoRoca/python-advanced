matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(matrix)

for i in matrix:
    print(*i)

# length rows
tamanio = len(matrix)
columns = len(matrix[0])

print("Quantity rows:", tamanio)
print("Quantity columns:", columns)

print("row 1", matrix[0])
print("row 2 - column 2:", matrix[1][1])