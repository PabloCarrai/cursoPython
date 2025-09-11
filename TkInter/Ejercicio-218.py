""" 
Confeccionar una aplicacion que permita ingresar
un entero por teclado y al presionar sobre un boton
muestre dicho valor al cuadrado en una label
"""
import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba de control entry")
        self.label = tk.Label(
            self.ventana, text="Ingrese un numero").grid(row=0, column=0)
        #   Esto lo necesita el entry(Almacena el dato)
        self.dato = tk.StringVar()
        #   Esto es lo del entry
        self.entry1 = tk.Entry(self.ventana, width=10,
                               textvariable=self.dato).grid(column=0, row=1)
        self.boton = tk.Button(self.ventana, text="Calcular Cuadrado",
                               command=self.calcularcuadrado).grid(column=0, row=2)

        self.label2 = tk.Label(
            self.ventana, text="Resultado")
        #   El grid en el label hay que hacerlo por separado sino devuelve NoneType
        self.label2.grid(column=0, row=3)
        self.ventana.mainloop()

    def calcularcuadrado(self):
        # Transformo en entero a datos y uso el get para obtener ese dato
        # Esto devuelve un string por eso usamos el int()
        valor = int(self.dato.get())
        #   Hago el calculo
        cuadrado = valor*valor
        #   Se lo paso al label
        self.label2.configure(text=cuadrado)


aplicacion = Aplicacion()
