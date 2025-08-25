""" 
Definir una lista de enteros por asignacion
en el bloque principal. Llamar a una funcion que 
reciba la lista y nos retorne el producto de todo 
sus elementos. Mostrar dicho producto en el bloque
principal de nuestro programa
"""


def multiplicando_elementos(lista):
    acumulador = 1
    for i in range(len(lista)):
        acumulador *= lista[i]
    return acumulador


lista = [1, 2, 3, 4, 5]

print("Lista original")
print(lista)
print("El producto de todos los elementos es ")
print(multiplicando_elementos(lista))
