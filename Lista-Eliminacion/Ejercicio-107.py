""" 
Crear una lista de 5 enteros y cargarlo por teclado. 
Borrar los elementos mayores o iguales a 10 y generar
una nueva lista con dichos valores. 
"""

lista = []
nuevaLista = []

for i in range(5):
    valor = int(input("Valor?  "))
    lista.append(valor)

print("-----------------")
print("Lista Original")
print("-----------------")
print(lista)
print("-----------------")

p = 0
while p < len(lista):
    if (lista[p] >= 10):
        nuevaLista.append(lista.pop(p))
    else:
        p = p+1


print("-----------------")
print("Lista Original resultante sin valor (>=10)")
print(lista)
print("-----------------")
print("Lista Resultante")
print("-----------------")
print(nuevaLista)
print("-----------------")
