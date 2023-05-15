# Escribir un programa que pregunte el nombre de usuario en la consola y después de que el
# usuario introduzca muestre por pantalla <NOMBRE> tienen <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el usuario.

name = input("Ingrese nombre: ")
name = name.upper()
length = len(name)

print(f"El nombre: {name} tiene {length} letras")
