"""  
Crear una lista por asignacion. 
La lista tiene que tener 5 elementos. 
Cada elemento debe ser una lista. 
La primera lista tiene que tener un elemento. 
La segunda dos elementos y la tercera tres. 
Asi sucesivamente. Sumar todos los valores de la lista
"""
acumulador = 0
lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
for i in range(len(lista)):
    for e in range(len(lista[i])):
        acumulador = acumulador+lista[i][e]
print("-----------")
print("La suma da ")
print("-----------")
print(acumulador)
print("-----------")
