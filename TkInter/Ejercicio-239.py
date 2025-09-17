""" 
Confeccionar una aplicacion que muestre
dos opciones en el menu de barra superior. 
La primer opcion despliega un submenu que 
permite cambiar el color de fondo del formulario
y la segunda permite cambiar el tamaño del formulario
"""

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("250x100")
        self.ventana.title("Ejercicio-239")
        #   Menues
        menubar1 = tk.Menu(self.ventana)  # Este seria el menu
        # A la ventana le defino el menu menubar1
        self.ventana.config(menu=menubar1)
        # Creo otro menu(SubMenu) con el nombre opciones1 tearoff=0(evita separar el menu,linea punteada)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        # Agrego los items al menu opciones1
        opciones1.add_command(label="Rojo", command=self.fijarRojo)
        #   Agregar linea separadora
        opciones1.add_separator()
        # Agrego los items al menu opciones1
        opciones1.add_command(label="Verde", command=self.fijarVerde)
        # Agrego los items al menu opciones1
        opciones1.add_command(label="Azul", command=self.fijarAzul)
        # agregar teclas acceso rapido
        self.ventana.bind_all("<Control-r>", self.cambiar)
        # Agrego submenu(menubar1)
        menubar1.add_cascade(label="Colores", menu=opciones1)
        #   Aca vamos con el otro menu, tamaño
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaño", menu=opciones2)
        self.ventana.mainloop()

    def fijarRojo(self):
        self.ventana.configure(background="red")

    def fijarVerde(self):
        self.ventana.configure(background="green")

    def fijarAzul(self):
        self.ventana.configure(background="blue")

    def ventanachica(self):
        self.ventana.geometry("640x480")

    def ventanagrande(self):
        self.ventana.geometry("1024x800")

    def cambiar(self, event):
        if event.keysym == "r":
            self.fijarRojo()


aplicacion = Aplicacion()
