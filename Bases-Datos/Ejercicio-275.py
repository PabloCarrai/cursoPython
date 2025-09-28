"""
Mostrar todas las tablas de la base de datos db1
"""

import mysql.connector

conexion = mysql.connector.connect(
    user="root", passwd="SomosDeCarn3", host="192.168.0.222", port=3307, database="db1"
)
cursor = conexion.cursor()
cursor.execute("show tables")
for tabla in cursor:
    print(tabla)


conexion.close()
