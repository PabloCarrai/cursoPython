""" 
Desarrollar un programa que cargue
una lista de 10 enteros. Cargar los 
valores aleatorios con numeros enteros
comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos y volver a mostrarlos
"""

import random


def cargar():
    lista = []
    for i in range(10):
        valor = random.randint(0, 1000)
        lista.append(valor)
    return lista


def mezclar(lista):
    random.shuffle(lista)


def mostrar(lista):
    print(f"Lista con elementos {lista}")


lista = cargar()
mostrar(lista)
mezclar(lista)
mostrar(lista)
