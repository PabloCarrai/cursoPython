import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class Aplicacion:

    def __init__(self):
        self.ventana = tk.Tk()

        self.agregar_menu()
        self.scrolledtext = st.ScrolledText(self.ventana, width=80, height=20)
        self.scrolledtext.grid(column=0, row=0, padx=10, pady=10)

        self.ventana.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar Archivo", command=self.guardar)
        opciones1.add_command(label="Recuperar Archivo",
                              command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

    def salir(self):
        sys.exit(0)

    def guardar(self):
        nombrearch = fd.asksaveasfilename(initialdir="/home/ed/cursoPython/Archivos/", title="Guardar Como",
                                          filetypes=(("txt files", ".txt"), ("todos los archivos", "*.*")))
        if nombrearch != "":
            archivo = open(nombrearch, "w", encoding="utf-8")
            archivo.write(self.scrolledtext.get("1.0", tk.END))
            archivo.close()
            mb.showinfo("Informacion",
                        "Los datos fueron guardados en el archivo")

    def recuperar(self):
        nombrearch = fd.askopenfilename(initialdir="/home/ed/cursoPython/Archivos/", title="Guardar Como",
                                        filetypes=(("txt files", ".txt"), ("todos los archivos", "*.*")))
        print(nombrearch)
        if nombrearch != "":
            archivo = open(nombrearch, "r", encoding="utf-8")
            contenido = archivo.read()
            archivo.close()
            self.scrolledtext.delete("1.0", tk.END)
            self.scrolledtext.insert("1.0", contenido)


aplicacion = Aplicacion()
