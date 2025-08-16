"""  
Crear una lista por asignacion. La lista tiene que tener 2elementos. 
Cada elemento debe ser una lista de 5 enteros. 
Calcular y mostrar la suma de cada lista contenidda en la lista
principal
"""
acu = 0
lista = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]
suma1 = lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
suma2 = lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print("--------------")
print(suma1)
print("--------------")
print(suma2)
print("--------------")
for x in range(len(lista[0])):
    acu = acu+lista[0][x]
print(acu)
acu = 0
print("--------------")
for x in range(len(lista[1])):
    acu = acu+lista[1][x]
print(acu)
print("--------------")
print("--------------")
for k in range(len(lista)):
    suma = 0
    for i in range(len(lista[k])):
        suma = suma+lista[k][i]
    print(suma)
