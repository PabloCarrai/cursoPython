"""  
Solicitar la carga del nombre
de una persona en minusculas. 
Mostrar un mensaje si comienza con
vocal dicho nombre
"""

nombre = input("Ingrese un nombre   ")
if (nombre[0] == "a" or nombre[0] == "e" or nombre[0] == "i" or nombre[0] == "o" or nombre[0] == "u"):
    print("Su nombre comienza con una vocal ")
    print(nombre[0])
