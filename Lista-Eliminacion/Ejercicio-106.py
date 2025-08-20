"""  

Crear dos listas paralelas. En la primera
ingresar los nombres de empleados y en la 
segunda los sueldos de cada empleado. 
Ingresar por teclado cuando inicia el programa
a la cantidad de empleados de la empresa. 
Borrar luego todos los empleados que tienen
un sueldo mayor a 10000(tanto sueldo como empleado)
"""

#   Creo las listas vacias
nombres = []
sueldos = []
#   Averiguo cuantos empleados van a cargar
cEmpleadosCargar = int(input("Cuantos empleados va a cargar?  "))
#   Hago la carga del empleado y el sueldo
for i in range(cEmpleadosCargar):
    nombre = input("Nombre? ")
    sueldo = int(input("Sueldo?  "))
    nombres.append(nombre)
    sueldos.append(sueldo)
#   Muestro como quedaron las listas
print("Empleados-Sueldos ")
for x in range(len(nombres)):
    print(nombres[x], sueldos[x])
#   Recorro la lista y veo si tienen el sueldo >10000 y elimino en ambas listas
p = 0
while p < len(nombres):
    if (sueldos[p] > 10000):
        nombres.pop(p)
        sueldos.pop(p)
    else:
        p = p+1
#   Muestro como quedaron las listas
print("Se quedan")
print("Empleados-Sueldos ")
for x in range(len(nombres)):
    print(nombres[x], sueldos[x])
