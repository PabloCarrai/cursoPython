""" 
Se tiene que cargar los votos por tres candidatos a una eleccion.
En una lista cargar en la primer componente el nombre del candidato
y en la segunda componente cargar una lista con componentes de tipo tupla
con el nombre de la provincia y la cantidad de votos 
obtenidos en dicha provincia
Se debe cargar los datospor teclado, pero si se cargaran 
por asignacion tendria una estructura similar a la siguiente. 

candidatos = [("juan", [("cordoba", 100), ("buenos aires", 200)]),
              ("ana", [("cordoba", 50)]), ("luis", [("Buenos aires", 20)])]

1) funcion para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos
2) imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias

"""


def cargar_candidatos():
    candidatos = []
    for x in range(3):
        nom = input("Nombre  ")
        cant = int(input("Cuantas Provincias? "))
        provincias = []
        for z in range(cant):
            prov = input("Provincia? ")
            votos = int(input("Votos?"))
            provincias.append((prov, votos))
        candidatos.append((nom, provincias))
    return candidatos


def total_votos_candidatos(lista):
    for x in range(len(lista)):
        suma = 0
        for z in range(len(lista[x][1])):
            suma = suma+lista[x][1][z][1]
        print(lista[x][0], suma)


candidatos = cargar_candidatos()
total_votos_candidatos(candidatos)
