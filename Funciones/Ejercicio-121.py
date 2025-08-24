"""  
Elaborar una funcion que nos retorne el perimetro
de un cuadrado pasando como parametro el 
valor de un lado
"""


def perimetro_Cuadrado(lado):
    return lado*4


lado = int(input("Lado del Cuadrado?  "))
print(perimetro_Cuadrado(lado))
