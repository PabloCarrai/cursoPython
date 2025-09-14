""" 
Solicitar el ingreso del nombre de una persona y seleccionar
de un control listbox un pais. Al presionar sobre un boton
mostrar en la barra de la ventana el nombre ingresado y 
el pais seleccionado
"""

import tkinter as tk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        #   Vamos con el label del nombre
        self.nombreLabel = tk.Label(self.ventana, text="Nombre:")
        self.nombreLabel.grid(column=0, row=0)
        #   Vamos con la entrada del nombre
        self.valorEntrada = tk.StringVar()
        self.entradaNombre = tk.Entry(
            self.ventana, textvariable=self.valorEntrada)
        self.entradaNombre.grid(column=1, row=0)

        #   Label del listbox
        self.etiquetapais = tk.Label(self.ventana, text="Pais")
        self.etiquetapais.grid(column=0, row=2)

        #   Creo la scrollbar
        self.scrollbar1 = tk.Scrollbar(self.ventana, orient=tk.VERTICAL)

        # Un listbox que permite multiple seleccion(selectmode=tk.MULTIPLE)
        self.listbox1 = tk.Listbox(
            self.ventana, yscrollcommand=self.scrollbar1.set, height=3)  # agregamos la barra scroll
        self.listbox1.grid(column=1, row=2)

        self.listbox1.insert(0, "Paraguay")
        self.listbox1.insert(1, "Uruguay")
        self.listbox1.insert(2, "Chile")
        self.listbox1.insert(3, "Argentina")

        #   configurar con el listbox
        self.scrollbar1.config(command=self.listbox1.yview)
        #   Se lo agrega a la derecha del listbox
        self.scrollbar1.grid(column=2, row=2, sticky="NS")

        self.boton = tk.Button(
            self.ventana, text="Registrar", command=self.cambiarTitulo)
        self.boton.grid(column=0, row=3)

        self.ventana.mainloop()

    def cambiarTitulo(self):
        pais = ""
        for elegido in self.listbox1.curselection():
            pais = self.listbox1.get(elegido)
        pais = f"{self.valorEntrada.get()} - {pais}"
        self.ventana.title(pais)


aplicacion = Aplicacion()
