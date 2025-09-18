""" 
Confeccionar una aplicacin que muestre
dos controles del tipo LabelFrame. 
El primero disponer 2 Label, 2 Entry. 
En el segundo LabelFrame disponer 3
botones
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-242")
        self.ventana.geometry("400x400")

        #   Vamos con el labelframe
        self.labelframe1 = ttk.LabelFrame(self.ventana, text="Login")
        # padx y pady son la separacion entre controles
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #   Armamos el contenido del labelframe usando un metodo
        self.login()

        #   Vamos con el labelframe2
        self.labelframe2 = ttk.LabelFrame(self.ventana, text="Operaciones")
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)
        self.operaciones()

        self.ventana.mainloop()

    def login(self):
        self.label1 = ttk.Label(self.labelframe1, text="Nombre de Usuario")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1 = ttk.Entry(self.labelframe1, width=15)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe1, text="Ingrese Clave")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2 = ttk.Entry(self.labelframe1, width=15, show="*")
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe1, text="Ingresar")
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def operaciones(self):
        self.botonAgregarUsuario = ttk.Button(
            self.labelframe2, text="Agregar Usuario")
        self.botonAgregarUsuario.grid(column=0, row=0, padx=4, pady=4)
        self.botonModificarUsuario = ttk.Button(
            self.labelframe2, text="Modificar Usuario")
        self.botonModificarUsuario.grid(column=1, row=0, padx=4, pady=4)
        self.botonBorrarUsuario = ttk.Button(
            self.labelframe2, text="Borrar Usuario")
        self.botonBorrarUsuario.grid(column=2, row=0, padx=4, pady=4)


aplicacion = Aplicacion()
