import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.labelframe = tk.LabelFrame(self.ventana, text="Opciones")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)

        self.botonBorrarLinea = tk.Button(
            self.labelframe, text="Borrar Linea", command=self.borrar_linea)
        self.botonBorrarLinea.grid(column=0, row=0, padx=10, pady=10)

        self.botonBorrarRectangulo = tk.Button(
            self.labelframe, text="Borrar Rectangulo", command=self.borrar_rectangulo)
        self.botonBorrarRectangulo.grid(column=1, row=0, padx=10, pady=10)

        self.botonBorrarOvalo = tk.Button(
            self.labelframe, text="Borrar Ovalo", command=self.borrar_ovalo)
        self.botonBorrarOvalo.grid(column=2, row=0, padx=10, pady=10)

        self.botonBorrarTodosCuadrados = tk.Button(
            self.labelframe, text="Borrar todos los cuadrados", command=self.borrar_cuadrados)
        self.botonBorrarTodosCuadrados.grid(column=3, row=0, padx=10, pady=10)

        self.botonBorrarTodos = tk.Button(
            self.labelframe, text="Borrar Todo", command=self.borrar_todos)
        self.botonBorrarTodos.grid(column=4, row=0, padx=10, pady=10)

        self.canvas1 = tk.Canvas(
            self.ventana, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1, padx=10, pady=10)
        #   El identificador es self.linea, de la linea
        self.linea = self.canvas1.create_line(0, 0, 100, 50, fill="white")
        #   El identificador del ovalo
        self.ovalo = self.canvas1.create_oval(400, 10, 500, 150, fill="red")
        #   El Identificador del rectangulo
        self.rectangulo = self.canvas1.create_rectangle(
            150, 10, 300, 110, fill="white")

        #   van los rectangulos
        self.canvas1.create_rectangle(
            100, 300, 150, 350, fill="#aaaaaa", tags="cuadrado")
        self.canvas1.create_rectangle(
            200, 300, 250, 350, fill="#555555", tags="cuadrado")
        self.canvas1.create_rectangle(
            300, 300, 350, 350, fill="#cccccc", tags="cuadrado")

        self.ventana.mainloop()

    def borrar_linea(self):
        self.canvas1.delete(self.linea)

    def borrar_rectangulo(self):
        self.canvas1.delete(self.rectangulo)

    def borrar_ovalo(self):
        self.canvas1.delete(self.ovalo)

    def borrar_cuadrados(self):
        self.canvas1.delete("cuadrado")

    def borrar_todos(self):
        self.canvas1.delete(tk.ALL)


aplicacion = Aplicacion()
