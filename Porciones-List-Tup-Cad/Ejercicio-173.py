"""  
Confeccionar una funcion que reciba una palabra y verifique
si es capicua(es decir que se lee igual de izquierda a derecha
y de derecha a izquierda)
"""


def capicua(cadena):
    iguales = 0
    indice = -1  # ultimo caracter
    for x in range(0, len(cadena)//2):
        if cadena[x] == cadena[indice]:
            iguales = iguales+1
        indice = indice-1
    print(cadena)
    if iguales == (len(cadena)//2):
        print("Capicua")
    else:
        print("No es capicua")


capicua("neuquen")
capicua("Casa")
