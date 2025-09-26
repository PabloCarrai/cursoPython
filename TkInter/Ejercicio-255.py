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
        suma = valor1+valor2+valor3
        largo1 = valor1*500/suma
        largo2 = valor2*500/suma
        largo3 = valor3*500/suma
        porc1 = valor1/suma*100
        porc2 = valor2/suma*100
        porc3 = valor3/suma*100

        self.canvas1.create_rectangle(10, 200, 10+largo1, 260, fill="red")
        self.canvas1.create_text(50, 220, text="{0:.2f}".format(
            porc1)+"%", fill="white", font="Arial")

        self.canvas1.create_rectangle(
            10+largo1, 200, 10+largo1+largo2, 260, fill="green")
        self.canvas1.create_text(50+largo1, 220, text="{0:.2f}".format(
            porc2)+"%", fill="white", font="Arial")

        self.canvas1.create_rectangle(
            10+largo1+largo2, 200, 10+largo1+largo2+largo3, 260, fill="blue")
        self.canvas1.create_text(50+largo1+largo2, 220, text="{0:.2f}".format(
            porc3)+"%", fill="white", font="Arial")


aplicacion = Aplicacion()
