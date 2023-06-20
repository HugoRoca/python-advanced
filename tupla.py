tupla = (1,2,3,4,5)

print(tupla)
print("first element:", tupla[0])

# modified value
# tupla[0] = 999
print("tupla normal:", tupla)
aux_list = list(tupla)
aux_list[0] = 1111

tupla = tuple(aux_list)
print("tuple modified: ", tupla)

# delete
tamanio = len(tupla)
print("Tamanio tupla:", tamanio)

# concat
newTupla = (1,2,3) + (4,5,6)
print(newTupla)