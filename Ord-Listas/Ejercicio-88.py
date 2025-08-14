"""  
Cargar una lista con 5 elementos enteros. 
Ordenarla de menor a mayor y mostrarla por pantalla. 
Luego ordenar de mayor a menor e imprimirla nuevamente. 
"""

cincoElementos = []
for i in range(5):
    valor = int(input("Valor?   "))
    cincoElementos.append(valor)
print("Lista Creada ")
print(cincoElementos)

#   Menor a mayor
for i in range(len(cincoElementos)-1):
    for x in range(len(cincoElementos)-1-i):
        if (cincoElementos[x] > cincoElementos[x+1]):
            aux = cincoElementos[x]
            cincoElementos[x] = cincoElementos[x+1]
            cincoElementos[x+1] = aux
print("Lista Ordenada Menor a Mayor")
print(cincoElementos)

#   Mayor a menor
for i in range(len(cincoElementos)-1):
    for x in range(len(cincoElementos)-1-i):
        if (cincoElementos[x] < cincoElementos[x+1]):
            aux = cincoElementos[x]
            cincoElementos[x] = cincoElementos[x+1]
            cincoElementos[x+1] = aux
print("Lista Ordenada Mayor a Menor")
print(cincoElementos)
