""" 
Confeccionar una funcion que carguepor teclado una lista
de 5 enteros y la retorne. Una segunda funcion debe recibir
una lista y mostrar todos los valores mayores a 10. 
Desde el bloque principal del programa llamar a ambas funciones
"""


def generarLista():
    lista = []
    for x in range(5):
        valor = int(input("Valor?  "))
        lista.append(valor)
    return lista


def listaMayorDiez(lista):
    for i in range(len(lista)):
        if lista[i] > 10:
            print("Mayores a 10")
            print(lista[i])


lista = generarLista()
listaMayorDiez(lista)
