import psycopg2

conexion1 = psycopg2.connect(
    host="192.168.0.222",
    port=5432,
    database="mi_base_de_datos",
    user="tu_usuario",
    password="tu_contraseña_segura",
)
cursor1 = conexion1.cursor()
cursor1.execute("delete from articulos where codigo=1")
cursor1.execute("update articulos set precio=50 where codigo=3")
conexion1.commit()
cursor1.execute("select codigo,descripcion,precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()
