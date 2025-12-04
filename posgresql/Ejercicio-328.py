import psycopg2

conexion1 = psycopg2.connect(
    host="192.168.0.222",
    port=5432,
    database="mi_base_de_datos",
    user="tu_usuario",
    password="tu_contraseña_segura",
)
cursor1 = conexion1.cursor()
cursor1.execute("select codigo,descripcion,precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()
