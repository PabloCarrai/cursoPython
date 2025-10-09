"""
Implementar un programa que solicite el ingreso
de un codigo de un producto y luego nos muestre
su descripcion y precio
"""

import sqlite3

conexion = sqlite3.connect("bd1.db")

try:
    codigo = int(input("Ingrese un codigo entre 1,2 y 3 "))
    if codigo > 3 or codigo < 1:
        codigo = int(input("Tiene que ser entre 1,2 y 3 "))

except ValueError:
    print("Valor ingresado incorrecto")

try:
    cursor = conexion.cursor()
    cursor.execute("select * from articulos where codigo=?", (codigo,))
    resultado = cursor.fetchone()
    if resultado != None:
        print("Producto:")
        print(f"id:{resultado[0]}, Descripcion: {resultado[1]}, Precio: {resultado[2]}")
except sqlite3.OperationalError:
    print("problemas con sqlite3")
finally:
    conexion.close()
    print("Conexion Cerrada")
