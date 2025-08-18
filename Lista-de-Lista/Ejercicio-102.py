"""  
Definir una lista y almacenar los nombres
de 3 empleados. Por otro lado definir otra lista
en cada elemento una sublista con los numeros de 
dias del mes que el empleado falto. 
Imprimir los nombres de los empleados y los dias que falto
Mostrar los empleados con la cantidad de inasistencia.
Finalmente mostrar el nombre o los nombres de los 
empleados que faltaron menos dias. 
"""

empleados = []
faltas = []

for k in range(3):
    nombre = input("Nombre? ")
    empleados.append(nombre)
    cantidad = int(input("Dias? "))
    faltas.append([])
    for x in range(cantidad):
        dia = int(input("Numero de dias que falto "))
        faltas[k].append(dia)

print("Nombres y dias que faltaron ")
for k in range(3):
    print(empleados[k])
    for x in range(len(faltas[k])):
        print(faltas[k][x])

print("Nombre empleado y cantidad de inasistencias")
for x in range(3):
    print(empleados[x], len(faltas[x]))

men = len(faltas[0])
for x in range(3):
    if len(faltas[x]) < men:
        men = len(faltas[x])

print("Empleado de menor falta")
for x in range(3):
    if (len(faltas[x]) == men):
        print(empleados[x])
