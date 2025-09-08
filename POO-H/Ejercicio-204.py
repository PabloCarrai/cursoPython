""" 
Definir una clase llamada Punto con dos atributos x e y
Crearle el metodo especial __srt__ para retornar un string con el formato (x,y)
"""


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


punto = Punto(2, 34)
print(punto)
