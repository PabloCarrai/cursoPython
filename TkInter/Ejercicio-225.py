""" 
Mostrar una ventana y en su interior tres controles
de tipo CheckButton cuya etiquetas correspondan a 
distrintos lenguajes de programacion. Cuando se presione
un boton mostrar en un label la cantidad de checkbutton que 
se encuentran chequeados
"""
import tkinter as tk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()

        #   Este chequea si esta chequeado o no el checkbutton
        #   En estos casos no es una sola variable para todos, es una por checkbutton
        self.seleccion1 = tk.IntVar()
        #   Esto es el checkbutton
        self.check1 = tk.Checkbutton(
            self.ventana, text="Python", variable=self.seleccion1)
        #   Ahora es ubicarlo en la ventana
        self.check1.grid(column=0, row=0)

        #   Este es para el otro checkbutton
        self.seleccion2 = tk.IntVar()
        #   Aca tenemos nuevo checkbutton
        self.check2 = tk.Checkbutton(
            self.ventana, text="C++", variable=self.seleccion2)
        #   lo ubicamos en la pantalla
        self.check2.grid(column=0, row=1)

        #   Este es para otro checkbutton
        self.seleccion3 = tk.IntVar()
        self.check3 = tk.Checkbutton(
            self.ventana, text="Java", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)

        #   Necesitamos un boton
        self.boton1 = tk.Button(
            self.ventana, text="Verificar", command=self.verificar)
        self.boton1.grid(column=0, row=3)

        #   En la etiqueta va el resultado
        self.etiqueta = tk.Label(self.ventana, text="Cantidad")
        self.etiqueta.grid(column=0, row=4)

        self.ventana.mainloop()

    def verificar(self):
        #   Contamos cantidad de seleccion devuelve 1
        cant = 0
        if self.seleccion1.get() == 1:
            cant = cant+1
        if self.seleccion2.get() == 1:
            cant = cant+1
        if self.seleccion3.get() == 1:
            cant = cant+1
        #   Aca agregamos la cantidad como texto
        self.etiqueta.configure(text=f"Cantidad: {cant}")


aplicacion = Aplicacion()
