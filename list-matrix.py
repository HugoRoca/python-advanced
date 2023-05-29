lista = [1, 2, 3, 4, 5, "hi", 2.4, True, False]
length = len(lista)
print(f"Tamanio de la lista {length}")

# Position
print(f"Primer elemento de la lista {lista[1]}")
print(f"El último elementos de la lista es {lista[length - 1]}")

# slicing
print("Slicing, último elemento:", list[-1])
print("Slicing, primer elemento:", lista[9-1])
print("Slicing, ver todo los elementos:", lista[:])
print("Slicing, ver todo los elementos:", lista[0:])
print("Slicing, ver todo los elementos:", lista[0:50])
print("Slicing, ver todo los elementos:", lista[:0])

# dar vuelta a un número
print("Slicing, dada vuelta:", lista[::-1])

# Properties
# Iterar
text = ["Hola", "mi nombre", "es", "Facundo"]

for word in text:
    print(word + " ", end="")

print("-----------------")
for word in range(len(text)):
    print(f"Position {word} - word {text[word]}")

# Ordenar una lista
lista_1 = [2, 4, 1,5,6,8,11,3,44,5,10,0]
print("Lista desordenada", lista_1)

lista_2 = sorted(lista_1, reverse=True)
print("Lista ordenada", lista_2)

# Add items
list_empty = []
print("Lista vacia", list_empty)
list_empty.append(1)
list_empty.append(2)
list_empty.append(3)

print("Lista con datos", list_empty)

# Using insert
list_empty.insert(1, 4)
print("Lista con insert", list_empty)

# Using extend
list_empty.extend([100, 200])
print("Lista con extend", list_empty)

# Delete data
val_pop = list_empty.pop(0)
print("Lista nueva con pop", list_empty)
print("Valor eliminado", val_pop)

# delete with del
del list_empty[0]
print("Eliminado con del", list_empty)

# Modificar
list_empty[-1] = 999
print("Lista modificada", list_empty)

# Buscar
position = list_empty.index(999)
print("Position of 999 is", position)