"""  
Confeccionar una funcion que le enviemos
como parametros dos enteros y nos retorne
el mayor.
"""


def retornarMayor(v, v1):
    if (v > v1):
        return v
    else:
        return v1


v = int(input("Valor?  "))
v1 = int(input("Valor?  "))
maximo = retornarMayor(v, v1)
print("El mayor es ", maximo)
