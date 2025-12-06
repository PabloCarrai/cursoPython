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
            self.labelframeListadoCompleto,
            text="Listado Completo",
            command=self.listadoCompleto,
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
            self.labelframeBorradoArticulo, text="Borrar", command=self.borrarArticulo
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
        self.entradaModificarArticuloDescripcion.config(state="disabled")

        self.etiquetaModificarArticuloPrecio = Label(
            self.labelframeModificarArticulo, text="Precio"
        )
        self.etiquetaModificarArticuloPrecio.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaModificarArticuloPrecio = StringVar()
        self.entradaModificarArticuloPrecio = Entry(
            self.labelframeModificarArticulo,
            textvariable=self.datoEntradaModificarArticuloPrecio,
        )
        self.entradaModificarArticuloPrecio.config(state="disabled")
        self.entradaModificarArticuloPrecio.grid(column=1, row=2, padx=10, pady=10)

        self.botonModificarArticuloConsultar = Button(
            self.labelframeModificarArticulo,
            text="Consultar",
            command=self.consultaPorCodigo2,
        )
        self.botonModificarArticuloConsultar.grid(column=1, row=3, padx=10, pady=10)
        self.botonModificarArticuloModificar = Button(
            self.labelframeModificarArticulo,
            text="Modificar",
            command=self.modificarRegistro,
        )
        self.botonModificarArticuloModificar.grid(column=1, row=4, padx=10, pady=10)
        self.botonModificarArticuloModificar.config(state="disabled")

        #   La agrego al notebook
        self.notebook.add(self.seccion5, text="Modificar Articulo")

        self.ventana.mainloop()

    def cargar_articulo(self):
        datos = (
            self.datoEntradaCargaArticulosDescripcion.get(),
            self.datoEntradaCargaArticuloPrecio.get(),
        )
        #   Chequeo que haya algo cargado en las entradas de datos
        if (
            len(self.datoEntradaCargaArticulosDescripcion.get()) == 0
            or len(self.datoEntradaCargaArticuloPrecio.get()) == 0
        ):
            ms.showerror("Cuidado", "No se han cargado datos")
        else:
            self.articulo1.alta(datos)
            ms.showinfo("Informacion", "Datos cargados")
            self.datoEntradaCargaArticulosDescripcion.set("")
            self.datoEntradaCargaArticuloPrecio.set("")

    def consultarPorCodigo(self):
        self.entradaConsultaCodigoDescripcion.config(state="normal")
        self.entradaConsultaCodigoPrecio.config(state="normal")
        self.entradaConsultaCodigoDescripcion.delete(0, END)
        self.entradaConsultaCodigoPrecio.delete(0, END)
        datos = (self.datoentradaConsultaCodigoCodigo.get(),)
        if len(self.datoentradaConsultaCodigoCodigo.get()) == 0:
            ms.showerror("Cuidado", "No ha insertado el codigo a buscar")
        else:
            resultado = self.articulo1.consulta(datos)
            if len(resultado) > 0:
                self.entradaConsultaCodigoDescripcion.insert("0", resultado[0][0])
                self.entradaConsultaCodigoPrecio.insert("0", resultado[0][1])
            else:
                self.entradaConsultaCodigoDescripcion.insert("0", "")
                self.entradaConsultaCodigoPrecio.insert("0", "")
                ms.showinfo("Informacion", "No existe articulo con dicho codigo")

    def listadoCompleto(self):
        self.areaTexto.delete("1.0", END)
        resultado = self.articulo1.recuperar_todos()
        for fila in resultado:
            self.areaTexto.insert(
                END, f"Codigo: {fila[0]}\n Descripcion: {fila[1]}\n Precio: {fila[2]}\n"
            )

    def borrarArticulo(self):
        datos = (self.datoentradaBorradoArticuloCodigo.get(),)
        resultado = self.articulo1.borrado_articulo(datos)
        ms.showinfo("Informacion", "Registro borrado")
        self.datoentradaBorradoArticuloCodigo.set("")

    def consultaPorCodigo2(self):
        self.entradaModificarArticuloDescripcion.config(state="normal")
        self.entradaModificarArticuloDescripcion.delete(0, END)
        self.entradaModificarArticuloPrecio.config(state="normal")
        self.entradaModificarArticuloPrecio.delete(0, END)
        self.entradaModificarArticuloCodigo.config(state="readonly")
        datos = (self.datoEntradaModificarArticuloCodigo.get(),)
        self.botonModificarArticuloModificar.config(state="normal")
        if len(self.datoEntradaModificarArticuloCodigo.get()) == 0:
            ms.showerror("Cuidado", "No ha insertado el codigo a buscar")
        else:
            resultado = self.articulo1.consulta(datos)
            if len(resultado) > 0:
                self.entradaModificarArticuloDescripcion.insert("0", resultado[0][0])
                self.entradaModificarArticuloPrecio.insert("0", resultado[0][1])
            else:
                self.entradaModificarArticuloDescripcion.insert("0", "")
                self.entradaModificarArticuloPrecio.insert("0", "")
                ms.showinfo("Informacion", "No existe articulo con dicho codigo")

    def modificarRegistro(self):
        datos = (
            self.entradaModificarArticuloDescripcion.get(),
            self.entradaModificarArticuloPrecio.get(),
            self.entradaModificarArticuloCodigo.get(),
        )
        self.articulo1.modificar_articulo(datos)
        ms.showinfo("Hecho", "Registro Modificado")
        self.entradaModificarArticuloCodigo.config(state="normal")


aplicacion = Aplicacion()
