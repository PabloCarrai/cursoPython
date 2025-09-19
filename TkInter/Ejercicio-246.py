

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-246.py")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0, 0)

        self.botonConfirmar = ttk.Button(self.ventana, text="Confirmar")
        self.botonConfirmar.place(x=680, y=550, width=90, height=30)

        self.botonCancelar = ttk.Button(self.ventana, text="Cancelar")
        self.botonCancelar.place(x=580, y=550, width=90, height=30)

        self.ventana.mainloop()


aplicacion = Aplicacion()
