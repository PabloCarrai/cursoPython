""" 
Realizar un programa que pida cargar
una fecha cualquiera, luego verificar
si dicha fecha corresponde a Navidad
"25 de diciembre"
"""

dia = int(input("Ingrese el dia "))
mes = int(input("Ingrese el mes "))
anio = int(input("Ingrese el año "))
if ((dia == 25) and (mes == 12)):
    print("Estamos en Navidad")
