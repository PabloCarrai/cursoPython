"""  
Confeccionar un programa que contenga
las siguientes funciones:
1)  Carga de una lista y retorno al bloque principal
2)  Fijar en cero todos los elementos de la lista que 
tengan un valor menor a 10
3)  Imprimir la lista
"""


def cargar():
    lista = []
    continua = "s"
    while continua == "s":
        valor = int(input("Valor?  "))
        lista.append(valor)
        continua = input("Quiere ingresar otro valor? s/n? ")
    return lista


def fijar_cero(lista):
    for i in range(len(lista)):
        if lista[i] < 10:
            lista[i] = 0


def imprimir_elementos(lista):
    print(f"Elementos en la lista {lista}")
    for i in range(len(lista)):
        print(f"Elemento {lista[i]}")


lista = cargar()
imprimir_elementos(lista)
fijar_cero(lista)
imprimir_elementos(lista)
