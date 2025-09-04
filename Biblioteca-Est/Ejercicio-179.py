""" 
Confeccionar un programa con las siguientes funciones
1)  Generar una lista de 4 elementos enteros aleatorios comprendidos entre 1 y 3. 
Agregar un quinto elemento con un 1.
2)  Controlar que el primer elemento de la lista sea un 1, en el caso de que haya un 2 o un 3 mezclar la lista
y volver a controlar hasta que haya un 1. 
3)  Imprimir la lista
"""

import random


def crearLista():
    lista = []
    for i in range(4):
        valor = random.randint(1, 3)
        lista.append(valor)
    lista.append(1)
    return lista


def verificarPrimerElemento(lista):
    while lista[0] != 1:
        random.shuffle(lista)
    return lista


def imprimir(lista):
    print(f"La lista {lista}")


lista = crearLista()
imprimir(lista)
verificarPrimerElemento(lista)
imprimir(lista)
