import mysql.connector


class Articulos:
    def abrir(self):
        conexion = mysql.connector.connect(
            user="root",
            passwd="SomosDeCarn3",
            host="192.168.0.222",
            port=3307,
            database="db1",
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
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def borrado_articulo(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        pass

    def modificar_articulo(self, dato):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        pass
