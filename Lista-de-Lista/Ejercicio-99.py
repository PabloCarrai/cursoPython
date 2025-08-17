"""  
Solicitar por teclado dos enteros. 
El primer valor indica la cantidad de 
elementos que crearemos en la lista. 
El segundo valor indica la cantidad de 
elementos que tendra cada una de las 
listas internas a la lista principal. 
Por ejemplo si el operador carga un 2
y un 4 significa que debemos crear una lista
similar a la siguiente
lista = [[1, 1, 1, 1], [1, 1, 1, 1]
"""
lista = []

valor = int(input("Primer Valor?   "))
valor1 = int(input("Segundo Valor?   "))
for k in range(valor):
    #   Agrega una lista vacia
    lista.append([])
    for x in range(valor1):
        valor2 = int(input("Valor? "))
        lista[k].append(valor2)
print(lista)
suma = 0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma = suma+lista[k][x]

print(suma)
