"""
Confeccionar una aplicacion que muestre
un dialogo cuando se seleccione una opcion
del menu. El dialogo debe solicitar el ingreso
de dos enteros que se utilizaran en la ventana
principal para redimensionarla.
"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio-249.py")

        barra_menu = tk.Menu()
        menu_opciones = tk.Menu(barra_menu, tearoff=True)
        barra_menu.add_cascade(menu=menu_opciones, label="Opciones")
        menu_opciones.add_command(
            label="Configurar Ventana", command=self.configurarVentana)
        self.ventana.config(menu=barra_menu)

        self.ventana.mainloop()

    def configurarVentana(self):
        dialogo = DialogoTamaño(self.ventana)
        s = dialogo.mostrar()
        self.ventana.geometry(f"{s[0]}x{s[1]}")


class DialogoTamaño:

    def __init__(self, ventanaprincipal):
        #   Relacionamos el dialogo con la ventana principal
        self.dialogo = tk.Toplevel(ventanaprincipal)
        self.etiqueta = ttk.Label(self.dialogo, text="Ingrese Ancho:")
        self.etiqueta.grid(column=0, row=0)
        self.datoancho = tk.StringVar()
        self.entradaancho = ttk.Entry(
            self.dialogo, textvariable=self.datoancho)
        self.entradaancho.focus()
        self.entradaancho.grid(column=1, row=0)
        self.etiqueta1 = ttk.Label(self.dialogo, text="Ingrese Alto:")
        self.etiqueta1.grid(column=0, row=1)
        self.datoalto = tk.StringVar()
        self.entradaalto = ttk.Entry(
            self.dialogo, textvariable=self.datoalto)
        self.entradaalto.grid(column=1, row=1)
        self.boton = ttk.Button(
            self.dialogo, text="Continuar", command=self.confirmar)
        self.boton.grid(column=1, row=2)
        self.dialogo.protocol("WM_DELETE_WINDOWS", self.confirmar)
        self.dialogo.resizable(0, 0)
        self.dialogo.grab_set()

    def mostrar(self):
        self.dialogo.wait_window()  # Aparece y no sale hasta cerrar
        return (self.datoancho.get(), self.datoalto.get())

    def confirmar(self):
        self.dialogo.destroy()


aplicacion = Aplicacion()
