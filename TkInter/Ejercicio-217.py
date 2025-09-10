""" 
Mostrar los botones del 1 al 5. Cuando se preciona
mostrar en una label todos los botones precionados
hasta ese entonces. 
"""

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.botonesPrecionados = ""
        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana, text=self.botonesPrecionados)
        self.label1.grid(column=0, row=6)

        #   Botones
        self.boton1 = tk.Button(
            text="Boton-1", command=self.anotarBoton1)
        self.boton1.grid(column=0, row=1)

        self.boton2 = tk.Button(
            text="Boton-2", command=self.anotarBoton2)
        self.boton2.grid(column=1, row=1)

        self.boton3 = tk.Button(
            text="Boton-3", command=self.anotarBoton3)
        self.boton3.grid(column=2, row=1)

        self.boton4 = tk.Button(
            text="Boton-4", command=self.anotarBoton4)
        self.boton4.grid(column=3, row=1)

        self.boton5 = tk.Button(
            text="Boton-5", command=self.anotarBoton5)
        self.boton5.grid(column=4, row=1)

        self.ventana.mainloop()

    def anotarBoton1(self):
        self.botonesPrecionados = self.botonesPrecionados+"Boton-1"
        self.label1.config(text=self.botonesPrecionados)

    def anotarBoton2(self):
        self.botonesPrecionados = self.botonesPrecionados+"Boton-2"
        self.label1.config(text=self.botonesPrecionados)

    def anotarBoton3(self):
        self.botonesPrecionados = self.botonesPrecionados+"Boton-3"
        self.label1.config(text=self.botonesPrecionados)

    def anotarBoton4(self):
        self.botonesPrecionados = self.botonesPrecionados+"Boton-4"
        self.label1.config(text=self.botonesPrecionados)

    def anotarBoton5(self):
        self.botonesPrecionados = self.botonesPrecionados+"Boton-5"
        self.label1.config(text=self.botonesPrecionados)


aplicacion = Aplicacion()
