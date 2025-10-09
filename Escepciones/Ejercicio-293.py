import mysql.connector
from decouple import config

try:
    conexion = mysql.connector.connect(
        user=config("MYSQL_USER"),
        passwd=config("MYSQL_PASSWORD"),
        host=config("MYSQL_HOST"),
        port=config("MYSQL_PORT"),
    )
    mycursor = conexion.cursor()
    mycursor.execute("show databasesx")
    resultado = mycursor.fetchall()
    for x in resultado:
        print(x)
except mysql.connector.errors.ProgrammingError:
    print("Error en el comando sql")
finally:
    conexion.close()
    print("Conexion cerrada")
