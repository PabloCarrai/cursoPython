"""   
Disponer un control checkbutton que muestre
el siguiente mensaje. ¿Estas de acuerdo con los
terminos y condiciones? ademas agregar un Button
cuando se tilde el checkbuton inmediatamente
activar el boton
"""
import tkinter as tk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(
            self.ventana, text="¿Estas de acuerdo con los terminos y condiciones?", variable=self.seleccion1, command=self.activarBoton)
        self.check1.grid(column=0, row=0)

        self.boton = tk.Button(self.ventana, text="Aceptar", state=tk.DISABLED)
        self.boton.grid(column=0, row=1)

        self.ventana.mainloop()

    def activarBoton(self):
        if self.seleccion1.get() == 1:
            self.boton.config(state=tk.NORMAL)
        else:
            if self.seleccion1.get() == 0:
                self.boton.config(state=tk.DISABLED)


aplicacion = Aplicacion()
