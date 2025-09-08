""" 
Declarar una clase Cuenta y dos subclases CajaAhorro y PlazoFijo.
Definir los atributos y metodos comunes entre una caja de ahorro
y un plazo fijo y agruparlo en la clase Cuenta. 
Una caja de ahorro y un plazo fijo tienen un nombre y un monto. 
Un plazo fijo añade un plazo de imposicion en dias y una tasa
de interes. Hacer que la caja de ahorro no genere interes.
En el bloque principal del programa definir un objeto de la 
CajaAhorro y otro de la clase PlazoFijo
"""


class Cuenta:
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def imprimir(self):
        print(f"Titular {self.nombre} Monto: {self.monto}")


class CajaAhorro(Cuenta):
    def __init__(self, nombre, monto):
        super().__init__(nombre, monto)

    def imprimir(self):
        print("Cuenta Caja de ahorro")
        super().imprimir()


class PlazoFijo(Cuenta):
    def __init__(self, nombre, monto, plazo, interes):
        super().__init__(plazo, interes)
        self.plazo = plazo
        self.interes = interes

    def imprimir(self):
        print("Cuenta plazo fijo ")
        return super().imprimir()
        print(f"Plazo en dias {self.plazo}")
        print(f"Interes {self.interes}")

    def ganancia(self):
        gan = self.monto*self.interes/100
        print(f"Monto de interes {gan}")


cajaahorro = CajaAhorro("Juan", 1300)
cajaahorro.imprimir()

plazofijo1 = PlazoFijo("Peres", 1000, 30, 0.75)
plazofijo1.imprimir()
plazofijo1.ganancia()
