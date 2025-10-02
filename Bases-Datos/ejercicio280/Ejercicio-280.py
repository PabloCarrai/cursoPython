from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as sc
from tkinter import messagebox as ms
import conexion


class Aplicacion:

    def __init__(self):
        #   Creamos el articulo(conexion a db)
        self.articulo1 = conexion.Articulos()
        #   Creamos la ventana
        self.ventana = Tk()
        #   Seteamos el titulo
        self.ventana.title("Mantenimiento de Articulos")
        #   Creo el notebook
        self.notebook = ttk.Notebook(self.ventana)
        #   Lo acomodo
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        #   Vamos con las secciones
        self.seccion1 = ttk.Frame(self.notebook)
        self.seccion1.grid(padx=10, pady=10)

        self.labelframeCargaArticulos = ttk.LabelFrame(self.seccion1, text="Articulo")
        self.labelframeCargaArticulos.grid(column=0, row=0, padx=10, pady=10)

        #   Label Descripcion
        self.etiquetaCargaArticulosDescripcion = Label(
            self.labelframeCargaArticulos, text="Descripcion:"
        )
        self.etiquetaCargaArticulosDescripcion.grid(column=0, row=0, padx=10, pady=10)

        #   Entrada Descripcion
        self.datoEntradaCargaArticulosDescripcion = StringVar()
        self.entradaCargaArticulosDescripcion = Entry(
            self.labelframeCargaArticulos,
            textvariable=self.datoEntradaCargaArticulosDescripcion,
        )
        self.entradaCargaArticulosDescripcion.grid(column=1, row=0, padx=10, pady=10)
        #   Etiqueta Precio
        self.etiquetaCargaArticuloPrecio = Label(
            self.labelframeCargaArticulos, text="Precio:"
        )
        self.etiquetaCargaArticuloPrecio.grid(column=0, row=1, padx=10, pady=10)
        #   Entrada Precio
        self.datoEntradaCargaArticuloPrecio = StringVar()
        self.entradaCargaArticuloPrecio = ttk.Entry(
            self.labelframeCargaArticulos,
            textvariable=self.datoEntradaCargaArticuloPrecio,
        )
        self.entradaCargaArticuloPrecio.grid(column=1, row=1, padx=10, pady=10)
        #   Boton confirmar
        self.botonConfirmarCargaArticulo = Button(
            self.labelframeCargaArticulos,
            text="Confirmar",
            command=self.cargar_articulo,
        )
        self.botonConfirmarCargaArticulo.grid(column=1, row=2)
        #   Agrego la seccion al notebook
        self.notebook.add(self.seccion1, text="Carga de Articulo")

        #   Otra seccion
        self.seccion2 = ttk.Frame(self.notebook)
        self.seccion2.grid(padx=10, pady=10)

        self.labelframeConsultaCodigo = ttk.Labelframe(self.seccion2, text="Articulo")
        self.labelframeConsultaCodigo.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaConsultaCodigoCodigo = Label(
            self.labelframeConsultaCodigo, text="Codigo"
        )
        self.etiquetaConsultaCodigoCodigo.grid(column=0, row=0, padx=10, pady=10)

        self.datoentradaConsultaCodigoCodigo = StringVar()
        self.entradaConsultaCodigoCodigo = Entry(
            self.labelframeConsultaCodigo,
            textvariable=self.datoentradaConsultaCodigoCodigo,
        )
        self.entradaConsultaCodigoCodigo.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaConsultaCodigoDescripcion = Label(
            self.labelframeConsultaCodigo, text="Descripcion"
        )
        self.etiquetaConsultaCodigoDescripcion.grid(column=0, row=1, padx=10, pady=10)

        self.datoentradaConsultaCodigoDescripcion = StringVar()
        self.entradaConsultaCodigoDescripcion = ttk.Entry(
            self.labelframeConsultaCodigo,
            textvariable=self.datoentradaConsultaCodigoDescripcion,
        )
        self.entradaConsultaCodigoDescripcion.config(state="readonly")
        self.entradaConsultaCodigoDescripcion.grid(column=1, row=1, padx=10, pady=10)

        self.etiquetaConsultaCodigoPrecio = Label(
            self.labelframeConsultaCodigo, text="Precio"
        )
        self.etiquetaConsultaCodigoPrecio.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaConsultaCodigoPrecio = StringVar()
        self.entradaConsultaCodigoPrecio = Entry(
            self.labelframeConsultaCodigo,
            textvariable=self.datoEntradaConsultaCodigoPrecio,
        )
        self.entradaConsultaCodigoPrecio.config(state="readonly")
        self.entradaConsultaCodigoPrecio.grid(column=1, row=2, padx=10, pady=10)

        self.botonConsultaCodigoConsultar = Button(
            self.labelframeConsultaCodigo,
            text="Consultar",
            command=self.consultarPorCodigo,
        )
        self.botonConsultaCodigoConsultar.grid(column=1, row=3, padx=10, pady=10)

        #   La agrego al notebook
        self.notebook.add(self.seccion2, text="Consulta Por Codigo")

        #   Otra seccion
        self.seccion3 = ttk.Frame(self.notebook)
        self.seccion3.grid(padx=10, pady=10)

        self.labelframeListadoCompleto = LabelFrame(self.seccion3, text="Articulo")
        self.labelframeListadoCompleto.grid(column=0, row=0, padx=10, pady=10)

        self.botonListadoCompleto = Button(
            self.labelframeListadoCompleto, text="Listado Completo"
        )
        self.botonListadoCompleto.grid(column=0, row=0, padx=10, pady=10)

        self.areaTexto = sc.ScrolledText(
            self.labelframeListadoCompleto, width=40, height=10
        )
        self.areaTexto.grid(column=0, row=2, padx=10, pady=10)

        #   La agrego al notebook
        self.notebook.add(self.seccion3, text="Listado Completo")
        #   Otra seccion
        self.seccion4 = ttk.Frame(self.notebook)
        self.seccion4.grid(padx=10, pady=10)

        self.labelframeBorradoArticulo = LabelFrame(self.seccion4, text="Articulo")
        self.labelframeBorradoArticulo.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaBorradoArticuloCodigo = Label(
            self.labelframeBorradoArticulo, text="Codigo"
        )
        self.etiquetaBorradoArticuloCodigo.grid(column=0, row=0, padx=10, pady=10)

        self.datoentradaBorradoArticuloCodigo = StringVar()
        self.entradaBorradoArticuloCodigo = ttk.Entry(
            self.labelframeBorradoArticulo,
            textvariable=self.datoentradaBorradoArticuloCodigo,
        )
        self.entradaBorradoArticuloCodigo.grid(column=1, row=0, padx=10, pady=10)
        self.botonBorradoArticuloBorrado = Button(
            self.labelframeBorradoArticulo, text="Borrar"
        )
        self.botonBorradoArticuloBorrado.grid(column=1, row=1, padx=10, pady=10)

        #   La agrego al notebook
        self.notebook.add(self.seccion4, text="Borrado de Articulo")
        self.seccion5 = ttk.Frame(self.notebook)
        self.seccion5.grid(padx=10, pady=10)

        self.labelframeModificarArticulo = LabelFrame(self.seccion5, text="Articulo")
        self.labelframeModificarArticulo.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaModificarArticuloCodigo = Label(
            self.labelframeModificarArticulo, text="Codigo"
        )
        self.etiquetaModificarArticuloCodigo.grid(column=0, row=0, padx=10, pady=10)

        self.datoEntradaModificarArticuloCodigo = StringVar()
        self.entradaModificarArticuloCodigo = Entry(
            self.labelframeModificarArticulo,
            textvariable=self.datoEntradaModificarArticuloCodigo,
        )
        self.entradaModificarArticuloCodigo.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaModificarArticuloDescripcion = Label(
            self.labelframeModificarArticulo, text="Descripcion"
        )
        self.etiquetaModificarArticuloDescripcion.grid(
            column=0, row=1, padx=10, pady=10
        )
        self.datoEntradaModificarArticuloDescripcion = StringVar()
        self.entradaModificarArticuloDescripcion = Entry(
            self.labelframeModificarArticulo,
            textvariable=self.datoEntradaModificarArticuloDescripcion,
        )
        self.entradaModificarArticuloDescripcion.grid(column=1, row=1, padx=10, pady=10)

        self.etiquetaModificarArticuloPrecio = Label(
            self.labelframeModificarArticulo, text="Precio"
        )
        self.etiquetaModificarArticuloPrecio.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaModificarArticuloPrecio = StringVar()
        self.entradaModificarArticuloPrecio = Entry(
            self.labelframeModificarArticulo,
            textvariable=self.datoEntradaModificarArticuloPrecio,
        )
        self.entradaModificarArticuloPrecio.grid(column=1, row=2, padx=10, pady=10)

        self.botonModificarArticuloConsultar = Button(
            self.labelframeModificarArticulo, text="Consultar"
        )
        self.botonModificarArticuloConsultar.grid(column=1, row=3, padx=10, pady=10)
        self.botonModificarArticuloModificar = Button(
            self.labelframeModificarArticulo, text="Modificar"
        )
        self.botonModificarArticuloModificar.grid(column=1, row=4, padx=10, pady=10)

        #   La agrego al notebook
        self.notebook.add(self.seccion5, text="Modificar Articulo")

        self.ventana.mainloop()

    def cargar_articulo(self):
        datos = (
            self.datoEntradaCargaArticulosDescripcion.get(),
            self.datoEntradaCargaArticuloPrecio.get(),
        )
        self.articulo1.alta(datos)
        ms.showinfo("Informacion", "Datos cargados")
        self.datoEntradaCargaArticulosDescripcion.set("")
        self.datoEntradaCargaArticuloPrecio.set("")

    def consultarPorCodigo(self):
        self.entradaConsultaCodigoDescripcion.config(state="normal")
        self.entradaConsultaCodigoPrecio.config(state="normal")
        print(self.datoentradaConsultaCodigoCodigo.get())



aplicacion = Aplicacion()
