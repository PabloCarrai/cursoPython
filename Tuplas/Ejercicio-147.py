""" 
Confeccionar un programa con las siguientes funciones. 
1) Cargar el nombre de un empleado y su sueldo. 
Retornar una tupla con dichos valores. 
2) Una funcion que reciba como parametros dus tuplas
con los nombres y sueldos de empleados y muestre
el nombre del empleado con sueldo mayor. 

En el bloque principal del programa llamar dos veces a la 
funcion de carga y seguidamente llamar a la funcion que muestre
el nombre del empleado con sueldo mayor

empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mayor_sueldo(empleado1, empleado2)
"""


def cargar_empleado():
    nombre = input("Nombre?  ")
    sueldo = int(input("Sueldo?  "))
    return (nombre, sueldo)


def mayor_sueldo(v, v1):
    if (v[1] > v1[1]):
        print(f"Empleado con mayor sueldo: {v[0]}, Sueldo de: $ {v[1]}")
    else:
        print(
            f"Empleado con mayor sueldo: {v1[0]}, Sueldo de: $ {v1[1]}")


empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mayor_sueldo(empleado1, empleado2)
