""" 
Almacenar en una lista de 5 elementos tuplas que guardan 
el nombre de un pais y la cantidad de habitantes. 
Definir tres funciones, en la primera cargar la lista, 
en la segunda imprimirla y en la tercera mostrar
el nombre del pais con mayor cantidad de habitantes. 
"""


def cargarTresTuplas():
    lista = []
    for i in range(5):
        pais = input("Pais?  ")
        habitantes = int(input("Habitantes?  "))
        lista.append((pais, habitantes))
    return lista


def imprimirPaisHabitantes(lista):
    print("-"*20)
    print("Paises- Habitantes-")
    for i in range(len(lista)):
        print(lista[i][0], lista[i][1])
    print("-"*20)


def imprimirPaisMayorHabitantes(lista):
    mayorHabitantes = lista[0][1]
    paismayorHabitantes = lista[0][0]
    for e in range(len(lista)):
        if (lista[e][1] > mayorHabitantes):
            mayorHabitantes = lista[e][1]
            paismayorHabitantes = lista[e][0]
    print("-"*20)
    print("Paises con mas  Habitantes-")
    print(f"{paismayorHabitantes} - {mayorHabitantes}")
    print("-"*20)


datos = cargarTresTuplas()
imprimirPaisHabitantes(datos)
imprimirPaisMayorHabitantes(datos)
