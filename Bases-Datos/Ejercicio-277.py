#   Recuperar datos de la tabla
import mysql.connector

conexion = mysql.connector.connect(
    user="root", passwd="SomosDeCarn3", host="192.168.0.222", port=3307, database="db1"
)
cursor = conexion.cursor()
cursor.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(f"Codigo: {fila[0]} Descripcion: {fila[1]} Precio: {fila[2]}")
conexion.close()
