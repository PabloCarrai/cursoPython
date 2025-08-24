""" 
Confeccionar una funcion que le enviemos
como parametro un string y nos retorne
la cantidad de caracteres que tiene. En
El bloque principal solicitar la carga por
teclado y llamar a la funcion dos veces. 
Imprimir en el bloque principal cual de 
las dos palabras tiene mas caracteres. 
"""


def contar_Palabra(palabra):
    return len(palabra)


def enviar_palabra(p, p1):
    palabra = contar_Palabra(p)
    palabra1 = contar_Palabra(p1)
    if (palabra == palabra1):
        print("Son del mismo tamaño de caracteres")
    else:
        if (palabra > palabra1):
            print("La palabra con mayor caracter es la primer palabra ", palabra)
        else:
            print("La palabra con mayor caracter es la primer palabra ", palabra1)


palabra = input("Palabra? ")
palabra1 = input("Palabra? ")
enviar_palabra(palabra, palabra1)
