"""  
Realizar un programa que permita cargar dos listas 
de 15 valores cada una. Informar con un mensaje
cual de las dos listas tiene un valor acumulado mayor. 
Lista 1 mayor Lista 2 Mayor Listas iguales
"""
acumuladorListaUno = 0
acumuladorListaDos = 0
aux = 1
while (aux <= 15):
    valor = int(input("Valor para Lista 1 "))
    aux = aux+1
    acumuladorListaUno = acumuladorListaUno+valor
aux = 1
while (aux <= 15):
    valor = int(input("Valor para Lista 2 "))
    aux = aux+1
    acumuladorListaDos = acumuladorListaDos+valor
aux = 1
if (acumuladorListaUno == acumuladorListaDos):
    print("Listas Iguales")
else:
    if (acumuladorListaUno > acumuladorListaDos):
        print("Lista 1 Mayor")
    else:
        print("Lista 2 Mayor")
