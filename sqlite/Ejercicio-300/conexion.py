import sqlite3

class Articulos:
    def abrir(self):
        conexion = sqlite3.connect("bd1.db")
        return conexion

    def alta(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "insert into articulos(descripcion,precio) values(?,?)"
            cursor.execute(sql, datos)
            cone.commit()
        finally:
            cone.close()

    def consulta(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select descripcion, precio from articulos where codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            #   Es raro, pero tengo que cerrar la conexion luego del return
            cone.close()

    def recuperar_todos(self):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select codigo, descripcion, precio from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def borrado_articulo(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "delete from articulos where codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
        finally:
            cone.close()

    def modificar_articulo(self, dato):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "update articulos set descripcion=?, precio=? where codigo=?"
            cursor.execute(sql, dato)
            cone.commit()
        finally:
            cone.close()
