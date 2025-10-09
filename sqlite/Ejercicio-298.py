"""
Implementar un programa que solicite el ingreso
de un codigo de un producto y luego nos muestre
su descripcion y precio
"""

import sqlite3

conexion = sqlite3.connect("bd1.db")

try:
    precio = float(input("Precio? "))
except:
    print("Dato incorrecto")

try:
    cursor = conexion.execute("select * from articulos where precio<?", (precio,))
    filas = cursor.fetchall()
    if len(filas) > 0:
        for fila in filas:
            print(f"Productos cuyo precio es menor a {precio}:")
            print(f"id: {fila[0]} Descripcion: {fila[1]} Precio: {fila[2]}")
    else:

        print("No existe articulo con precio menor al ingresado")
except:
    print("Error sql")
finally:
    conexion.close()
