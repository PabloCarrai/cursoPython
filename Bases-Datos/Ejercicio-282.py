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

    def insertar_Varios(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into articulos(descripcion,precio) values(%s,%s)"
        #   Este executemany inserta una lista de tuplas(datos)
        cursor.executemany(sql, datos)
        cone.commit()
        cone.close()


articulo = Articulos()

datos = [
    ("Lavandina", 23.56),
    ("Lentejas Secas", 40.59),
    ("Azucar Negra", 55.98),
    ("Azucar Blanca", 55.97),
    ("Miel Pura", 20.89),
]
articulo.insertar_Varios(datos)
