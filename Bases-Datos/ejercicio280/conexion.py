import mysql.connector
from decouple import config


class Articulos:
    def abrir(self):
        conexion = mysql.connector.connect(
            user=config("MYSQL_USER"),
            passwd=config("MYSQL_PASSWORD"),
            host=config("MYSQL_HOST"),
            port=config("MYSQL_PORT"),
            database=config("MYSQL_DATABASE"),
        )
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into articulos(descripcion,precio) values(%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        return cursor.fetchall()
        #   Es raro, pero tengo que cerrar la conexion luego del return
        cone.close()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        return cursor.fetchall()
        cone.close()

    def borrado_articulo(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def modificar_articulo(self, dato):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, dato)
        cone.commit()
        cone.close()
