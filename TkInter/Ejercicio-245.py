import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-245.py")
        self.ventana.geometry("400x200")

        self.boton1 = ttk.Button(self.ventana, text="Boton 1")
        self.boton1.grid(column=0, row=0)

        self.boton2 = ttk.Button(self.ventana, text="Boton 2")
        self.boton2.grid(column=1, row=0)

        self.boton3 = ttk.Button(self.ventana, text="Boton 3")
        # ocupa dos filas y se expande al norte y sur
        self.boton3.grid(column=2, row=0, rowspan=2, sticky="ns")

        self.boton4 = ttk.Button(self.ventana, text="Boton 4")
        self.boton4.grid(column=0, row=1)

        self.boton5 = ttk.Button(self.ventana, text="Boton 5")
        self.boton5.grid(column=1, row=1)

        self.boton6 = ttk.Button(self.ventana, text="Boton 6")
        self.boton6.grid(column=0, row=2, columnspan=3,
                         sticky="we")  # se expande entre columnas este oeste en sticky

        self.ventana.mainloop()


aplicacion = Aplicacion()
