""" 
Confeccionar una funcoin que cargue por teclado
una lista de 5 enteros y la retorne. Una segunda
funcion debe recibir una lista y retornar el mayor
y el menor valor de la lista. Desde el bloque 
principal del programa llamar a ambas funciones e
imprimir el mayor y el menor de la lista
"""


def retornarLista():
    lista = []
    for i in range(5):
        valor = int(input("Valor? "))
        lista.append(valor)
    return lista


def mayorYMenor(lista):
    mayor = lista[0]
    menor = lista[0]

    for x in range(len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    return menor, mayor


lista = retornarLista()
print("Lista Original")
print(lista)
print("Menor,Mayor ")
print(mayorYMenor(lista))
