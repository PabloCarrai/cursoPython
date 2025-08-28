""" 
Desarrollar una funcion que solicite la carga del 
dia,mes y año y almacene dichos datos en una tupla
que luego debe retornar. La segunda funcion a implementar
debe recibir una tupla como la fecha y mostrarla en pantalla
"""


def generarTupla():
    dia = int(input("Dia?  "))
    mes = int(input("Mes?  "))
    anio = int(input("Año?  "))
    tupla = (dia, mes, anio)
    return tupla


def mostrarTupla(tupla):
    print(f"Hoy es {tupla[0]}/{tupla[1]}/{tupla[2]}")


tupla = generarTupla()
mostrarTupla(tupla)
