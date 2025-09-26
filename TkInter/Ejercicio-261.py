import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()

        self.canvas1 = tk.Canvas(
            self.ventana, width=700, height=400, background="black")
        self.canvas1.grid(column=0, row=1, padx=10, pady=10)

        archivo1 = tk.PhotoImage(file="/home/ed/cursoPython/TkInter/png1.png")
        self.canvas1.create_image(300, 100, archivo1, anchor="nw")

        self.ventana.mainloop()


aplicacion = Aplicacion()
