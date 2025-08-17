"""  
Se tiene que cargar la siguiente informacion. 
Nombre de 3 empleados. 
Ingresos en concepto de sueldo, cobrado por cada empleado 
en los ultimos 3 meses. 
Confeccionar el programa para. 
a) Realizar la carga de los nombres de empleados y 
los tres sueldos por cada empleado. 
b) Generar una lista que contenga el ingreso 
acumulado en sueldos en los ultimos 3 meses para 
cada empleado. 
c) Mostrar por pantalal el total pagado en sueldos 
a cada empleado en los ultimos 3 meses. 
d) Obtener el nombre del empleado que tuvo el mayor
ingreso acumulado. 
En este problema definiremos tres listas. 
Una lista para almacenar los nombres de los empleados
por ejemplo si la cargamos por asignacion. 
nombres = ["Juan", "Ana", "Luis"]
Una lista paralela a la anterior para almacenar los 
sueldos en los ultimos tres meses por cada
empleado. 
sueldos = [[5000, 5100, 5800], [7000, 7900, 8000], [10000, 11000, 10000]]
Otra lista paralela donde almacenamos el total de sueldos cobrados
por cada empleados que resulta de sumar los tres sueldos de cada
empleado en la lista sueldos
totalSueldos = [[15900], [22900], [31000]]
Es importante notar que estos datos no los cargamos por asignacion sino
los cargaremos por teclado a las dos primeras listas y la tercera la generaremos
extrayendo los datos de la lista sueldos
"""
nombres = []
sueldos = []
totalSueldos = []
#   Cargamos los empleados y sus sueldos
for i in range(3):
    #   El acumulador va a sumar las tres cifras por cada vuelta
    acumulador = 0
    #   Cargo el nombre del empleadp
    empleado = input("Empleado?  ")
    nombres.append(empleado)
    #   Cargo los tres sueldos
    sueldo1 = int(input("Sueldo? "))
    sueldo2 = int(input("Sueldo? "))
    sueldo3 = int(input("Sueldo? "))
    #   Los agrego a la lista
    sueldos.append([sueldo1, sueldo2, sueldo3])
    #   totalizo el total de los tres sueldos
    acumulador = acumulador+sueldo1+sueldo2+sueldo3
    totalSueldos.append([acumulador])
#   Muestro la info
print("Empleados")
for i in range(len(nombres)):
    print(nombres[i], totalSueldos[i][0])

pos = 0
mayor = totalSueldos[0]
for i in range(len(totalSueldos)):
    if totalSueldos[i] > mayor:
        mayor = totalSueldos[i]
        pos = i
print("Mayor sueldo ")
print(nombres[pos], totalSueldos[i][0])
