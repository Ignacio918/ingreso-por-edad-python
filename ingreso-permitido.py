    # Paso 1 : Solicitar al usuario que ingrese la edad del cliente

from math import perm


edad = int(input("Por favor, ingresa tu edad: "))

    # Paso 2 : Verificar si la edad ingresada cumple con el requisito para ingresar al boliche

permitido = True if edad >=18 else False # ternario

    # Paso 3: Mostrar al usuario si su cliente puede o no ingresar al boliche

if permitido:
    print("¡Puedes ingresar al boliche!")
else:
    print("Lo sentimos mucho, no se puede ingresar al boliche siendo menor de edad")
