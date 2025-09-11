""" 
Confeccionar un programa que permita ingresar
dos numeros en controles de tipo entry. Luego
sumar los dos valores ingresados y mostrar 
dicha suma en un label al presionar un boton
"""
import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x400")

        self.labelprimernumero = tk.Label(
            self.ventana, text="Primer Numero").grid(column=0, row=0)
        self.datoprimernumero = tk.StringVar()
        self.entryprimernumero = tk.Entry(self.ventana, width=10,
                                          textvariable=self.datoprimernumero).grid(column=1, row=0)

        self.labelsegundonumero = tk.Label(
            self.ventana, text="Segundo Numero").grid(column=0, row=2)
        self.datosegundonumero = tk.StringVar()
        self.entrysegundonumero = tk.Entry(self.ventana, width=10,
                                           textvariable=self.datosegundonumero).grid(column=1, row=2)

        self.boton = tk.Button(self.ventana, text="Sumar",
                               command=self.sumarDosNumeros).grid(column=0, row=3)

        self.labelResultado = tk.Label(
            self.ventana, text="Resultado")
        #   En los label tengo que hacer el grid de esta forma sino da error
        self.labelResultado.grid(column=1, row=3)

        self.ventana.mainloop()

    def sumarDosNumeros(self):
        primernumero = int(self.datoprimernumero.get())
        segundonumero = int(self.datosegundonumero.get())
        suma = primernumero+segundonumero
        self.labelResultado.configure(text=suma)


aplicacion = Aplicacion()
