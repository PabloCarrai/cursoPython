"""
Crear una base de datos y insertar unas tablas.
"""

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

    def crear_Db(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = f"create database db2"
        cursor.execute(sql)
        sql="use db2"
        cursor.execute(sql)
        sql="create table usuarios(nombre varchar(30) primary key, clave varchar(30))"
        cursor.execute(sql)
        cone.commit()
        cursor.close()
        cone.close()


prueba1 = gestorDB()
prueba1.crear_Db()
