import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):

        self.ventana = tk.Tk()
        self.canvas1 = tk.Canvas(
            self.ventana, width=900, height=500, background="black")
        self.canvas1.grid(column=0, row=0, padx=10, pady=10)

        self.archivo0 = tk.PhotoImage(
            file="/home/ed/cursoPython/TkInter/1.gif")
        #   Hay que usar gif, y tambien ruta absoluta
        self.archivo1 = tk.PhotoImage(
            file="/home/ed/cursoPython/TkInter/2.gif")

        self.canvas1.create_image(
            30, 100, image=self.archivo0, anchor="nw", tags="movil")
        self.canvas1.create_image(
            250, 100, image=self.archivo1, anchor="nw", tags="movil")
        #   Agrego un bind(Accion) para el tag movil, agrego accion presion boton izquierdo
        self.canvas1.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.canvas1.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.carta_seleccionada = None

        self.ventana.mainloop()

    def presion_boton(self, evento):
        #   guardo la referencia de la carta seleccionada
        carta = self.canvas1.find_withtag(tk.CURRENT)
        #   Guardo la carta elegida y su posicion en x y y
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        #   extraigo x e y
        x, y = evento.x, evento.y
        #   desenpaqueto los elementos guardados en carga_seleccionada
        carta, x1, y1 = self.carta_seleccionada
        #   Muevo la carta
        self.canvas1.move(carta, x-x1, y-y1)
        #   actualizo la carta seleccionada con las nuevas posiciones
        self.carta_seleccionada = (carta, x, y)


aplicacion = Aplicacion()
