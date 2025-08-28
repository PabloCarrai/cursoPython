""" 
Almacenar en una lista 5 empleados, cada elemento 
es una lista con el nombre del empleado junto
a sus ultimos 3 sueldos(estos tres valores en tupla)
El programa debe tener las siguientes funciones. 
1) Carga de los nombres de empleados y sus ultimos tres sueldos. 
2) Imprimir el monto total cobrado por cada empleado.
3) Imprimir los nombres de empleados que tuvieron un ingreso
trimestral mayor a 10000 en los ultimos tres meses. 

Tener en cuenta que la estructura de datos si se carga por 
asignacion deberia de ser similar a 
empleados = [["juan", (20000, 30000, 4233)], ["ana", (3444, 1000, 53333)]]

"""


def cargarEmpleadoUltimosTresSueldos():
    empleados = []
    for i in range(5):
        nombre = input("Nombre? ")
        sueldo = int(input(f"Sueldo de {nombre}? "))
        sueldo1 = int(input(f"Sueldo de {nombre}? "))
        sueldo2 = int(input(f"Sueldo de {nombre}? "))
        empleados.append([nombre, (sueldo, sueldo1, sueldo2)])
    return empleados


def imprimirMontoTotalPorEmpleado(lista):
    for i in range(len(lista)):
        contador = lista[i][1][0]+lista[i][1][1]+lista[i][1][2]
        print(f"{lista[i][0]} Cobra: {contador}")


def imprimirIngresoMayorDiezmill(lista):
    print("Empleado sueldo mayor a 10000")
    for i in range(len(lista)):
        contador = lista[i][1][0]+lista[i][1][1]+lista[i][1][2]
        if contador > 10000:
            print(f"{lista[i][0]}, {contador}")


prueba = cargarEmpleadoUltimosTresSueldos()
imprimirMontoTotalPorEmpleado(prueba)
imprimirIngresoMayorDiezmill(prueba)
