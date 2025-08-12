""" 
Crear y cargar una lista con 5 enteros. 
Implementar algoritmo que identifique el mayor 
valor de la lista. 
"""

#   Genero una lista vacia
lista = []
#   Cargo cada valor en la lista
for w in range(5):
    valor = int(input("Valor? "))
    lista.append(valor)

#   Presupongo que el primer valor es el mayor
mayor = lista[0]
for x in range(1, 5):
    #   Chequeo que eso sea asi
    if (lista[x] > mayor):
        #   Si hay algun valor mas grande asigno a mayor dicho valor
        mayor = lista[x]

print("Lista completa ")
print(lista)
print("Mayor de la lista ")
print(mayor)
