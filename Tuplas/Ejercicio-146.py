""" 
Confeccionar un programa con las siguientes funciones. 
1) Cargar una lista de 5 enteros. 
2) Retornar el mayor y menor valor de la lista
mediante una tupla. Desempaquetar la tupla
en el bloque principal y mostrar el mayor y menor
"""


def cargarEnteros():
    lista = []
    for i in range(5):
        valor = int(input(f"Valor?  {i}: "))
        lista.append(valor)
    return lista


def retornarMayorMenor(lista):
    menor = lista[0]
    mayor = lista[0]
    for i in range(len(lista)):
        if (menor > lista[i]):
            menor = lista[i]
        else:
            if (mayor < lista[i]):
                mayor = lista[i]
    return (menor, mayor)


lista = cargarEnteros()
menor, mayor = retornarMayorMenor(lista)
print(f"Menor {menor}")
print(f"Mayor {mayor}")
