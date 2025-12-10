from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as sc
from tkinter import messagebox as ms
from urllib.request import urlopen


class LectorPaginaWeb:
    def __init__(self):
        self.ventana = Tk()
        self.etiquetaIngreseURL = Label(self.ventana, text="Ingrese Url del Sitio Web")
        self.etiquetaIngreseURL.grid(column=0, row=0, padx=10, pady=10)
        self.datoEntradaIngreseURL = StringVar()
        self.entradaIngreseURL = Entry(
            self.ventana, textvariable=self.datoEntradaIngreseURL
        )
        self.entradaIngreseURL.grid(column=0, row=1, padx=10, pady=10)
        self.botonRecuperar = Button(
            self.ventana, text="Recuperar", command=self.recuperarContenidoUrl
        )
        self.botonRecuperar.grid(column=0, row=2, padx=10, pady=10)
        self.scrolledtext = sc.ScrolledText(self.ventana, width=40, height=10)
        self.scrolledtext.grid(column=0, row=3, padx=10, pady=10)

        self.ventana.mainloop()

    def recuperarContenidoUrl(self):
        self.scrolledtext.delete(1.0, END)
        url = self.datoEntradaIngreseURL.get()
        if len(url) <= 0:
            ms.showerror("Error", "Pone una url decente")
        else:
            try:
                with urlopen(url) as response:
                    html_content_bytes = response.read()
                    html_content_string = html_content_bytes.decode("utf-8")
                    self.scrolledtext.insert(END, html_content_string)
            except Exception as e:
                ms.showerror("Error", f"Error abriendo o leyendo url: {e}")


pagina = LectorPaginaWeb()
