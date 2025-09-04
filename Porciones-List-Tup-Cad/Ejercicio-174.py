""" 
Cargar una cadena de caracteres por teclado. 
Mostrar la cadena del final al principio utilizando
subindices negativos
"""


def delUltimoAlPrimero(cadena):
    indiceNegativo = - 1
    for x in range(len(cadena)):
        print(cadena[indiceNegativo], end="")
        indiceNegativo = indiceNegativo - 1


cadena = input("Ingrese cadena ")
print(f"Cadena Original {cadena} ")
print("Cadena de atras para adelante ")
delUltimoAlPrimero(cadena)
