# Escribir un programa que pregunte al usuario por el númerod de horas y el coste por hora.
# Después  debe mostrar la paga que le corresponde.

quantity_hours = int(input("Ingrese la cantidad de horas: "))
price_hour = int(input("Ingrese el costo por hora: "))

print(f"El pago total es {quantity_hours * price_hour}")
