""" 
Ingresar por teclado los nombres de 5 personas en una lista.
Mostrar el nombre de persona menor en orden alfabetica
"""

listaNombres = []
for t in range(5):
    nombre = input("Nombre?   ")
    listaNombres.append(nombre)

nombreMenorAlfabeticamente = listaNombres[0]
for t in range(len(listaNombres)):
    if (listaNombres[t] < nombreMenorAlfabeticamente):
        nombreMenorAlfabeticamente = listaNombres[t]

print("Lista Completa")
print(listaNombres)
print("Menor Alfabeticamente")
print(nombreMenorAlfabeticamente)
