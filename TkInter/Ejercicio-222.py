"""  
Mostrar dos controles de tipo RadioButton con las etiqueta
"Varon" y "Mujer", cuando se presione un boton actualizar
una label con el radiobuton Seleccionado
"""
import tkinter as tk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()

        #   Esto es necesario para  radiobutton(para ambos radiobuton se usa el mismo)
        self.seleccion = tk.IntVar()
        #   Esto es la seleccion por defecto
        self.seleccion.set(2)
        #   El radiobuton de Varon
        self.radio1 = tk.Radiobutton(
            self.ventana, text="Varon", variable=self.seleccion, value=1)
        #   Lo agregamos al grid
        self.radio1.grid(column=0, row=0)
        #   Esto es el otro radiobutton Mujer
        self.radio2 = tk.Radiobutton(
            self.ventana, text="Mujer", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)

        self.boton = tk.Button(
            self.ventana, text="Mostrar Seleccionado", command=self.mostrarSeleccionado).grid(column=0, row=3)

        self.labelResultado = tk.Label(self.ventana, text="Opcion")
        self.labelResultado.grid(column=0, row=4)
        self.ventana.mainloop()

    def mostrarSeleccionado(self):
        if self.seleccion.get() == 1:
            self.labelResultado.configure(text="Opcion Seleccionada: Varon")
        else:
            if self.seleccion.get() == 2:
                self.labelResultado.configure(
                    text="Opcion Seleccionada: Mujer")


aplicacion = Aplicacion()
