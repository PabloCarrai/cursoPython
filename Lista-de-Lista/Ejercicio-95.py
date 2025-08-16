"""  
Se tiene la siguiente lista
lista = [[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]
Imprimir la lista. Luego fijar con el valor a cero todos los 
elementos mayores a 10 contenidos en todos los elementos de la 
variable lista. Volver a imprimir

"""

lista = [[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]
print("------------------")
print("Lista Original")
print("------------------")
print(lista)
for v in range(len(lista)):
    for u in range(len(lista[v])):
        if (lista[v][u] > 10):
            lista[v][u] = 0
print("------------------")
print("Lista Modificada")
print("------------------")
print(lista)
