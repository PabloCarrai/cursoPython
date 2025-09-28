import mysql.connector

conexion = mysql.connector.connect(user="root", passwd="SomosDeCarn3",host="192.168.0.222",port=3307)
cursor = conexion.cursor()
cursor.execute("show databases")
for base in cursor:
    print(base[0])
conexion.close()
