""" 
Plantear una funcion que reciba un string
en mayuscula o minuscula y retorne la cantidad
de letras a o A
"""


def cantidad_Aa(texto):
    cantidadA = 0
    for i in texto:
        if ((i == "a") or (i == "A")):
            cantidadA = cantidadA+1
    return cantidadA


palabra = input("Palabra?  ")
print("Cantidad de a o A en ", palabra, cantidad_Aa(palabra))
