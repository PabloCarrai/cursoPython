"""  
Definir dos lista de 3 elementos. 
La primer lista, cada elemento es una sublista con 
nombre del padre y de la madre de una familia. 
La segunda lista esta consituida por lista con los 
nombres de los hijos de cada familia. Puede
haber familia sin hijos. 
Tambien imprimir solo los nombres del padre y 
la cantidad de hijos que tiene dicho padre. 
Un ejemplo si se define por asignacion. 
padres = [["juan", "ana"], ["carlos", "maria"], ["pedro", "laura"]]
hijos = [["marcos", "alberto", "silvia"], [], ["oscar"]]
Como son listas paralelas podemos decir que
la familia cuyo padres sean "juan" y "ana" tienen tres
hijos llamados "marcos", "alberto", "silvia". La segunda familia
no tiene hijos y la tercera solo uno 
"""
padres = []
hijos = []

#   Cargo los padres
for x in range(3):
    #   Cargo la lista vacia para los padres
    padre = input("Nombre del Padre? ")
    madre = input("Nombre de la Madre? ")
    padres.append([padre, madre])


print("Los padres son ")
for x in range(len(padres)):
    for i in range(len(padres[x])):
        print(padres[x][i])

for x in range(3):
    nhijos = int(input("Cuantos Hijos tiene?  "))
    hijos.append([])
    for i in range(nhijos):
        hijo = input("Nombre?  ")
        hijos[x].append(hijo)

pos = 0
mayor = hijos[0]
for x in range(len(hijos)):
    if (hijos[x] > mayor):
        mayor = hijos[x]
        pos = x

print("Mas hijos ")
print(padres[pos][0])
