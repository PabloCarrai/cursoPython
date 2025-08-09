"""  
Realizar la carga de dos nombres por teclado. 
Mostrar cual de los dos es mayor
alfabeticamente o si son iguales
"""

nombre = input("Ingrese un nombre  ")
nombre1 = input("Ingrese otro nombre  ")
print("El nombre mayor alfabeticamente es ")
if (nombre == nombre1):
    print("Ambos nombres son iguales")
else:
    if (nombre > nombre1):
        print(nombre)
    else:
        print(nombre1)
