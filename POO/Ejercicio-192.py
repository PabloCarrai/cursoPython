"""  
Implementar la clase Operaciones. Se deben cargar dos valores enteros
por teclado en el metodo __init__, calcular su suma, resta, multiplicacion
y division, cada una en un metodo, imprimir dichos resultados
"""


class Operaciones:
    def __init__(self):
        self.valor = int(input("Valor? "))
        self.valor1 = int(input("Valor?  "))

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
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.division()
