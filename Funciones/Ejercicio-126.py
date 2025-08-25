""" 
Crear una lista de enteros por asignacion. 
Definir una funcion que reciba una lista de 
enteros y un segundo parametro tipo entero. 
Dentro de la funcion mostrar cada elemento de 
la lista multiplicado por el valor entero enviado

lista = [3, 7, 8, 10, 2]
def multiplicar(lista, entero)
"""


def multiplicar(lista, entero):
    lista_aux = []
    for i in range(len(lista)):
        lista_aux.append(lista[i]*entero)
    return lista_aux


lista = [3, 7, 8, 10, 2]
aux = multiplicar(lista, 3)

print("Lista Original")
print(lista)
print("Lista modificada multiplicada por 3")
print(aux)
