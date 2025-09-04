"""  
Confeccionar un programa con las siguentes funciones.
1) Cargar una lista con 5 palabras
2) Intercambiar la primer palabra con la ultima
3) Imprimir la lista
"""


def cargar_lista():
    lista = []
    for i in range(5):
        palabra = input("Palabra?  ")
        lista.append(palabra)
    return lista


def intercambiar_elemento_lista(lista):
    aux = lista[0]
    lista[0] = lista[-1]
    lista[-1] = aux
    return lista


def imprimir_lista(lista):
    print(f"La lista es {lista}")


lista = cargar_lista()
imprimir_lista(lista)
lista1 = intercambiar_elemento_lista(lista)
imprimir_lista(lista1)
