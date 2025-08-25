"""
En una empresa se almacenan los
sueldos de 10 personas.
Desarrollar las siguientes funciones
y llamarlas desde el bloque principal.
1) Carga de los sueldos en una lista.
2) Impresion de todos los sueldos.
3) Cuantos tienen un sueldo superior a 4000
4) Retornar el promedio de los sueldos
5) Mostrar todos los sueldos que estan por
debajo del promedio
"""


def cargaSueldos():
    sueldos = []
    for i in range(10):
        sueldo = int(input("Sueldo? "))
        sueldos.append(sueldo)
    return sueldos


def mostrarSueldos(lista):
    for i in range(len(lista)):
        print("----------------------")
        print("Sueldos agendados")
        print("Sueldo", lista[i])
        print("----------------------")


def sueldosSuperior(lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] > 4000:
            contador = contador+1
    print("Cantidad: ", contador)


def promedio_Sueldos(lista):
    promedio = 0
    for i in range(len(lista)):
        promedio = promedio+lista[i]
    return promedio//len(lista)


def debajo_cuatromil(lista, promedio):
    for i in range(len(lista)):
        if lista[i] < promedio:
            print("----------------------")
            print("Por debajo de promedio", promedio)
            print(lista[i])
            print("----------------------")


sueldos = cargaSueldos()
mostrarSueldos(sueldos)
sueldosSuperior(sueldos)
debajo_cuatromil(sueldos, promedio_Sueldos(sueldos))
