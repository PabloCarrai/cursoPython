""" 
Cargar una oracion por teclado. Mostrar luego 
cuantos espacios en blanco se ingresaron. Tener
en cuenta que un espacio en blanco es igual a " "
en cambio una cadena vacia  es ""
"""

contadorEspacioBlanco = 0
oracion = input("Ingrese una oracion    ")
for x in range(len(oracion)):
    if oracion[x] == " ":
        contadorEspacioBlanco = contadorEspacioBlanco+1
print("Cantidad de espacios en blancos ")
print(contadorEspacioBlanco)
