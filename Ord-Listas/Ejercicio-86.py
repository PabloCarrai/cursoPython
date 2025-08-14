"""  
Crear una lista y almacenar los nombres
de 5 paises. Ordenar alfabeticamente la 
lista e imprimirla
"""
paises = []
for i in range(5):
    pais = input("Pais?  ")
    paises.append(pais)
print("Lista de Paises Generada ")
print(paises)

#   Metodo de la burbuja
for k in range(4):  # Siempre es len(lista)-1
    for x in range(4-k):
        if (paises[x] > paises[x+1]):
            aux = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux
print("Lista Ordenada")
print(paises)
