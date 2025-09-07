"""  
Plantear una clase Operaciones que solicite
en el metodo __init__ la carga de dos enteros
e inmediatamente muestre su suma, resta, multiplicacion
y division. Hacer cada operacion en otro metodo de 
la clase Operacion y llamarlo desde el metodo __init__
"""


class Operaciones:
    def __init__(self):
        self.valor = int(input("Valor? "))
        self.valor1 = int(input("Valor?  "))
        #   Invoco a los metodos de la funcion usando el self.metodo()
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        print(
            f"Los valores son {self.valor} {self.valor1} su Suma es {self.valor+self.valor1}")

    def resta(self):
        print(
            f"Los valores son {self.valor} {self.valor1} su Resta es {self.valor-self.valor1}")

    def multiplicacion(self):
        print(
            f"Los valores son {self.valor} {self.valor1} su Multiplicacion es {self.valor*self.valor1}")

    def division(self):
        print(
            f"Los valores son {self.valor} {self.valor1} su Division es {self.valor/self.valor1}")


operacion = Operaciones()
