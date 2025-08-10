"""  
Definir una lista que almacene 5 enteros. 
Sumar todos sus elementos y mostrar dicha suma
"""

totalizadorEnteros = 0
lista = [10, 2, 6, 8, 15]
for i in range(len(lista)):
    totalizadorEnteros = totalizadorEnteros + lista[i]

print("Lista")
print(lista)
print("Suma")
print(totalizadorEnteros)
