""" 
Realizar la carga de valores enteros por teclado.
Almacenarlo en una lista. Finalizar la carga de enteros
al ingresar el cero. Mostrar finalmente el tamaño de la lista
y el contenido de la lista
"""

lista = []
aux = 1
while aux != 0:
    valor = int(input("Valor? 0-salir "))
    if valor == 0:
        print("Adios ")
        aux = 0
    else:
        lista.append(valor)
print("Elementos de la lista ")
print(lista)
print("Cantidad de elementos de dicha lista ")
print(len(lista))
