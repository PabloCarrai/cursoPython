import mysql.connector
from decouple import config

conexion = mysql.connector.connect(
    user=config("MYSQL_USER"),
    passwd=config("MYSQL_PASSWORD"),
    host=config("MYSQL_HOST"),
    port=config("MYSQL_PORT"),
    database=config("MYSQL_DATABASE"),
)
cursor = conexion.cursor()
sql = "insert into articulos(descripcion,precio) values(%s,%s)"
datos = ("Manteca", 66.66)
cursor.execute(sql, datos)
conexion.commit()
#   Esto nos devuelve el ultimo id generado
print(f"El valor del ultimo codigo de articulo generado es {cursor.lastrowid}")
conexion.close()
