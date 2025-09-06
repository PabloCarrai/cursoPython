""" 
Desarrollar un programa que cargue los lados de un triangulo
por teclado e implemente los siguientes metodos: inicializar los atributos
imprimir el valor del lado mayor, otro metodo que muestre si
es equilatero o no. El nombre de la clase llamarla Triangulo
"""


class Triangulo:
    def inicializar(self):
        self.lado = int(input("Lado 1?  "))
        self.lado1 = int(input("Lado 2?  "))
        self.lado2 = int(input("Lado 3?  "))

    def imprimirMayor(self):
        if ((self.lado > self.lado1) and (self.lado > self.lado2)):
            print(
                f"Valores lado 1: {self.lado} lado 2: {self.lado1} lado 3: {self.lado2}")
            print(f"El mayor es {self.lado}")
        else:
            if ((self.lado1 > self.lado) and (self.lado1 > self.lado2)):
                print(
                    f"Valores lado 1: {self.lado} lado 2: {self.lado1} lado 3: {self.lado2}")
                print(f"El mayor es {self.lado1}")
            else:
                if ((self.lado2 > self.lado) and (self.lado2 > self.lado1)):
                    print(
                        f"Valores lado 1: {self.lado} lado 2: {self.lado1} lado 3: {self.lado2}")
                    print(f"El mayor es {self.lado2}")

    def mostrarEquilatero(self):
        if ((self.lado == self.lado1) and (self.lado1 == self.lado2) and (self.lado == self.lado2)):
            print(
                f"Valores lado 1: {self.lado} lado 2: {self.lado1} lado 3: {self.lado2}")
            print("Es un equilatero  ")


triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimirMayor()
triangulo1.mostrarEquilatero()
