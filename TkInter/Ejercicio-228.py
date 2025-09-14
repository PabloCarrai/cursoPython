"""  
Disponer un listbox con una serie de nombres de frutas. 
Permitir la seleccion solo de uno de ellos. Cuando se presione
un boton recuperar la fruta seleccionada y mostrarla en una
label
"""


import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        #   Creo el listbox
        self.listbox1 = tk.Listbox(self.ventana)
        #   Lo ubico
        self.listbox1.grid(column=0, row=0)
        #   Asi agrego elementos
        self.listbox1.insert(0, "papas")
        self.listbox1.insert(1, "manzana")
        self.listbox1.insert(2, "melon")
        self.listbox1.insert(3, "naranja")
        self.listbox1.insert(4, "uvas")
        self.listbox1.insert(5, "cereza")

        self.label = tk.Label(self.ventana, text="Seleccionados")
        self.label.grid(column=0, row=1)

        self.boton = tk.Button(
            self.ventana, text="Recuperar", command=self.recuperar)
        self.boton.grid(column=0, row=2)

        self.ventana.mainloop()

    def recuperar(self):
        #   curselection devuelve cantidad de elementos seleccionados en el listbox
        if (len(self.listbox1.curselection()) != 0):
            #   Recupera una tupla y solo necesito el primer elemento por eso el 0
            self.label.configure(text=self.listbox1.get(
                self.listbox1.curselection()[0]))


aplicacion = Aplicacion()
