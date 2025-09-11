"""  
Disponer dos controles de tipo Entry para el ingreso de enteros. 
Mediante dos controles radiobutton permitir seleccionar si queremos
sumarlos o restarlos. Al precionar un boto mostrar el resultado
de la operacion seleccionada
"""

import tkinter as tk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()

        #   Etiqueta primer entero
        self.etiquetaprimerentero = tk.Label(
            self.ventana, text="Primer Entero")
        self.etiquetaprimerentero.grid(column=0, row=0)

        self.datoprimernumero = tk.StringVar()
        #   Primer entrada
        self.primerEntero = tk.Entry(
            self.ventana, width=15, textvariable=self.datoprimernumero)
        self.primerEntero.grid(column=1, row=0)
        #   Etiqueta del segundo entero
        self.etiquetasegundoentero = tk.Label(
            self.ventana, text="Segundo Entero")
        self.etiquetasegundoentero.grid(column=0, row=1)

        self.datosegundonumero = tk.StringVar()
        #   Entrada del segundo entero
        self.segundoEntero = tk.Entry(
            self.ventana, width=15, textvariable=self.datosegundonumero)
        self.segundoEntero.grid(column=1, row=1)

        #   IntVar de los radiobutons
        self.seleccion = tk.IntVar()
        #   Elijo la dos por defecto
        self.seleccion.set(2)
        #   Primer radiobutton
        self.radio1 = tk.Radiobutton(
            self.ventana, text="Sumar", variable=self.seleccion, value=1)
        #   Lo agregamos al grid
        self.radio1.grid(column=1, row=4)
        #   Segundo radiobutton
        self.radio2 = tk.Radiobutton(
            self.ventana, text="Restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=5)
        #   Boton
        self.boton = tk.Button(
            self.ventana, text="Operar", command=self.operar).grid(column=0, row=3)
        #   Label del resultado de la operacion
        self.labelResultado = tk.Label(self.ventana, text="resultado")
        self.labelResultado.grid(column=0, row=5)
        self.ventana.mainloop()

    def operar(self):
        #   Genero variables en donde obtengo lo que haya en los entry
        primervalor = int(self.datoprimernumero.get())
        segundovalor = int(self.datosegundonumero.get())
        #   Hago las operaciones
        suma = primervalor+segundovalor
        resta = primervalor-segundovalor
        #   chequeo la seleccion y en base a eso seteo el resultado al label
        if self.seleccion.get() == 1:
            self.labelResultado.configure(text=suma)
        else:
            if self.seleccion.get() == 2:
                self.labelResultado.configure(text=resta)


aplicacion = Aplicacion()
