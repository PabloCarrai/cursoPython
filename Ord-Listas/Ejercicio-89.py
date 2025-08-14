"""  

"""

alumnos = []
notas = []
for x in range(5):
    nom = input("Nombre?  ")
    alumnos.append(nom)
    nota = int(input("Nota? "))
    notas.append(nota)

#   Ordenamiento de notas de mayor a menor
for k in range(4):
    for x in range(4-k):
        if (notas[x] < notas[x+1]):
            aux = notas[x]
            notas[x] = notas[x+1]
            notas[x+1] = aux
            # ahora alumnos
            aux1 = alumnos[x]
            alumnos[x] = alumnos[x+1]
            alumnos[x+1] = aux1
print("Lista de alumnos y notas ordenadas de mayor a meno")
for x in range(5):
    print(alumnos[x], notas[x])
