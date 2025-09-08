""" 
Plantear una clase llamada Jugador. 
Definir en la clase Jugador los atributos, nombre y puntaje.
Y los metodos __init__ imprimir y pasar_tiempo(Debe reducir
en uno la variable de clase)
Declarar dentro de la clase Jugador una variable de clase
que indique cuantos minutos falta para el fin del juego
(Iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
reducir la variable de la clase de uno en uno hasta llegar a cero
"""


class Jugador:
    tiempo_faltante = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        print(
            f"Jugador: {self.nombre} Puntaje: {self.puntaje} faltan {Jugador.tiempo_faltante} ")

    def pasar_tiempo(self):
        Jugador.tiempo_faltante = Jugador.tiempo_faltante-1
        print(f"Faltan {Jugador.tiempo_faltante} para finalizar el partido")
        if Jugador.tiempo_faltante == 0:
            print("Termino el partido")


cacho = Jugador("Cacho", 123)
for i in range(30):
    cacho.imprimir()
    cacho.pasar_tiempo()
