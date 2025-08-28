""" 
Definir una tupla con tres valores enteros. 
Convertir el contenido de la tupla a tipo lista. 
Modificar la lista y luego convertir la lista en tupla
Crear otra tupla a partir de tres variables independientes
que almacenan dia, mes año. (enpaquetamiento) luego 
desempaquetar la tupla a otras tres variables independientes
"""


def crear_tupla():
    dia = int(input("Dia? "))
    mes = int(input("Mes?  "))
    anio = int(input("Año?  "))
    return (dia, mes, anio)


def convertirTupla_Lista(tupla):
    return list(tupla)


def modificarLista(lista):
    lista[0] = 19
    return lista


def convertirListaTupla(lista):
    return tuple(lista)


tuplaPura = crear_tupla()
print("La tupla es ")
print(tuplaPura)
print("Ahora es ")
lista = convertirTupla_Lista(tuplaPura)
print(lista)
listaModificada = modificarLista(lista)
print("La lista modificada")
print(listaModificada)
print("Convierto la lista en tupla")
listaaTupla = convertirListaTupla(listaModificada)
print(listaaTupla)

#   Empaquetar
print("Crear tupla de tres variables independientes.")
dia = 10
mes = 2
anio = 2323
fechatupla3 = dia, mes, anio
print(fechatupla3)

print("Desenpaquetar")
dia1, mes1, anio1 = fechatupla3
print(dia1, mes1, anio1, sep="/")
