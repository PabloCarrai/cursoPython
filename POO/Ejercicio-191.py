""" 
Desarrollar una clase que represente
un Cuadrado y tenga los siguientes metodos,
Inicializar el valor del lado llegando como
parametro al mentodo __init__(definir el atributo
lado), imprimir su perimetro y su superficie
"""


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        print(f"El perimetro del lado {self.lado} es {self.lado*4}")

    def superficie(self):
        print(f"La superficie del lado {self.lado} es {self.lado*self.lado}")


cuadrado = Cuadrado(10)
cuadrado.perimetro()
cuadrado.superficie()
