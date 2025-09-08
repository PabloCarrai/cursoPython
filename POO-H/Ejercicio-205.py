""" 
Declarar una clase Llamada Familia. Definir como atributos 
el nombre del padre, madre y una lista con los nombres de los
hijos.
Definir el metodo especial __str__ que retorne un string
con el nombre del padre, la madre y de todos sus hijos
"""


class Familia:
    def __init__(self, padre, madre, hijos=[]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        cadena = self.padre+", "+self.madre
        for hijo in self.hijos:
            cadena = cadena+", "+hijo
        return cadena


familia = Familia("Miguel", "Ana", ["Marta", "Yesica", "Romina", "Leo"])
print(familia)
