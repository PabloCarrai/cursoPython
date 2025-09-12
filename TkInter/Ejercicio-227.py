"""  
Disponer de varios objetos de la clase
checkbutton con nombres de navegadores web. 
En el titulo de la ventana mostrar todos los
nombres de navegadores seleccionados
"""


import tkinter as tk


class Aplicacion:
    leyenda = ""

    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccionfirefox = tk.IntVar()
        self.checkbotonfirefox = tk.Checkbutton(
            self.ventana, text="Firefox", variable=self.seleccionfirefox, command=self.cambiartitulo)
        self.checkbotonfirefox.grid(column=0, row=0)

        self.seleccionopera = tk.IntVar()
        self.checkbotonopera = tk.Checkbutton(
            self.ventana, text="Opera", variable=self.seleccionopera, command=self.cambiartitulo)
        self.checkbotonopera.grid(column=0, row=1)

        self.seleccionchrome = tk.IntVar()
        self.checkbotonchrome = tk.Checkbutton(
            self.ventana, text="Chrome", variable=self.seleccionchrome, command=self.cambiartitulo)
        self.checkbotonchrome.grid(column=0, row=2)

        self.ventana.mainloop()

    def cambiartitulo(self):
        cadena = ""
        if self.seleccionchrome.get() == 1:
            cadena = cadena+"Chrome"
        if self.seleccionfirefox.get() == 1:
            cadena = cadena+"Firefox"
        if self.seleccionopera.get() == 1:
            cadena = cadena+"Opera"

        self.ventana.title(cadena)


aplicacion = Aplicacion()
