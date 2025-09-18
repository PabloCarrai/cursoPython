""" 
Confeccionar una aplicacion que muestre un cuaderno con tres pestañas. 
Los titulos de cada pestaña deben ser Button Label y Entry. Segun la 
pestaña mostrar un mensaje informando el objeto de la clase y un 
ejemplo de la misma.
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x400")
        self.ventana.title("Ejercicio-241")

        #   Creo el cuaderno y lo asocio a la ventana
        self.cuaderno1 = ttk.Notebook(self.ventana)
        #   Creo el frame y lo asocio al cuaderno
        self.pagina1 = ttk.Frame(self.cuaderno1)
        #   Al cuaderno le asocio la pagina
        self.cuaderno1.add(self.pagina1, text="button")

        #   El contenido se asocia a la pagina del cuaderno
        self.label1 = ttk.Label(
            self.pagina1, text="la clase button nos permite capturar el clic y lanzar un evento")
        self.label1.grid(column=0, row=0)
        self.boton1 = ttk.Button(self.pagina1, text="Ejemplo de boton")
        self.boton1.grid(column=0, row=1)
        self.boton2 = ttk.Button(
            self.pagina1, text="Ejemplo de boton inactivo", state="disabled")
        self.boton2.grid(column=0, row=2)

        #   segundo frame
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Label")
        self.label2 = ttk.Label(
            self.pagina2, text="La clase label permite mostrar un mensaje")
        self.label2.grid(column=0, row=0)

        self.label3 = ttk.Label(
            self.pagina2, text="Se puede hacer un salto de linea dentro del label")
        self.label3.grid(column=0, row=1)

        #   Otra pagina
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Entry")
        self.label4 = ttk.Label(
            self.pagina3, text="En tkinter el control de entrada por teclado se llama entry")
        self.label4.grid(column=0, row=0)

        self.entry1 = ttk.Entry(self.pagina3, width=30)
        self.entry1.grid(column=0, row=1)

        self.cuaderno1.grid(column=0, row=0)

        self.ventana.mainloop()


aplicacion = Aplicacion()
