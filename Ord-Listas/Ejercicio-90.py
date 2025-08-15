""" 
Crear y cargar en una lista los nombres de 5 paises y en otra lista
paralela la cantidad de habitantes del mismo. Ordenar alfabeticamente
e imprimor los resultados. 
Por ultimo orgenar con respecto a la cantidad de habitantes(de mayor a menor)
e imprimir nuevamente. 
"""

paises = []
habitantes = []
for i in range(5):
    pais = input("Pais? ")
    habitante = int(input("Habitantes? "))
    paises.append(pais)
    habitantes.append(habitante)

#   Ordenamiento de paises alfabeticamente
for k in range(len(paises)-1):
    for x in range(len(paises)-1-k):
        if (paises[x] > paises[x+1]):
            aux = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux
            # ahora habitantes
            aux1 = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux1
print("Ordenado alfabeticamente")
for x in range(5):
    print(paises[x], habitantes[x])

#   Ordenamiento de paises alfabeticamente
for k in range(len(paises)-1):
    for x in range(len(paises)-1-k):
        if (paises[x] < paises[x+1]):
            aux = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux
            # ahora habitantes
            aux1 = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux1
print("Ordenado habitantes")
for x in range(5):
    print(paises[x], habitantes[x])
