""" 
Confeccionar un programa que contenga
las siguientes funciones. 
1)  Carga de una lista de 5 nombres
2)  Ordenar alfabeticamente la lista
3)  Imprimir la lista de nombres
"""


def cargar_elementos():
    lista = []
    for i in range(5):
        valor = input("Nombre?  ")
        lista.append(valor)
    return lista


def ordenar_lista(lista):
    for k in range(len(lista)):
        for x in range(4-k):
            if (lista[x] > lista[x+1]):
                aux = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = aux


def imprimir_lista(lista):
    print(f"Los elementos de la lista {lista}")
    for e in lista:
        print(e)


lista = cargar_elementos()
imprimir_lista(lista)
print("Ordenados son: ")
ordenar_lista(lista)
imprimir_lista(lista)
