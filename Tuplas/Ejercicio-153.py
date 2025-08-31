""" 
Almacenar en una lista 5 elementos las tuplas con 
el nombre del empleado y su sueldo. 
Implementar las funciones
1) Cargar empleado
2) Impresion de los empleados y sus sueldos
3) Nombre del empleado con sueldo mayor
4) Cantidad de empleados con sueldo menor a 1000
Si se cargara por teclado seria algo similar a 
empleados = [("juan", 2300), ("pedro", 1200)]

"""


def cargar_Empleados():
    empleados = []
    for i in range(5):
        empleado = input("Nombre?  ")
        sueldo = int(input("Sueldo?  "))
        empleados.append((empleado, sueldo))
    return empleados


def imprimir_Empleados(lista):
    print("Empleado-Sueldo")
    for e in lista:
        print(e[0], e[1])


def mayor_Sueldo(lista):
    mayor = lista[0][1]
    ems = lista[0][0]
    for nombre, sueldo in lista:
        if sueldo > mayor:
            mayor = sueldo
            ems = nombre
    print("Mayor sueldo")
    print(mayor, ems)


def cant_empleados(lista):
    cantEmpleados = 0
    for nombre, sueldo in lista:
        if sueldo < 1000:
            cantEmpleados = cantEmpleados+1
    print(f"Cantidad de sueldos menor a 1000: {cantEmpleados}")


empleados = cargar_Empleados()
imprimir_Empleados(empleados)
imprimir_Empleados(empleados)
mayor_Sueldo(empleados)
cant_empleados(empleados)
