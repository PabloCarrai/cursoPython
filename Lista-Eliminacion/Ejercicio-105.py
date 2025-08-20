"""
Crear una lista y almacenar 10
enteros pedidos por teclado.
Eliminar todos los elementos
que sean iguales al numero 5
"""

#   Lista
lista = []

#   Carga de los 10 valores
for i in range(10):
    valor = int(input("Valor?   "))
    lista.append(valor)

print("La lista Parte de  ")
print(lista)

#   Eliminar valores 5 de la lista
pos = 0
while pos < len(lista):
    if (lista[pos] == 5):
        lista.pop(pos)
    else:
        pos = pos+1

print("Esto queda asi  ")
print(lista)
