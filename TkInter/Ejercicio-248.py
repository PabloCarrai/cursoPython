"""  
Confeccionar un programa que tenga
solo un menu de opciones que al ser
presionado nos muestre un cuadro de
mensaje que inform si queremos finalizar
la ejecucion del programa. Si se presiona
"si" se finaliza el programa en caso contrario
no se hace nada
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-248.py")
        self.ventana.geometry("400x250")

        menuprincipal = tk.Menu(self.ventana)
        self.ventana.config(menu=menuprincipal)
        menuprincipal.add_command(label="Opciones", command=self.acercade)

        self.ventana.mainloop()

    def acercade(self):
        respuesta = mb.askyesno(
            "Cuidado", "¿Quiere salir del programa?")
        if respuesta:
            self.ventana.destroy()


aplicacion = Aplicacion()
