dictionary = {"rojo": "red", "azul": "blue", "amarillo": "yellow"}

# show
print("Rojo en inglés es:", dictionary["rojo"])
print("Azul en inglés es:", dictionary["azul"])
print("Amarillo en inglés es:", dictionary["amarillo"])

# add
dictionary["verde"] = "grin"
print(dictionary)

dictionary.update({"blanco": "white"})
print(dictionary)

# update
dictionary["verde"] = "green"
# dictionary.update({"verde": "green"})
print(dictionary)

# get
red = dictionary.get("rojo")
print(red)

celeste = dictionary.get("celeste")
print("Color no existe:", celeste)

# del
del dictionary["rojo"]
dictionary.pop("azul")

print(dictionary)

# items
print("items:", dictionary.items())

# keys
print("keys:", dictionary.keys())

# values
print("values:", dictionary.values())

print("Key and value")
for key, value in dictionary.items():
    print(key, value)

print("Keys")
for key in dictionary.keys():
    print(key)