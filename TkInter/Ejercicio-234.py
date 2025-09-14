import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-234")

        self.seleccion = tk.IntVar()

        self.seleccion.set(2)

        self.radio1 = ttk.Radiobutton(
            self.ventana, text="Varon", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)

        self.radio2 = ttk.Radiobutton(
            self.ventana, text="Mujer", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)

        self.boton = ttk.Button(
            self.ventana, text="Mostrar Seleccionado", command=self.mostrarseleccionado)
        self.boton.grid(column=0, row=2)

        self.label1 = ttk.Label(self.ventana, text="Opcion seleccionada ")
        self.label1.grid(column=0, row=3)

        self.ventana.mainloop()

    def mostrarseleccionado(self):
        if self.seleccion.get() == 1:
            self.label1.configure(text="Opcion Seleccionada Varon")
        else:
            if self.seleccion.get() == 2:
                self.label1.configure(text="Opcion Seleccionada Mujer")


aplicacion = Aplicacion()
