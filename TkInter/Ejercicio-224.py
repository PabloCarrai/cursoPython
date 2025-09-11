"""
Disponer tres controles tipo RadioButton con
las etiquetas Rojo, Verde y Azul. Cuando se
presione un boton cambiar el color de fondo del
formulario.
Si consideramos que la variable ventana1 es un
objeto Tk, luego si queremos que el fondo sea
de color rojo debemos llamar el metodo configure
y en el parametro bg indicar un string con el
color a activar(red,green o blue)
"""

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        #   Variable que usan los RadioButtos
        self.variableRadioButtons = tk.IntVar()
        #   Seteamos la primer opcion como predeterminada
        self.variableRadioButtons.set(1)
        #   Etiqueta informativa
        self.EtiquetaColores = tk.Label(
            self.ventana, text="Elija un color de Fondo ").grid(column=0, row=0)
        #   RadioButons para rojo
        self.radioButtonsRed = tk.Radiobutton(
            self.ventana, text="Rojo", variable=self.variableRadioButtons, value=1)
        self.radioButtonsRed.grid(column=0, row=1)

        #   RadioButons para verde
        self.radioButtonsGreen = tk.Radiobutton(
            self.ventana, text="Verde", variable=self.variableRadioButtons, value=2)
        self.radioButtonsGreen.grid(column=0, row=2)

        #   RadioButons para Azul
        self.radioButtonsBlue = tk.Radiobutton(
            self.ventana, text="Azul", variable=self.variableRadioButtons, value=3)
        self.radioButtonsBlue.grid(column=0, row=3)

        #   El boton de elegir el fondo
        self.botonElegirFondo = tk.Button(
            self.ventana, text="Cambiar Color", command=self.ElegirColor)
        self.botonElegirFondo.grid(column=0, row=4)

        self.ventana.mainloop()

    def ElegirColor(self):
        if self.variableRadioButtons.get() == 1:
            self.ventana.configure(bg="red")
        if self.variableRadioButtons.get() == 2:
            self.ventana.configure(bg="green")
        if self.variableRadioButtons.get() == 3:
            self.ventana.configure(bg="blue")


aplicacion = Aplicacion()
