"""  
Confacionar un programa que contenga dos controles
de tipo ScrolledText. En el primero ingresamos por teclado
cualquier texto. Mediante 4 controles de tipo entry 
indicar desde que fila y columna hasta que fila y columna
extraer caracteres del primer scrolledText y copiarlo
al segundo ScrolledText cuando se presiona el boton
"""


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as sc


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-251.py")
        self.ventana.geometry("450x500")

        self.scrolledtext = sc.ScrolledText(self.ventana, width=50, height=10)
        self.scrolledtext.grid(column=0, row=0)

        self.labelframe = tk.LabelFrame(self.ventana, text="Region")
        self.labelframe.grid(column=0, row=5)

        self.etiquetaDesde = ttk.Label(self.labelframe, text="Desde Fila:")
        self.etiquetaDesde.grid(column=0, row=6)

        self.datoentradaDesde = tk.StringVar()
        self.entradaDesde = ttk.Entry(self.labelframe,textvariable=self.datoentradaDesde)
        self.entradaDesde.grid(column=1, row=6)

        self.etiquetadesdeColumna = ttk.Label(
            self.labelframe, text="Desde Columna:")
        self.etiquetadesdeColumna.grid(column=0, row=7)

        self.datoentradaDesdeColumna = tk.StringVar()
        self.entradaDesdeColumna = ttk.Entry(self.labelframe,textvariable=self.datoentradaDesdeColumna)
        self.entradaDesdeColumna.grid(column=1, row=7)

        self.etiquedahasta = ttk.Label(
            self.labelframe, text="Hasta Fila:")
        self.etiquedahasta.grid(column=0, row=8)

        self.datoentradaHasta = tk.StringVar()
        self.entradaHasta = ttk.Entry(self.labelframe,textvariable=self.datoentradaHasta)
        self.entradaHasta.grid(column=1, row=8)

        self.ventana.mainloop()


aplicacion = Aplicacion()
