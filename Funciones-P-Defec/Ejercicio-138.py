""" 
Cargar una lista de 10 enteros, luego mostrarlos en pantalla
a cada elemento separado de una coma en la misma linea. 
"""


def cargarEnteros():
    lista = []
    for i in range(10):
        valor = int(input("Valor?  "))
        lista.append(valor)
    return lista


def mostrarLista(lista):
    for i in range(len(lista)):
        print(lista[i], end=",")


lista = cargarEnteros()
mostrarLista(lista)
