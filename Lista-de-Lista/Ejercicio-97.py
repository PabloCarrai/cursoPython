""" 
Crear y cargar una lista con los nombres de tres alumnos. 
Cada alumno tiene dos notas, almacenar las notas en una 
lista paralela. Cada componente de la lista paralela debera
ser una lista con dos notas. Imprimir luego cada nombre y sus 
dos notas. 
Si cargamos los datos por asignacion seria algo parecido a 
esto. 

alumno = ["Juan", "Ana", "Luis"]
notas = [[10, 8], [9, 9], [2, 10]]

En la componente 0 de la lista tenemos almacenado
el nombre "Juan" y como son lista paralelas en 
la componente 0 de la lista notas tendremos almacenado
una lista con las dos notas 10 y 8
Nuestro objetivo es cargarlo por teclado
"""
alumno = []
notas = []

for i in range(3):
    print("Carga de Estudiantes ")
    nombre = input("Nombre?   ")
    alumno.append(nombre)
    nota1 = int(input("Nota? "))
    nota2 = int(input("Nota? "))
    notas.append([nota1, nota2])

print("Impresion nombres ")
for i in range(len(alumno)):
    print(alumno[i], notas[i][0], notas[i][1])
