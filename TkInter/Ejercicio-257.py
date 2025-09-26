import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.canvas1 = tk.Canvas(
            self.ventana, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0, padx=10, pady=10)
        #   Se dispara al presionar el boton izquierdo del mouse
        self.canvas1.bind("<ButtonPress-1>", self.boton_presion)
        #   Capturamos motion que se dispara al mover el mouse
        self.canvas1.bind("<Motion>", self.mover_mouse)
        #   Dispara cuando soltamos el boton izquierdo del mouse
        self.canvas1.bind("<ButtonRelease-1>", self.boton_soltar)

        self.presionado = False

        self.ventana.mainloop()

    def boton_presion(self, evento):
        self.presionado = True
        self.origenx = evento.x
        self.origeny = evento.y

    def mover_mouse(self, evento):
        if (self.presionado == True):
            self.canvas1.create_line(
                self.origenx, self.origeny, evento.x, evento.y, fill="orange")
            self.origenx = evento.x
            self.origeny = evento.y

    def boton_soltar(self, evento):
        self.presionado = False


aplicacion = Aplicacion()
