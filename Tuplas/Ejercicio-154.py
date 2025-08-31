""" 
Definir una funcion que cargue
una lista de palabras y la retorne. 
Luego otra funcion tiene que mostrar
las palabras de la lista que tienen
mas de 5 caracteres
"""


def cargar_palabras():
    palabras = []
    cantidad_Palabras = int(input("Cuantas Palabras cargara?  "))
    for i in range(cantidad_Palabras):
        palabra = input("Palabra? ")
        palabras.append(palabra)
    return palabras


def mostrar_palabra_mas_cinco_Caracteres(lista):
    for elemento in lista:
        if len(elemento) > 5:
            print("Con mas de 5 caracteres")
            print(f"Palabras {elemento}")


palabras = cargar_palabras()
mostrar_palabra_mas_cinco_Caracteres(palabras)
