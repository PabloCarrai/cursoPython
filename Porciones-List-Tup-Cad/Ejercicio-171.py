""" 
Realizar un programa que contenga las siguientes funciones:
1)  Carga de una lista de 10 enteros. 
2)  Recibir una lista y retornar otra con la primer mitad(se sabe que siempre
llega una lista con una cantidad par de elementos)
3)  Imprimir una lista
"""


def carga_datos():
    enteros = []
    for elemento in range(10):
        valor = int(input("Valor? "))
        enteros.append(valor)
    return enteros


def primer_mitad(lista):
    mitad = lista[:5]
    return mitad


def imprimir_lista(lista):
    print("Lista ")
    print(lista)


lista_original = carga_datos()
print("Lista Original  ")
imprimir_lista(lista_original)
mitad_original = primer_mitad(lista_original)
print("Primer Mitad de Lista ")
imprimir_lista(mitad_original)
