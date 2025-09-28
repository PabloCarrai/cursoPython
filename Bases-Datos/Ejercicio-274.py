import mariadb

conexion = mysql.connector.connect(
    host="192.168.0.222", user="root", passwd="Somosdecarne", port=3306)
cursor = conexion.cursor()
cursor.execute("show databases")
for base in cursor:
    print(base)
conexion.close()
