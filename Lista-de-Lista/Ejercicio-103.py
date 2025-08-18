"""

Desarrollar un programa que cree una lista
de 50 elementos. El primer elemento
es una lista con un elemento entero, el segundo
elemento es una lista de dos elementos.
La lista deberia de tener una estuctura y asignale
esos valores a medida que se crean elementos.

lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4],
         [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]

"""
lista = []
aux = 1

#   Armo las sublistas
for i in range(1, 50):
    lista.append([])
#   Agrego los elementos a cada lista
for i in range(len(lista)):
    lista[i].append(list(range(1, aux)))
    aux = aux+1
#   Imprimo la lista
for x in range(len(lista)):
    print(lista[x])
