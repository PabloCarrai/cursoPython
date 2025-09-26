import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.canvas1 = tk.Canvas(
            self.ventana, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1, padx=10, pady=10)

        self.cuadrado = self.canvas1.create_rectangle(
            150, 10, 200, 60, fill="red")
        self.ventana.bind("<KeyPress>", self.presion_tecla)

        self.ventana.mainloop()

    def presion_tecla(self, evento):
        x1, y1, x2, y2 = self.canvas1.coords(self.cuadrado)
        if (evento.keysym == "Right"):
            if x2+4 <= 600:
                self.canvas1.move(self.cuadrado, 4, 0)
        if (evento.keysym == "Left"):
            if x1-4 >= 0:
                self.canvas1.move(self.cuadrado, -4, 0)
        if (evento.keysym == "Down"):
            if y2+4 <= 400:
                self.canvas1.move(self.cuadrado, 0, 4)
        if (evento.keysym == "Up"):
            if y1-4 >= 0:
                self.canvas1.move(self.cuadrado, 0, -4)


aplicacion = Aplicacion()
