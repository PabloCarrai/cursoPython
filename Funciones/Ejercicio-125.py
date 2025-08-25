""" 
Crear y cargar por teclado en el bloque principal. 
una lista de 5 enteros. Implementar una funcion que
imprima el mayor y el menor valor de la lista
"""


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


lista = []
for i in range(5):
    valor = int(input("Valor?   "))
    lista.append(valor)

print("La lista original quedo como ")
print(lista)
print("El mayor valor de la lista es ", retornarMayor(lista))
print("El menor valor de la lista es ", retornarMenor(lista))
