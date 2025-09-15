"""  
Mostrar una ventana y en su interior tres controles de tipo
checkbuton cuya etiquetas correspondan a distintos lenguajes de programacion. 
Cuando se presione un boton mostrar en una label la cantidad de checkbutton
que se encuentran chequeados. Utilizar widget del modulo ttk
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-235")
        self.ventana.geometry("400x400")

        self.seleccion1 = tk.IntVar()

        self.check1 = ttk.Checkbutton(
            self.ventana, text="Python", variable=self.seleccion1)
        self.check1.grid(column=0, row=0)

        self.seleccion2 = tk.IntVar()
        self.check2 = ttk.Checkbutton(
            self.ventana, text="C++", variable=self.seleccion2)
        self.check2.grid(column=0, row=1)

        self.seleccion3 = tk.IntVar()
        self.check3 = ttk.Checkbutton(
            self.ventana, text="Java", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)

        self.boton1 = ttk.Button(
            self.ventana, text="Verificar", command=self.verificar)
        self.boton1.grid(column=0, row=3)

        self.label1 = ttk.Label(self.ventana, text="Cantidad de lenguajes")
        self.label1.grid(column=0, row=4)

        self.ventana.mainloop()

    def verificar(self):
        cant = 0
        if self.seleccion1.get() == 1:
            cant += 1
        if self.seleccion2.get() == 1:
            cant += 1
        if self.seleccion3.get() == 1:
            cant += 1

        self.label1.configure(text=f"Cantidad {cant}")

        pass


aplicacion = Aplicacion()
