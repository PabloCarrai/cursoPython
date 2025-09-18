""" 
Armar visual de acuerdo al video
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-243")
        self.ventana.geometry("400x200")

        #   Vamos con el labelframe
        self.labelframe1 = ttk.LabelFrame(self.ventana, text="Articulos:")
        # padx y pady son la separacion entre controles
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        #   Objetos del primer labelframe.
        #       Etiqueta codigo de articulo
        self.etiquetaCodigoArticulo = ttk.Label(
            self.labelframe1, text="Codigo de articulo")
        self.etiquetaCodigoArticulo.grid(column=0, row=0, padx=4, pady=4)
        #       Entraada codigo de articulo
        self.entradaCodigoArticulo = ttk.Entry(self.labelframe1, width=20)
        self.entradaCodigoArticulo.grid(column=1, row=0, padx=4, pady=4)
        #       Etiqueta Descripcion
        self.etiquetaDescripcion = ttk.Label(
            self.labelframe1, text="Descripcion:")
        self.etiquetaDescripcion.grid(column=0, row=1, padx=4, pady=4)
        #       Entrada Descripcion
        self.entradaDescripcion = ttk.Entry(
            self.labelframe1, width=20)
        self.entradaDescripcion.grid(column=1, row=1, padx=4, pady=4)
        #       Etiqueta Precio
        self.etiquetaPrecio = ttk.Label(self.labelframe1, text="Precio")
        self.etiquetaPrecio.grid(column=0, row=2, padx=4, pady=4)
        #       Entrada Precio
        self.entradaPrecio = ttk.Entry(self.labelframe1, width=20)
        self.entradaPrecio.grid(column=1, row=2, padx=4, pady=4)

        #   Vamos con el labelframe2
        self.labelframe2 = ttk.LabelFrame(self.ventana, text="Operaciones")
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)
        #   Contenido del labelframe2
        #       boton Alta
        self.botonAlta = ttk.Button(self.labelframe2, text="Alta")
        self.botonAlta.grid(column=0, row=0, padx=4, pady=4)

        #       boton Baja
        self.botonBaja = ttk.Button(self.labelframe2, text="Baja")
        self.botonBaja.grid(column=1, row=0, padx=4, pady=4)

        #       boton Modificacion
        self.botonModificacion = ttk.Button(
            self.labelframe2, text="Modificacion")
        self.botonModificacion.grid(column=2, row=0, padx=4, pady=4)

        self.ventana.mainloop()


aplicacion = Aplicacion()
