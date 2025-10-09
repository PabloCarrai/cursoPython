import sqlite3

conexion = sqlite3.connect("bd1.db")

try:
    #   Inserto y se pone en donde aparece ?
    conexion.execute(
        "insert into articulos(descripcion,precio)values(?,?)", ("naranjas", 23.5)
    )
    conexion.execute(
        "insert into articulos(descripcion,precio)values(?,?)", ("peras", 33.5)
    )
    conexion.execute(
        "insert into articulos(descripcion,precio)values(?,?)", ("mandarina", 43.5)
    )
    conexion.commit()
    print("registros insertados")
except sqlite3.OperationalError:
    print("problemas con sqlite3")
finally:
    conexion.close()
    print("Conexion Cerrada")
