""" 
Mediante dos controles de tipo Entry permitir el ingreso de dos numeros. 
Crear un menu que contenga una opcion que cambie el tamaño de la ventana
con los valores ingresados por teclado. Finalmente disponer otra opcion
que finalice el programa
"""

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-240")
        self.ventana.geometry("250x100")

        self.etiquetaaltura = tk.Label(self.ventana, text="Altura")
        self.etiquetaaltura.grid(column=0, row=0)

        self.entradaaltura = tk.Entry(self.ventana, width=10)
        self.entradaaltura.grid(column=1, row=0)

        self.etiquetaancho = tk.Label(self.ventana, text="Ancho")
        self.etiquetaancho.grid(column=0, row=1)

        self.entradaancho = tk.Entry(self.ventana, width=10)
        self.entradaancho.grid(column=1, row=1)

        #   Menu
        barra_menu = tk.Menu(self.ventana)
        menu_Pantalla = tk.Menu(barra_menu, tearoff=False)
        menu_Pantalla.add_command(
            label="Cambiar Tamaño de Ventana",
            command=self.modificarPantalla
        )
        menu_Pantalla.add_separator()
        menu_Pantalla.add_command(label="Salir", command=self.ventana.destroy)
        barra_menu.add_cascade(menu=menu_Pantalla, label="Pantalla")
        self.ventana.config(menu=barra_menu)

        self.ventana.mainloop()

    def modificarPantalla(self):
        self.ventana.geometry(
            f"{self.entradaaltura.get()}x{self.entradaancho.get()}")


aplicacion = Aplicacion()
