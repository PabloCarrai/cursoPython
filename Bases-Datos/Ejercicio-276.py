import mysql.connector

conexion = mysql.connector.connect(
    user="root", passwd="SomosDeCarn3", host="192.168.0.222", port=3307, database="db1"
)
cursor = conexion.cursor()
sql = "insert into articulos(descripcion,precio) values(%s,%s)"
datos=("Naranjas",23.50)
cursor.execute(sql,datos)
datos=("Peras",34)
cursor.execute(sql,datos)
datos=("Bananas",54.50)
cursor.execute(sql,datos)
datos=("Mandarina",33.45)
cursor.execute(sql,datos)
conexion.commit()   #   Este metodo hace que los execute se ejecuten


conexion.close()