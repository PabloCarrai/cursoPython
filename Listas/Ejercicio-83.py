"""  
Realizar un programa que pida la carga de
dos listas numericas enteras de 4 elementos
cada una. Generar una tercer lista que surja
de la suma de los elementos de la misma
posicion de cada lista. Mostrar esta tercer
lista
"""

lista1 = []
lista2 = []
lista3 = []

#   Cargo primer lista
for i in range(4):
    valor = int(input("Valor? "))
    lista1.append(valor)
print("Primer lista hecha ")
#   Cargo segunda lista
for i in range(4):
    valor = int(input("Valor? "))
    lista2.append(valor)
print("Segunda lista hecha ")
#   Sumo valores de lista1 y lista2 en cada posicion y lo agrego a lista 3
for i in range(4):
    lista3.append(lista1[i]+lista2[i])
#   Visualizo lista 1
print(lista1)
#   Visualizo lista 2
print(lista2)
#   Visualizo lista 3
print(lista3)
