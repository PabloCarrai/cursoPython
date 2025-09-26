import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.canvas1 = tk.Canvas(
            self.ventana, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0, padx=10, pady=10)
        #   Esto enlace el evento con nuestro metodo(Motion es el evento del movimiento de mouse)
        self.canvas1.bind("<Motion>", self.mover_mouse)
        #   Ahora capturo el evento del boton ezquierdo
        self.canvas1.bind("<Button-1>", self.presion_mouse)

        self.ventana.mainloop()

    def mover_mouse(self, evento):
        self.ventana.title(f"{evento.x}x{evento.y}")

    def presion_mouse(self, evento):
        self.canvas1.create_oval(
            evento.x-5, evento.y-5, evento.x+5, evento.y+5, fill="green")


aplicacion = Aplicacion()
