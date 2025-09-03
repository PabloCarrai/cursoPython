""" 
Crear un diccionario en python para almacenar los datos de empleados
de una empresa. La clave sera su numero de legajo y en su valor se 
almacena una lista con el nombre, profesion y sueldo. 
Desarrollar las siguientes funciones. 
1)  Carga de datos de empleados
2)  Permitir modificar el sueldo de un empleado. Ingresando su numero de legajo para buscarlo. 
3)  Mostrar todos los datos de empleados que tienen una profesion de "analista de sistema"
"""


def cargar_empleados():
    empleados = {}
    continua = "s"
    while continua == "s":
        lista = []
        nlegajo = input("Numero de Legajos?  ")
        empleado = input("Nombre?  ")
        profesion = input("Profesion?  ")
        sueldo = int(input("Sueldo?  "))
        lista.append(empleado)
        lista.append(profesion)
        lista.append(sueldo)
        empleados[nlegajo] = lista
        continua = input("Desea cargar otro empleado s/n?   ")
    return empleados


def mostrar_empleados(diccionario):
    print("-"*60)
    print("Empleados  ")
    print("-"*60)
    for legajo in diccionario:
        if diccionario[legajo][1] == "analista de sistemas":
            print(
                f"Legajo: {legajo} Nombre: {diccionario[legajo][0]} Profesion: {diccionario[legajo][1]} Sueldo: {diccionario[legajo][2]}")
    print("-"*60)


def editar_sueldo(diccionario):
    nlegajo = input("Legajo del empleado?  ")
    sueldo = int(input("Nuevo sueldo? "))
    if nlegajo in diccionario:
        diccionario[nlegajo][2] = sueldo
    else:
        print("No existe dicho empleado")


empleados = cargar_empleados()
mostrar_empleados(empleados)
editar_sueldo(empleados)
mostrar_empleados(empleados)