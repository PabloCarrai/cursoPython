"""  
Desarrollar un programa que permita cargar
5 nombres de persnas y sus edades. 
Realizar la carga por teclado de todos los
datos imprimir los nombres de personas mayores
de edad(>=18)
"""
nombres = []
edades = []

for i in range(5):
    nombre = input("Nombre?  ")
    edad = int(input("Edad? "))
    nombres.append(nombre)
    edades.append(edad)

for i in range(5):
    if (edades[i] >= 18):
        print("Mayores de edad")
        print(nombres[i])
