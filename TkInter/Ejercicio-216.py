""" 
Disponer dos objetos de la clase Button con 
la etiquetas: "varon" y "mujer". al presionarse
mostrar en la barra de titulo de la ventana
la etiqueta del boton presionado
"""

import tkinter as tk


class Aplicacion:
    def __init__(self):
        #   Creo la ventana principal
        self.ventana = tk.Tk()
        #   Creo el primer boton con texto varon y comando
        self.boton1 = tk.Button(
            self.ventana, text="Varon", command=self.mostrarvaron)
        #   Agrego el boton a la columna y fila 0
        self.boton1.grid(column=0, row=0)
        #   Creo el segundo boton
        self.boton2 = tk.Button(
            self.ventana, text="Mujer", command=self.mostrarmujer)
        #   Ubico el mismo en la columna 0 y linea 1
        self.boton2.grid(column=1, row=0)
        #   mantengo en loop la aplicacion
        self.ventana.mainloop()

    #   Aca va el metodo para cambiar el label de la venta la a Varon
    def mostrarvaron(self):
        #   De este modo actualiza el valor en el label
        self.ventana.title("Varon")

    #   Metodo para cambiar el label de la ventana a Mujer
    def mostrarmujer(self):
        #   De este modo actualiza el valor en el label
        self.ventana.title("Mujer")


aplicacion = Aplicacion()
