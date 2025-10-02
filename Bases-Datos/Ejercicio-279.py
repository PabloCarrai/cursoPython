from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as sc
from tkinter import messagebox as ms
import mysql.connector


class Aplicacion:
    def __init__(self):
        self.ventana = Tk()

        self.ventana.title("Mantenimiento de Articulos")

        self.notebook = ttk.Notebook(self.ventana)
        #   Elementos del primer labelframe(Carga Articulo)
        #   Primer LabelFrame
        self.labelframe = ttk.Labelframe(self.ventana, text="Articulo: ")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaDescripcion = ttk.Label(self.labelframe, text="Descripcion")
        self.etiquetaDescripcion.grid(column=0, row=0, padx=10, pady=10)

        self.datosentradaDescripcion = StringVar()
        self.entradaDescripcion = ttk.Entry(
            self.labelframe, textvariable=self.datosentradaDescripcion
        )
        self.entradaDescripcion.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaPrecio = Label(self.labelframe, text="Precio")
        self.etiquetaPrecio.grid(column=0, row=1, padx=10, pady=10)

        self.datoentradaPrecio = StringVar()
        self.entradaPrecio = Entry(self.labelframe, textvariable=self.datoentradaPrecio)
        self.entradaPrecio.grid(column=1, row=1, padx=10, pady=10)

        self.botonConfirmar = Button(
            self.labelframe, text="Confirmar", command=self.agregarRegistro
        )
        self.botonConfirmar.grid(column=1, row=2, padx=10, pady=10)

        #   Segundo Labelframe
        self.labelframe1 = ttk.Labelframe(self.ventana, text="Articulo:")

        self.etiquetaCodigo = Label(self.labelframe1, text="Codigo:")
        self.etiquetaCodigo.grid(column=0, row=0, padx=10, pady=10)

        self.datoentradaCodigo = StringVar()
        self.entradaCodigo = Entry(
            self.labelframe1, textvariable=self.datoentradaCodigo
        )
        self.entradaCodigo.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaDescripcion1 = Label(self.labelframe1, text="Descripcion")
        self.etiquetaDescripcion1.grid(column=0, row=1, padx=10, pady=10)

        self.datosentradaDescripcion1 = StringVar()
        self.entradaDescripcion1 = Entry(
            self.labelframe1, textvariable=self.datosentradaDescripcion1
        )
        self.entradaDescripcion1.grid(column=1, row=1, padx=10, pady=10)

        self.etiquetaPrecio1 = Label(self.labelframe1, text="Precio")
        self.etiquetaPrecio1.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaPrecio1 = StringVar()
        self.entradaPrecio1 = Entry(self.labelframe1)
        self.entradaPrecio1.grid(column=1, row=2, padx=10, pady=10)

        self.botonConsultar = Button(
            self.labelframe1, text="Consultar", command=self.consultarCodigo
        )
        self.botonConsultar.grid(column=1, row=3, padx=10, pady=10)

        #   Por defecto tienen que estar desabilitados
        self.entradaDescripcion1.config(state="disabled")
        self.entradaPrecio1.config(state="disabled")

        #   Tercer LabelFrame
        self.labelframe2 = ttk.LabelFrame(self.ventana, text="Articulo:")

        self.botonListadoCompleto = Button(
            self.labelframe2, text="Listado Completo", command=self.listadoCompleto
        )
        self.botonListadoCompleto.grid(column=0, row=1, padx=10, pady=10)

        self.areaTexto = sc.ScrolledText(self.labelframe2, width=40, height=10)
        self.areaTexto.grid(column=0, row=2, padx=10, pady=10)

        #   Cargo el primer elemento(labelframe) al notebook
        self.notebook.add(self.labelframe, text="Carga de Articulo")
        self.notebook.add(self.labelframe1, text="Consulta por Codigo")
        self.notebook.add(self.labelframe2, text="Listado Completo")

        self.notebook.grid(padx=10, pady=10)

        self.ventana.mainloop()

    def agregarRegistro(self):
        conexion = mysql.connector.connect(
            user="root",
            passwd="SomosDeCarn3",
            host="192.168.0.222",
            port=3307,
            database="db1",
        )
        cursor = conexion.cursor()
        sql = "insert into articulos(descripcion,precio) values(%s,%s)"
        datos = (
            f"{self.datosentradaDescripcion.get()}",
            f"{self.datoentradaPrecio.get()}",
        )
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
        ms.showinfo(message="Registro insertado", title="Insercion Correcta")
        self.entradaDescripcion.delete(0, END)
        self.entradaPrecio.delete(0, END)

    def consultarCodigo(self):
        self.entradaDescripcion1.config(state="normal")
        self.entradaPrecio1.config(state="normal")
        conexion = mysql.connector.connect(
            user="root",
            passwd="SomosDeCarn3",
            host="192.168.0.222",
            port=3307,
            database="db1",
        )
        cursor = conexion.cursor()
        cursor.execute(
            "select descripcion, precio from articulos where codigo=%s",
            [self.datoentradaCodigo.get()],
        )
        for fila in cursor:
            self.entradaDescripcion1.delete(0, END)
            self.entradaPrecio1.delete(0, END)
            self.entradaDescripcion1.insert(0, f"{fila[0]}")
            self.entradaPrecio1.insert(0, f"{fila[1]}")
        conexion.close()

    def listadoCompleto(self):
        self.areaTexto.delete("1.0", END)
        conexion = mysql.connector.connect(
            user="root",
            passwd="SomosDeCarn3",
            host="192.168.0.222",
            port=3307,
            database="db1",
        )
        cursor = conexion.cursor()
        cursor.execute("select * from articulos")
        for fila in cursor:
            self.areaTexto.insert(
                END, f"Codigo: {fila[0]}\n Descripcion: {fila[1]}\n Precio: {fila[2]}\n"
            )
        conexion.close()

        pass


aplicacion = Aplicacion()
