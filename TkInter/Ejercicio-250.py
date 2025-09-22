"""  
En una aduana hay una maquina que sortea 
las personas cuyo equipaje seran revisados. 
La persona selecciona la cantidad de bultos
(hacer dicha seleccion mediante un spinbox)
Luego se presiona el boton sortear y aparece
al lado de ese boton una label de color rojo o
verde(en caso de ser rojo se revisa su equipaje
en caso de ser verde no se revisa)
Para sortear generar un valor aleatorio entre
1 y 3. Si se genera un 1 se revisa, se se genera
un 2 o 3 no se revisa. Mostrar un mensaje de 
error si el spinbox tiene un cero
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from random import randint as rd


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-250.py")
        self.ventana.geometry("400x150")

        self.spindbox = ttk.Spinbox(
            self.ventana, font_=0, to=3, width=2, state="readonly")
        self.spindbox.grid(column=1, row=0, padx=10, pady=10)
        self.spindbox.set("1")

        self.etiquetaSeleccione = ttk.Label(
            self.ventana, text="Seleccione la cantidad de bultos")
        self.etiquetaSeleccione.grid(column=0, row=0, padx=10, pady=10)

        self.botonsortear = ttk.Button(
            self.ventana, text="Sortear", command=self.sortear)
        self.botonsortear.grid(column=0, row=1, padx=10, pady=10)

        self.etiquetaResultado = ttk.Label(self.ventana, text="Debe Revisarse")
        self.etiquetaResultado.grid(column=1, row=1, padx=10, pady=10)

        self.ventana.mainloop()

    def sortear(self):
        self.valoraleatorio = rd(0, 3)
        if (self.valoraleatorio == 1):
            self.etiquetaResultado.config(text="Se Sortea")
            self.etiquetaResultado.config(background="red")
        else:
            if (self.valoraleatorio == 2 or self.valoraleatorio == 3):
                self.etiquetaResultado.config(text="No se Sortea")
                self.etiquetaResultado.config(background="green")

        if int(self.spindbox.get()) == 0:
            self.spindbox.set("1")
            mb.showerror("Cuidad",
                         "Elija un numero distinto a 0")


aplicacion = Aplicacion()
