"""  

Confeccionar una funcion que reciba entre 2 y 5 enteros. 
La misma nos tiene que retornar la suma de dichos valores.
Debe tener tres parametros por defecto
"""


def hacerSuma(v, v1, v2=0, v3=0, v4=0):
    return v+v1+v2+v3+v4


print(hacerSuma(1, 2, 3))
print(hacerSuma(10, 2, 300, 50))
