""" 
Confeccionar una aplicacion que permita ingresar
dos valores enteros y al presionar un boton nos 
muestre la suma en el titulo de la ventana. 
Si el operador no ingresa alguno de los dos 
controles Entry datos informar mediante
un dialogo el error que se esta comentiendo
Agregar ademas u menu de opciones que al ser
seleccionado nos muestre informacion del programa
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-247.py")
        self.ventana.geometry("400x250")

        barra_menu = tk.Menu()
        menu_opciones = tk.Menu(barra_menu, tearoff=False)
        barra_menu.add_cascade(menu=menu_opciones, label="Opciones")
        self.ventana.config(menu=barra_menu)
        menu_opciones.add_command(
            label="Acerca de...",
            command=self.acercade
        )

        self.labelframesumanumeros = tk.LabelFrame(
            self.ventana, text="Suma de los numeros:")
        self.labelframesumanumeros.grid(column=0, row=0, ipadx=10, ipady=10)

        self.labelnumero1 = tk.Label(
            self.labelframesumanumeros, text="Ingrese primer valor:")
        self.labelnumero1.grid(column=0, row=0, ipadx=5, ipady=5, sticky="e")

        self.entrynumero1 = tk.Entry(self.labelframesumanumeros)
        self.entrynumero1.grid(column=1, row=0, ipadx=5, ipady=5)

        self.labelnumero2 = tk.Label(
            self.labelframesumanumeros, text="Ingrese segundo valor:")
        self.labelnumero2.grid(column=0, row=2, ipadx=5, ipady=5)

        self.entrynumero2 = tk.Entry(self.labelframesumanumeros)
        self.entrynumero2.grid(column=1, row=2, ipadx=5, ipady=5)

        self.botonsuma = tk.Button(
            self.labelframesumanumeros, text="Sumar", command=self.sumar)
        self.botonsuma.grid(column=1, row=3, ipadx=5, ipady=5, sticky="we")

        self.ventana.mainloop()

    def sumar(self):
        if (len(self.entrynumero1.get()) == 0 or len(self.entrynumero2.get()) == 0):
            messagebox.showerror(
                "Cuidado", "No se puede dejar los cuadros de entradas de numeros vacios")
        else:
            self.ventana.title(
                f"La suma de {self.entrynumero1.get()} y {self.entrynumero2.get()} es {int(self.entrynumero1.get())+int(self.entrynumero2.get())}")

    def acercade(self):
        messagebox.showinfo(
            "Informacion", "Este programa fue desarrollado para el aprendizaje de python y tkinter")


aplicacion = Aplicacion()
