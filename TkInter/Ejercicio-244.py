""" 

"""


import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-244.py")
        self.ventana.geometry("400x200")

        self.boton1 = ttk.Button(self.ventana, text="Boton 1")
        #   Fill permite que el boton tome todo el tamaño
        self.boton1.pack(side=tk.TOP, fill=tk.BOTH, ipadx=10, ipady=5)

        self.boton2 = ttk.Button(self.ventana, text="Boton 2")
        self.boton2.pack(side=tk.TOP, fill=tk.BOTH, ipadx=10, ipady=5)

        self.boton3 = ttk.Button(self.ventana, text="Boton 3")
        self.boton3.pack(side=tk.TOP, fill=tk.BOTH, ipadx=10, ipady=5)

        self.boton4 = ttk.Button(self.ventana, text="Boton 4")
        self.boton4.pack(side=tk.LEFT, ipadx=10, ipady=5)

        self.boton5 = ttk.Button(self.ventana, text="Boton 5")
        self.boton5.pack(side=tk.RIGHT, ipadx=10, ipady=5)

        self.boton6 = ttk.Button(self.ventana, text="Boton 6")
        self.boton6.pack(side=tk.RIGHT, ipadx=10, ipady=5)

        self.boton7 = ttk.Button(self.ventana, text="Boton 7")
        self.boton7.pack(side=tk.RIGHT, ipadx=10, ipady=5)

        self.ventana.mainloop()


aplicacion = Aplicacion()
