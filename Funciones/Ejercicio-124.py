""" 
Definir por asignacion una lista de enteros en el bloque principal del programa. 
Elaborar tres funciones, la primera recibe la listay retorna la suma de todos sus
elementos. la segunda recibe la lista y retorna el mayor valor y la ultima
recibe la lista y retorna el menor 
"""


def sumarizarlista(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma


def retornarMayor(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if (lista[i] > mayor):
            mayor = lista[i]
    return mayor


def retornarMenor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if (lista[i] < menor):
            menor = lista[i]
    return menor


listavalores = [10, 20, 30, 40, 50]
print("Lista completa ")
print(listavalores)
print("La suma de sus elementos es ", sumarizarlista(listavalores))
print("El elemento mayor es  ", retornarMayor(listavalores))
print("El elemento menor es  ", retornarMenor(listavalores))
