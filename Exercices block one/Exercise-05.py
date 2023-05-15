# Pedir el precio de un producto y calcular su IGV (18%) y su valor original

price = int(input("Ingrese precio del producto: "))
igv = price * 0.18
price_original = price - igv

print(f"El IGV del producto es: {igv} \n" 
      f"Y su valor original es: {price_original}")
