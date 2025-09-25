import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.labelframe = tk.LabelFrame(
            self.ventana, text="Partidos politicos:")
        self.labelframe.grid(column=0, row=0)

        self.labelPartidoA = tk.Label(self.labelframe, text="Partido A:")
        self.labelPartidoA.grid(column=0, row=0, padx=10, pady=10)

        self.datoEntradaPartidoA = tk.StringVar()
        self.entradaPartidoA = tk.Entry(
            self.labelframe, textvariable=self.datoEntradaPartidoA)
        self.entradaPartidoA.focus()
        self.entradaPartidoA.grid(column=1, row=0, padx=10, pady=10)

        self.labelPartidoB = tk.Label(self.labelframe, text="Partido B:")
        self.labelPartidoB.grid(column=0, row=1, padx=10, pady=10)

        self.datoEntradaPartidoB = tk.StringVar()
        self.entradaPartidoB = tk.Entry(
            self.labelframe, textvariable=self.datoEntradaPartidoB)
        self.entradaPartidoB.grid(column=1, row=1, padx=10, pady=10)

        self.labelPartidoC = tk.Label(self.labelframe, text="Partido C:")
        self.labelPartidoC.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaPartidoC = tk.StringVar()
        self.entradaPartidoC = tk.Entry(
            self.labelframe, textvariable=self.datoEntradaPartidoC)
        self.entradaPartidoC.grid(column=1, row=2, padx=10, pady=10)

        self.boton = tk.Button(
            self.labelframe, text="Generar Grafico", command=self.generarGrafico)
        self.boton.grid(column=0, row=3, columnspan=2,
                        padx=10, pady=10, sticky="we")

        self.canvas1 = tk.Canvas(
            self.ventana, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1, padx=10, pady=10)

        self.ventana.mainloop()

    def generarGrafico(self):
        self.canvas1.delete(tk.ALL)
        valor1 = int(self.datoEntradaPartidoA.get())
        valor2 = int(self.datoEntradaPartidoB.get())
        valor3 = int(self.datoEntradaPartidoC.get())
        if valor1 > valor2 and valor1 > valor3:
            mayor = valor1
        else:
            if valor2 > valor3:
                mayor = valor2
            else:
                mayor = valor3
        largo1 = valor1/mayor*400
        largo2 = valor2/mayor*400
        largo3 = valor3/mayor*400
        self.canvas1.create_rectangle(10, 10, 10+largo1, 90, fill="red")
        self.canvas1.create_rectangle(10, 120, 10+largo2, 200, fill="blue")
        self.canvas1.create_rectangle(10, 230, 10+largo3, 310, fill="green")
        self.canvas1.create_text(
            largo1+70, 50, text="Partido A", fill="white", font="Arial")
        self.canvas1.create_text(
            largo2+70, 160, text="Partido B", fill="white", font="Arial")
        self.canvas1.create_text(
            largo3+70, 270, text="Partido C", fill="white", font="Arial")


aplicacion = Aplicacion()
