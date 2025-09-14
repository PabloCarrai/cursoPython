"""  
Ingresar el nombre del usuario y clave en controles del tipo entry.
Si se ingresa las cadenas(usuario:juan clave:abc123) luego mostrar
en el titulo de la ventana el mensaje "Correcto" en caso contrario
mostrar el mensaje "Incorrecto"
utilizar widgets del modulo ttk
"""


import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-233")

        self.label1 = ttk.Label(self.ventana, text="Nombre:")
        self.label1.grid(column=0, row=0)

        self.dato1 = tk.StringVar()

        self.entry1 = ttk.Entry(self.ventana, width=30,
                                textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.label2 = ttk.Label(self.ventana, text="Clave")
        self.label2.grid(column=0, row=1)

        self.dato2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.ventana, width=30,
                                textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)

        self.boton1 = ttk.Button(
            self.ventana, text="ingresar", command=self.ingresar)
        self.boton1.grid(column=0, row=2)

        self.ventana.mainloop()

    def ingresar(self):
        if (self.dato1.get() == "juan" and self.dato2.get() == "abc123"):
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")


aplicacion = Aplicacion()
