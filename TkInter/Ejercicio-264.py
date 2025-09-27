import tkinter as tk
import random


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()

        self.canvas = tk.Canvas(self.ventana, width=900,
                                height=500, background="black")
        self.canvas.grid(column=0, row=0)

        for x in range(101):
            x1 = random.randint(1, 900)
            y1 = random.randint(1, 500)
            self.cuadrado = self.canvas.create_rectangle(
                x1, y1, x1+20, y1+20, fill="red", outline="red", tags="movil")

        self.canvas.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.canvas.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.cuadrado_seleccionado = None

        self.ventana.mainloop()

    def presion_boton(self, evento):
        cuadrado = self.canvas.find_withtag(tk.CURRENT)
        self.cuadrado_seleccionado = (cuadrado, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        cuadrado, x1, y1 = self.cuadrado_seleccionado
        self.canvas.move(cuadrado, x-x1, y-y1)
        self.cuadrado_seleccionado = (cuadrado, x, y)


aplicacion = Aplicacion()
