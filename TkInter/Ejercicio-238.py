""" 
Solicitar el ingreso del nombre de una persona y 
seleccionar de un control combobox un pais. Al 
persionar un boton mostrar en la barra de la ventana
el nombre ingresado y el pais seleccionado
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("250x100")
        self.ventana.title("Ejercicio-238")
        self.etiqueta = ttk.Label(self.ventana, text="Nombre")
        self.etiqueta.grid(column=0, row=0)
        self.entradaNombre = tk.Entry(self.ventana, width=15)
        self.entradaNombre.grid(column=1, row=0)
        self.etiquetaPais = ttk.Label(self.ventana, text="Pais")
        self.etiquetaPais.grid(column=0, row=2)
        #   Almacena la opcion seleccionada del combobox
        self.opcion = tk.StringVar()
        #   Esto tiene que ser una variable local, por eso es sin self
        paises = ("Uruguay", "Paraguay", "Chile",
                  "Argentina", "Colombia", "Venezuela", "Ecuador")
        #   Asocio ventana, ancho, la variable que almacena la opcion y los datos a mostrar(variable local),state="readonly" evita que se agregue texto
        self.combobox1 = ttk.Combobox(
            self.ventana, width=10, textvariable=self.opcion, value=paises, state="readonly")
        #   Para poner una opcion por defecto se usa el current
        self.combobox1.current(0)
        self.combobox1.grid(column=1, row=2)
        self.boton = ttk.Button(
            self.ventana, text="Elegir", command=self.mostrarDatos)
        self.boton.grid(column=0, row=3)
        self.ventana.mainloop()

    def mostrarDatos(self):
        self.ventana.title(
            f"Nombre: {self.entradaNombre.get()} Pais: {self.opcion.get()}")


aplicacion = Aplicacion()
