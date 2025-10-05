import mysql.connector
from decouple import config


class gestorDB:
    def abrir(self):
        conexion = mysql.connector.connect(
            user=config("MYSQL_USER"),
            passwd=config("MYSQL_PASSWORD"),
            host=config("MYSQL_HOST"),
            port=config("MYSQL_PORT"),
            db=config("MYSQL_DATABASE"),
        )
        return conexion

    def eliminar_Db(self):
        cone = self.abrir()
        cursor = cone.cursor()

        sql = f"drop table if exists usuarios"
        cursor.execute(sql)

        sql = f"create table usuario(nombre varchar(30) primary key,clave varchar(30),mail varchar(70))"
        cursor.execute(sql)

        cone.commit()
        cone.close()


prueba1 = gestorDB()
prueba1.eliminar_Db()
