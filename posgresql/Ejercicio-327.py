import psycopg2

conexion1 = psycopg2.connect(
    host="192.168.0.222",
    port=5432,
    database="mi_base_de_datos",
    user="tu_usuario",
    password="tu_contraseña_segura",
)
cursor1 = conexion1.cursor()
sql = "insert into articulos(descripcion,precio) values(%s,%s)"
datos = ("Naranja", 23.50)
cursor1.execute(sql, datos)
datos = ("Peras", 34)
cursor1.execute(sql, datos)
datos = ("Banana", 25)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
