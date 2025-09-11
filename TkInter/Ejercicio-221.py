""" 
Ingresar el nombre de usuario y clave en controles de tipo Entry. 
Si se ingresa la cadena usuario:juan clave abc123 mostrar en el 
titulo de la ventana el mensaje "Correcto". En caso contrario
mostrar el mensaje "Incorrecto"
Para mostrar el "*" cuando se ingresar la clave debemos pasar
en el parametro "show" el caracter a mostrar. 

self.entry2=tk.Entry(self.ventana1, width=30,textvariable=self.dato2, show="*")
"""
import tkinter as tk


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("200x200")

        self.labelnombre = tk.Label(
            self.ventana, text="Nombre: ").grid(column=0, row=0)
        self.datonombre = tk.StringVar()
        self.entrynombre = tk.Entry(self.ventana, width=10,
                                    textvariable=self.datonombre).grid(column=1, row=0)

        self.labelclave = tk.Label(
            self.ventana, text="Clave:").grid(column=0, row=1)
        self.datoclave = tk.StringVar()
        self.entryclave = tk.Entry(
            self.ventana, width=10, textvariable=self.datoclave, show="*").grid(column=1, row=1)

        self.boton = tk.Button(
            self.ventana, text="Aceptar", command=self.validarClave).grid(column=0, row=2)
        self.ventana.mainloop()

    def validarClave(self):
        if self.datonombre.get() == "juan" and self.datoclave.get() == "abc123":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")


aplicacion = Aplicacion()
