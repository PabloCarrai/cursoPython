""" 
Confeccionar un programa que permita ingresar
el nombre de usuario en un control entry y 
cuando se presione un boton mostrar el valor
ingresado en la barra de titulo de la ventana
"""
import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x400")
        self.label = tk.Label(
            self.ventana, text="Nombre").grid(column=0, row=0)
        #   Esto lo necesita el entry(Almacena el dato)
        self.dato = tk.StringVar()
        #   Esto es lo del entry
        self.entry1 = tk.Entry(self.ventana, width=20,
                               textvariable=self.dato).grid(column=1, row=0)
        self.boton = tk.Button(self.ventana, text="clic",
                               command=self.cambiarTitulo).grid(column=0, row=1)
        self.ventana.mainloop()

    def cambiarTitulo(self):
        nombre = self.dato.get()
        self.ventana.title(nombre)


aplicacion = Aplicacion()
