""" 
Desarrollar un programa que permita 
cargar 5 nombres de personas y sus
edades respectivas. Luego de realizar
la carga por teclado de todos los datos
imprimir los nombres de las personas 
mayores de edad(mayor o igual a 18 años)
Imprimir edad promedio de las personas
"""


def cargarPersonaEdad():
    nombres = []
    edades = []
    for i in range(5):
        nombre = input("Nombre? ")
        edad = int(input("Edad? "))
        nombres.append(nombre)
        edades.append(edad)

    for e in range(len(edades)):
        if edades[e] >= 18:
            print("Mayores de edad")
            print("Nombre ", nombres[e], " Edad:", edades[e])

    pedades = 0
    for x in range(len(edades)):
        pedades = pedades+edades[x]
    print("Promedio de edades ")
    print(pedades/len(edades))


cargarPersonaEdad()
