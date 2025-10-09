import sqlite3

conexion = sqlite3.connect("bd1.db")

try:
    cursor = conexion.cursor()
    cursor.execute("select * from articulos")
    filas = cursor.fetchall()
    for linea in filas:
        print(f"id:{linea[0]}, Descripcion: {linea[1]}, Precio: {linea[2]}")
    print("Registros leidos")
except sqlite3.OperationalError:
    print("problemas con sqlite3")
finally:
    conexion.close()
    print("Conexion Cerrada")
