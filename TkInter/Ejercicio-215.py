""" 
Mostrar dos Label, en una se muestra el nombre del programa
y en la segunda el año de creacion. Disponer un boton para 
finalizar el programa. 
No permitir al usuario redimensionar la ventana
"""
#   Importo tkinter
import tkinter as tk
#   Importo sys
import sys


class Aplicacion:
    def __init__(self):
        #   Creamos la ventana principal
        self.ventana1 = tk.Tk()
        #   Agregamos titulo
        self.ventana1.title("Ejercicio")
        #   Creamos el label seteamos texto
        self.label1 = tk.Label(self.ventana1, text="Sistema de facturacion")
        #   Ubicamos el label en la columna y fila 0
        self.label1.grid(column=0, row=0)
        #   Creamos el label 2 con su titulo
        self.label2 = tk.Label(self.ventana1, text="2025")
        #   Seteamos su ubicacion columna 0 fila 1
        self.label2.grid(column=0, row=1)
        #   Creamos el boton y agregamos texto y unimos al comando que tenemos que crear self.finalizar(metodo)
        self.boton1 = tk.Button(
            self.ventana1, text="Finalizar", command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        #   Con esto evitamos que se cambie el tamaño de la ventana
        self.ventana1.resizable(False, False)
        self.ventana1.mainloop()

    def finalizar(self):
        #   Con esto finalizo el programa
        sys.exit(0)


aplicacion = Aplicacion()
