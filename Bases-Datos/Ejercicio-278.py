#   eliminar datos y modificar registros
import mysql.connector

conexion = mysql.connector.connect(
    user="root", passwd="SomosDeCarn3", host="192.168.0.222", port=3307, database="db1"
)
cursor = conexion.cursor()
#   Eliminamos registro cuyo codigo sea igual a 1
cursor.execute("delete from articulos where codigo=1")
#   Cambiamos el precio del articulo cuyo codigo es 3
cursor.execute("update articulos set precio=50 where codigo=3")
#   Aplicamos los cambios
conexion.commit()

#   Nos traemos lo que haya
cursor.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(f"Codigo: {fila[0]} Descripcion: {fila[1]} Precio: {fila[2]}")


conexion.close()
