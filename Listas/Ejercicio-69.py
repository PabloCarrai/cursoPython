""" 
Definir una lista por asignacion con 5 enteros. 
Mostrar por pantalla solo los elementos con 
valor igual o superior a 7
"""
aux = 0
#   Defino lista por asignacion
valores = [7, 8, 9, 16, 4]
#   Recorro la lista usando el aux
while aux < len(valores):
    #   Si el valor en la posicion aux es >= 7
    if valores[aux] >= 7:
        #   Imprimo el valor
        print("Valor >= 7 ")
        print(valores[aux])
    #   Aumento el auxiliar porque sino el while no finaliza nunca
    aux = aux+1
