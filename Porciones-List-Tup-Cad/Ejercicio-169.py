""" 
Confeccionar una funcion que le enviemos
un numero de mes como parametro y nos retorne
una tupla con todos los nombres de meses que faltan
hasta fin de año(utilizar el concepto de porciones)
"""

mes = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
       "agosto", "septiembre", "octubre", "noviembre", "diciembre")


def mes_faltantes(numero):
    print("Meses Faltantes ")
    return mes[numero:]


numero = int(input("Ingrese numero de mes  "))
meses = mes_faltantes(numero)
print(meses)
