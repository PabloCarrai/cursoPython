import tkinter as tk


class Aplicacion:
    def __init__(self):
        #   Atributo de la clase
        self.valor = 1
        #   Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Controles Button y Label")
        #   Label que muestra el texto del valor
        self.label1 = tk.Label(self.ventana, text=self.valor)
        #   Esto posiciona el label en la columna y linea 0
        self.label1.grid(column=0, row=0)
        #   Setea en rojo el fondo
        self.label1.configure(background="red")
        #   Primer boton para incrementar en 1 el atributo valor
        self.boton1 = tk.Button(
            self.ventana, text="Incrementar", command=self.incrementar)
        #   Ubica el boton en la columna 0 y la linea 1
        self.boton1.grid(column=0, row=1)
        #   Segundo boton para decrementar en 1 el atributo valor
        self.boton2 = tk.Button(
            self.ventana, text="Decrementar", command=self.decrementar)
        #   Setea el boton2 en la columna 0 y linea 2
        self.boton2.grid(column=0, row=2)
        #   El loop de la aplicacion
        self.ventana.mainloop()

    #   metodo incrementar
    def incrementar(self):
        self.valor = self.valor+1
        #   De este modo actualiza el valor en el label
        self.label1.config(text=self.valor)
    #   Metodo decrementar

    def decrementar(self):
        self.valor = self.valor-1
        #   De este modo actualiza el valor en el label
        self.label1.config(text=self.valor)


aplicacion1 = Aplicacion()
