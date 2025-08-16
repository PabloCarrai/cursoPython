""" 
Se tiene la siguiente lista 
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
Imprimir la lista. Luego fijate con el valor cero todos los elementos 
mayores a 50 del primer elemento de la lista. 
Volver a imprimir la lista
"""
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
print("------------")
print("Lista Original")
print("------------")
print(lista)
for i in range(len(lista[0])):
    if lista[0][i] > 50:
        lista[0][i] = 0
print("------------")
print("Lista Modificada")
print("------------")
print(lista)
