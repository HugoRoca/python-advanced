"""
Solicitar al usuario que ingrese un email. imprimir un mensaje si la dirección es válida o no,
valiéndose de una función para decidirlo. una dirección se considera válida si contiene el @
"""

email = input("Ingrese email: ")

def validar_email(email):
    if "@" in email:
        print("Email es válido!")
    else:
        print("Email NO válido!")


print(validar_email(email))