""" 
Plantear una clase Club y otra Clase Socio.
La clase Socio debe tener los siguientes atributos. 
nombre, y antiguedad en el club(años)
En el metodo __init__ de la clase Socio pedir la carga
por teclado del nombre y su antiguedad. 
La clase Club debe tener como atributo 3 objetos
de la clase Socio. 
Definir una responsabilidad para imprimir 
el nombre del socio con mayor antiguedad en el club
"""


class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def mayorAntiguedad(self):
        self.socio1.imprimir()
        self.socio2.imprimir()
        self.socio3.imprimir()
        if ((self.socio1.antiguedad > self.socio2.antiguedad) and (self.socio1.antiguedad > self.socio3.antiguedad)):
            print(
                f"El socio con mas antiguedad es {self.socio1.nombre} con {self.socio1.antiguedad}")
        else:
            if ((self.socio2.antiguedad > self.socio1.antiguedad) and (self.socio2.antiguedad > self.socio3.antiguedad)):
                print(
                    f"El socio con mas antiguedad es {self.socio2.nombre} con {self.socio2.antiguedad}")
            else:
                if ((self.socio3.antiguedad > self.socio2.antiguedad) and (self.socio3.antiguedad > self.socio1.antiguedad)):
                    print(
                        f"El socio con mas antiguedad es {self.socio3.nombre} con {self.socio3.antiguedad}")


class Socio:
    def __init__(self):
        self.nombre = input("Nombre del Socio? ")
        self.antiguedad = int(input("Antiguedad en el Club? "))

    def imprimir(self):
        print(f"{self.nombre} tiene una antiguedad de {self.antiguedad}")


club = Club()
club.mayorAntiguedad()
