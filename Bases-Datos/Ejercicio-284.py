import mysql.connector
from decouple import config


class gestorDB:
    def abrir(self):
        conexion = mysql.connector.connect(
            user=config("MYSQL_USER"),
            passwd=config("MYSQL_PASSWORD"),
            host=config("MYSQL_HOST"),
            port=config("MYSQL_PORT"),
        )
        return conexion

    def eliminar_Db(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = f"drop database if exists db2"
        cursor.execute(sql)
        cursor.close()
        cone.close()


prueba1 = gestorDB()
prueba1.eliminar_Db()
