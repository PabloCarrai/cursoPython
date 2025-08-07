""" 
Una planta que fabrica perfiles de hierro
posee un lote de n piezas. 
Confeccionar un programa que pida
ingresar por teclado la cantidad de
piezas a procesar y luego ingrese la 
longitud de cada perfil. Sabiendo que 
la pieza cuya longitud este comprendida
en el rango de 1.20 y 1.30 son aptas. 
Imprimir por pantalla la cantidad de 
piezas aptas que hay en el lote
"""

x = 1
suma = 0
cpiezas = int(input("Ingrese cantidad de pieza a cargar "))
while (x <= cpiezas):
    x = x+1
    largo = float(input("Ingrese el largo de la pieza  "))
    if ((largo >= 1.20) and (largo <= 1.30)):
        suma = suma+1
print("Cantidad de piezas validas")
print(suma)
