"""  
Confeccionar una funcion que calcule
la superficie de un rectangulo y la retorne.
La funcion recibe como parametro los valores
de sus lados. 
def retornar_super(lado1,lado2):

En el bloque principal del programa cargar los
dos rectangulos y luego mostrar cual de los dos
tiene una superficie mayor
"""


def retornar_super(lado1, lado2):
    return lado1*lado2


lado = int(input("Primer Lado? "))
lado1 = int(input("Segundo Lado? "))
lado2 = int(input("Primer Lado? "))
lado3 = int(input("Segundo Lado? "))
primerRectangulo = retornar_super(lado, lado1)
segundoRectangulo = retornar_super(lado2, lado3)
if (primerRectangulo == segundoRectangulo):
    print("Ambos tiene misma superficie")
else:
    if (primerRectangulo > segundoRectangulo):
        print("El primer rectangulo tiene mayor superficie", primerRectangulo)
    else:
        print("El segundo rectangulo tiene mayor superficie", segundoRectangulo)
