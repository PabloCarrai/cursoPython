""" 
Desarrollar una clase que represente un punto
en el plano y tenga los siguientes metodos. 
Inicializar los valores de x e y que llegan
como parametros, imprimir en que cuadrante se
encuentra dicho punto

"""


class Punto:
    def __init__(self, puntox, puntoy):
        self.puntox = puntox
        self.puntoy = puntoy

    def imprimir(self):
        print(
            f"Coordemadas x:{self.puntox} y:{self.puntoy}")

    def imprimir_cuadrante(self):
        if ((self.puntox == 0) and (self.puntoy == 0)):
            print(
                f"Se encuentra en el centro del eje x:{self.puntox} y:{self.puntoy}")
        if ((self.puntox > 0) and (self.puntoy > 0)):
            print(
                f"Primer Cuadrante- x:{self.puntox} y:{self.puntoy}")
        if ((self.puntox < 0) and (self.puntoy > 0)):
            print(
                f"Segundo Cuadrante- x:{self.puntox} y:{self.puntoy}")
        if ((self.puntox < 0) and (self.puntoy < 0)):
            print(
                f"Tercer Cuadrante- x:{self.puntox} y:{self.puntoy}")
        if ((self.puntox > 0) and (self.puntoy < 0)):
            print(
                f"Cuarto Cuadrante- x:{self.puntox} y:{self.puntoy}")


locos = Punto(2, 4)
locos.imprimir()
locos.imprimir_cuadrante()

locos1 = Punto(-2, 4)
locos1.imprimir()
locos1.imprimir_cuadrante()

locos2 = Punto(-2, -4)
locos2.imprimir()
locos2.imprimir_cuadrante()

locos3 = Punto(2, -4)
locos3.imprimir()
locos3.imprimir_cuadrante()

locos4 = Punto(0, 0)
locos4.imprimir()
locos4.imprimir_cuadrante()
