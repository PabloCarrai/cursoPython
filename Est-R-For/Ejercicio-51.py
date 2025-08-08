"""  
Se cuenta con la siguiente informacion. 
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiantes deben ingresarse por teclado
a) Obtener el promedio de las edades de cada turno
b) Imprimir dichos promedios
c) Mostrar por pantalla un mensaje que indique cual de los
tres turnos tiene un promedio de edades mayores. 
"""
totalEdadTm = 0
totalEdadTt = 0
totalEdadTn = 0
for i in range(5):
    edad = int(input("Edad Estudiante Turno Mañana  "))
    totalEdadTm = totalEdadTm+edad
for x in range(6):
    edad = int(input("Edad Estudiante Turno Tarde    "))
    totalEdadTt = totalEdadTt+edad
for a in range(11):
    edad = int(input("Edad Estudiantes Turno Noche   "))
    totalEdadTn = totalEdadTn+edad
promedioTm = totalEdadTm/5
promedioTt = totalEdadTt/6
promedioTn = totalEdadTn/11
print("Promedio Edades Turno Mañana")
print(promedioTm)
print("Promedio Edades Turno Tarde")
print(promedioTt)
print("Promedio Edades Turno Noche")
print(promedioTn)

print("Turno con Mayor Promedio de Edad")
if ((promedioTm > promedioTt) and (promedioTm > promedioTn)):
    print("Turno Mañana ")
    print(promedioTm)
else:
    if ((promedioTt > promedioTm) and (promedioTt > promedioTn)):
        print("Turno Tarde")
        print(promedioTt)
    else:
        if ((promedioTn > promedioTm) and (promedioTn > promedioTt)):
            print("Turno Noche")
            print(promedioTn)
