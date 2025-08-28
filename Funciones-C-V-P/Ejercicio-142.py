""" 
Confeccionar una funcion que reciva una serie de 
edades y me retorne la cantidad que son mayores o 
iguales a 18(como minimo se envia un entero a la 
funcion)
"""


def retornarMayores(*valor):
    cMayores = 0
    for x in valor:
        if x >= 18:
            cMayores = cMayores+1
    return f"Cantidad de elementos mayores o iguales a 18: {cMayores}"


lista = [19, 20, 10, 5, 8, 3, 15, 19, 22]
#   Desempaqueta los elementos de la lista
print(retornarMayores(*lista))
