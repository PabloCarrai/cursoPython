""" 
Disponer de un listbox con una serie de nombres de frutas. 
Permitir la seleccion de varias frutas. 
Cuando se presione un boton recuperar
todas las frutas seleccionarlas y mostrarlas
en un label
"""


import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-229")
        # Un listbox que permite multiple seleccion(selectmode=tk.MULTIPLE)
        self.listbox1 = tk.Listbox(self.ventana, selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0, row=0)
        self.listbox1.insert(0, "uva")
        self.listbox1.insert(1, "naranjas")
        self.listbox1.insert(2, "limon")
        self.listbox1.insert(3, "sandia")
        self.listbox1.insert(4, "melon")
        self.listbox1.insert(5, "durazno")
        self.boton = tk.Button(
            self.ventana, text="Recuperar", command=self.recuperar)
        self.boton.grid(column=0, row=1)
        self.label = tk.Label(self.ventana, text="Seleccionados")
        self.label.grid(column=0, row=2)
        self.ventana.mainloop()

    def recuperar(self):
        if (len(self.listbox1.curselection()) != 0):
            todos = ""
            for posicion in self.listbox1.curselection():
                todos += self.listbox1.get(posicion)+"\n"
            self.label.configure(text=todos)


aplicacion = Aplicacion()
