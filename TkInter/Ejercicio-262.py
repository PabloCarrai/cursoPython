""" 
Disponer un boton y mostrar al azar una de las
tres cartas del problema anterio. Cada vez que
se presione sobre el boton generar un valor 
aleatorio y a partir de dicho valor mostrar
una de las cartas
"""


import tkinter as tk
from tkinter import ttk
from random import randint as rd


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.boton = tk.Button(self.ventana, text="Elegir",
                               command=self.elegirImagen)
        self.boton.grid(column=0, row=0)

        self.canvas1 = tk.Canvas(
            self.ventana, width=200, height=400, background="black")
        self.canvas1.grid(column=0, row=1, padx=10, pady=10)

        #   Hay que usar gif, y tambien ruta absoluta
        self.archivo0 = tk.PhotoImage(
            file="/home/ed/cursoPython/TkInter/1.gif")
        #   Hay que usar gif, y tambien ruta absoluta
        self.archivo1 = tk.PhotoImage(
            file="/home/ed/cursoPython/TkInter/2.gif")
        #   Hay que usar gif, y tambien ruta absoluta
        self.archivo2 = tk.PhotoImage(
            file="/home/ed/cursoPython/TkInter/3.gif")

        self.canvas1.create_image(10, 100, image=self.archivo0, anchor="nw")

        self.ventana.mainloop()

    def elegirImagen(self):

        # #   Elimino todo lo que haya en el canvas
        self.canvas1.delete("all")
        #   Genero un aleatorio entre 0 y 2
        aleatorio = rd(0, 2)
        if aleatorio == 0:
            self.canvas1.create_image(
                20, 100, image=self.archivo0, anchor="nw")
        elif aleatorio == 1:
            self.canvas1.create_image(
                20, 100, image=self.archivo1, anchor="nw")
        elif aleatorio == 2:
            self.canvas1.create_image(
                20, 100, image=self.archivo2, anchor="nw")


aplicacion = Aplicacion()
