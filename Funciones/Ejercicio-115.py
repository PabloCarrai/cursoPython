"""
Desarrollar una funcion que reciba un string.
Como parametro y nos muestre la cantidad de
vocales. Llamarlo desde el bloque principal
del programa 3 veces con string distintos.
"""


def contarVocales(palabra):
    contadorVocales = 0
    for i in palabra:
        if ((i in "aeiou") or (i in "AEIOU")):
            contadorVocales += 1
    print("Cantidad de Vocales")
    print(contadorVocales)
    print("Palabra")
    print(palabra)


print("-----------------------------------------------")
contarVocales("PutOO")
print("-----------------------------------------------")
contarVocales("Espectacular")
print("-----------------------------------------------")
contarVocales("Supercalifrasquilisticoespiadidoso")
print("-----------------------------------------------")
contarVocales("administracion")
print("-----------------------------------------------")
