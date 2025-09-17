""" 
Mostrar en una ventana un control del tipo comobobox
con los dias de la semana. Cuando se presione un boton
actualizar una label con el dia seleccionado. 
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-237-Combobox")
        self.ventana.geometry("350x50")

        self.etiquetaDias = ttk.Label(
            self.ventana, text="Seleccione un dia de la semana")
        self.etiquetaDias.grid(column=0, row=0)

        #   Almacena la opcion seleccionada del combobox
        self.opcion = tk.StringVar()
        #   Esto tiene que ser una variable local, por eso es sin self
        diassemana = ("lunes", "martes", "miercoles",
                      "jueves", "viernes", "sabado", "domingo")
        #   Asocio ventana, ancho, la variable que almacena la opcion y los datos a mostrar(variable local),state="readonly" evita que se agregue texto
        self.combobox1 = ttk.Combobox(
            self.ventana, width=10, textvariable=self.opcion, value=diassemana, state="readonly")

        #   Para poner una opcion por defecto se usa el current
        self.combobox1.current(0)
        self.combobox1.grid(column=1, row=0)
        self.boton = tk.Button(self.ventana, text="Elegir",
                               command=self.mostrarEleccion)
        self.boton.grid(column=0, row=2)
        self.etiqueta = tk.Label(self.ventana, text="Eleccion")
        self.etiqueta.grid(column=1, row=2)

        self.ventana.mainloop()

    def mostrarEleccion(self):
        self.etiqueta.configure(text=self.opcion.get())
        # messagebox.showinfo(message=self.opcion.get(), title="The chosen one")


aplicacion = Aplicacion()
