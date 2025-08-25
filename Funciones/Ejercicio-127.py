"""
Desarrollar una funcion que reciba una lista
de string y nos retorne el que tiene mas caracteres.
Si hay mas de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente
mas baja.
En el bloque principal iniciamos por asignacion
la lista de string.
palabras=["enero","febrero","marzo","abril","mayo","junio"]
print("Palabra con mas caracteres:",mascaracteres(palabra) )
"""


def mascaracteres(palabra):
    mayorCaracteres = palabra[0]
    for i in range(len(palabra)):
        if len(palabra[i]) > len(mayorCaracteres):
            mayorCaracteres = palabra[i]
    return mayorCaracteres, "Cantidad de caracteres ", len(mayorCaracteres)


palabra = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:", mascaracteres(palabra))
