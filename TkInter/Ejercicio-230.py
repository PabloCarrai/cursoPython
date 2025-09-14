import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-230")

        #   Creo la scrollbar
        self.scrollbar1 = tk.Scrollbar(self.ventana, orient=tk.VERTICAL)

        # Un listbox que permite multiple seleccion(selectmode=tk.MULTIPLE)
        self.listbox1 = tk.Listbox(
            self.ventana, selectmode=tk.MULTIPLE, yscrollcommand=self.scrollbar1.set)  # agregamos la barra scroll
        self.listbox1.grid(column=0, row=0)
        self.listbox1.insert(0, "uva")
        self.listbox1.insert(1, "naranjas")
        self.listbox1.insert(2, "limon")
        self.listbox1.insert(3, "sandia")
        self.listbox1.insert(4, "melon")
        self.listbox1.insert(5, "durazno")
        self.listbox1.insert(6, "peras")
        self.listbox1.insert(7, "anana")
        self.listbox1.insert(8, "radicheta")
        self.listbox1.insert(9, "acelga")
        self.listbox1.insert(10, "tomate")

        #   configurar con el listbox
        self.scrollbar1.config(command=self.listbox1.yview)
        #   Se lo agrega a la derecha del listbox
        self.scrollbar1.grid(column=1, row=0, sticky="NS")

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
