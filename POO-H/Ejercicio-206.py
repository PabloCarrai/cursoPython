""" 
Desarrollar un programa que implemente una clase
llamada Jugador. Definir como atributo su nombre y
puntaje. 
Codificar el metodo especial __str__ que retorne el nombre
y si es un principiante(menos de 1000 puntos) o experto
(1000 o mas puntos)
"""


class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def __str__(self):
        nivel = ""
        if self.puntaje < 1000:
            nivel = "Principiante"
        else:
            if self.puntaje > 1000:
                nivel = "Experto"
        return f"Nombre: {self.nombre} Puntaje: {self.puntaje} Nivel: {nivel}"


pedro = Jugador("Miguel", 1001)
print(pedro)
juana = Jugador("Juana", 999)
print(juana)
yesica = Jugador("Yesica", 2002)
print(yesica)
