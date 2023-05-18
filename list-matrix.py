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
