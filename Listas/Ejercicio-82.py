"""  
En un curso de 4 alumnos se registraron
las notas de sus examenes, y se debe procesar
de acuerdo a lo siguiente. 
a) Ingresar nombre y nota de cada alumno(almacenar
los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres
y condicion del alumno. En la condicion colocar
"Muy bueno" si la nota es mayor o igual a 8. 
"Bueno" si la nota esta entre 4 y 7 y colocar
"Insuficiente" si la nota es inferior a 4
c) Imprimir cantos alumnos tienen la leyenda
"Muy bueno"
"""

contMuyBueno = 0
alumnos = []
notas = []
for y in range(4):
    alumno = input("Alumno?  ")
    nota = float(input("Nota?  "))
    alumnos.append(alumno)
    notas.append(nota)

for y in range(4):
    if (notas[y] < 4):
        print(alumnos[y])
        print("Insuficiente ")
    else:
        if ((notas[y] > 4) and (notas[y] < 7)):
            print(alumnos[y])
            print("Bueno")
        else:
            if (notas[y] >= 8):
                print(alumnos[y])
                print("Muy bueno")
                contMuyBueno = contMuyBueno+1

print("Cantidad de Muy Buenos  ")
print(contMuyBueno)
