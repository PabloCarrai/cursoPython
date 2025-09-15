"""  
Disponer un listbox con una serie de nombres de frutas. 
Permitir la seleccion solo de uno de ellos. 
Cuando se presione un boton recuperar la fruta seleccionada
y mostrarla en un label.
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-236")
        self.ventana.geometry("400x400")

        self.listbox = tk.Listbox(self.ventana)
        self.listbox.grid(column=0, row=0)

        self.listbox.insert(0, "papa")
        self.listbox.insert(1, "manzana")
        self.listbox.insert(2, "sandia")
        self.listbox.insert(3, "naranja")
        self.listbox.insert(4, "pera")
        self.listbox.insert(5, "melon")

        self.boton1 = ttk.Button(
            self.ventana, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)

        self.label1 = ttk.Label(self.ventana, text="Seleccionado")
        self.label1.grid(column=0, row=2)
        self.ventana.mainloop()

    def recuperar(self):
        if (len(self.listbox.curselection())!= 0):
            self.label1.configure(text=self.listbox.get(
                self.listbox.curselection()[0]))


aplicacion = Aplicacion()
