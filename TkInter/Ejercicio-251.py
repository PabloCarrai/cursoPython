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
        self.ventana.geometry("500x650")

        self.scrolledtext = sc.ScrolledText(self.ventana, width=50, height=10)
        self.scrolledtext.grid(column=0, row=0, padx=10, pady=10, sticky="e")

        self.labelframe = tk.LabelFrame(self.ventana, text="Region")
        self.labelframe.grid(column=0, row=5, padx=10, pady=10, sticky="e")

        self.etiquetaDesde = ttk.Label(self.labelframe, text="Desde Fila:")
        self.etiquetaDesde.grid(column=0, row=6, padx=10, pady=10, sticky="e")

        self.datoentradaDesdefila = tk.StringVar()
        self.entradaDesde = ttk.Entry(
            self.labelframe, textvariable=self.datoentradaDesdefila)
        self.entradaDesde.grid(column=1, row=6, padx=10, pady=10, sticky="e")

        self.etiquetadesdeColumna = ttk.Label(
            self.labelframe, text="Desde Columna:")
        self.etiquetadesdeColumna.grid(
            column=0, row=7, padx=10, pady=10, sticky="e")

        self.datoentradaDesdeColumna = tk.StringVar()
        self.entradaDesdeColumna = ttk.Entry(
            self.labelframe, textvariable=self.datoentradaDesdeColumna)
        self.entradaDesdeColumna.grid(
            column=1, row=7, padx=10, pady=10, sticky="e")

        self.etiquedahasta = ttk.Label(
            self.labelframe, text="Hasta Fila:")
        self.etiquedahasta.grid(column=0, row=8, padx=10, pady=10, sticky="e")

        self.datoentradaHastafila = tk.StringVar()
        self.entradaHasta = ttk.Entry(
            self.labelframe, textvariable=self.datoentradaHastafila)
        self.entradaHasta.grid(column=1, row=8, padx=10, pady=10, sticky="e")

        self.etiquetahastacolumna = ttk.Label(
            self.labelframe, text="Hasta Columna")
        self.etiquetahastacolumna.grid(
            column=0, row=9, padx=10, pady=10, sticky="e")

        self.datoentradahastacolumna = tk.StringVar()
        self.entradahastacolumna = ttk.Entry(
            self.labelframe, textvariable=self.datoentradahastacolumna)
        self.entradahastacolumna.grid(
            column=1, row=9, padx=10, pady=10, sticky="e")

        self.botonCopiar = ttk.Button(
            self.labelframe, text="Copiar", command=self.copiar)
        self.botonCopiar.grid(column=1, row=10, padx=10, pady=10, sticky="e")

        self.scrolledtext2 = sc.ScrolledText(self.ventana, width=50, height=10)
        self.scrolledtext2.grid(column=0, row=12, padx=10, pady=10, sticky="e")

        self.ventana.mainloop()

    def copiar(self):
        ifila = self.datoentradaDesdefila.get()
        ffila = self.datoentradaHastafila.get()
        icolumna = self.datoentradaDesdeColumna.get()
        fcolumna = self.datoentradahastacolumna.get()
        datos = self.scrolledtext.get(ifila+"."+icolumna, ffila+"."+fcolumna)
        self.scrolledtext2.delete("1.0", tk.END)
        self.scrolledtext2.insert("1.0", datos)


aplicacion = Aplicacion()
