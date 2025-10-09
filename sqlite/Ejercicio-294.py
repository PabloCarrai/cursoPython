import sqlite3  #   Importamos el modulo sqlite3

conexion = sqlite3.connect("bd1.db")  #   me conecto a la db bd1, si no existe la creo
try:
    #   Creo la tabla articulos
    conexion.execute(
        "create table articulos(codigo integer primary key autoincrement,descripcion text,precio real)"
    )
    print("Se creo la tabla articulos")
    #   Capturo excepciones de sqlite en el caso de que la tabla ya exista
except sqlite3.OperationalError:
    print("La tabla articulo ya existe")
finally:
    #   Cierro la conexion
    conexion.close()
