""" 
Confeccionarun programa que permita cargar
un codigo de producto como clave en un diccionario.
Guardar para dicha clave una tupla con el nombre del producto
su precio y cantidad en stock.
Implementar las siguientes actividades.
1)  Carga de datos en el diccionario
2)  Listado completo de productos
3)  Consulta de un producto por su clave, mostrar
el nombre, precio y stock
4)  Listado de todos los productos que tengan
un stock con valor a cero
"""


def cargar_datos():  # 1
    productos = {}
    continuar = "s"
    while continuar == "s":
        codigo = input("Codigo?  ")
        producto = input("Producto?  ")
        precio = int(input(f"Precio de {producto}  "))
        stock = int(input(f"Stock de {producto}  "))
        productos[codigo] = (producto, precio, stock)
        continuar = input("Continua Cargando Datos (s/n)?  ")
    return productos


def listado_productos(productos):  # 2
    print("-"*60)
    print("Listado de articulos completo")
    print("-"*60)
    for codigo in productos:
        print(
            f"Codigo: {codigo} Producto: {productos[codigo][0]} Precio: ${productos[codigo][1]} Stock: {productos[codigo][2]}")
    print("-"*60)


def consulta_clave(productos):
    print("-"*60)
    print("Consulta de articulos por Codigo")
    print("-"*60)
    codigo = input("Codigo del producto?  ")
    if codigo in productos:
        print(
            f"Codigo: {codigo} Producto: {productos[codigo][0]} Precio: ${productos[codigo][1]} Stock: {productos[codigo][2]}")
    else:
        print(
            f"No tenemos ningun producto registrado bajo ese codigo Codigo: {codigo}  ")
    print("-"*60)


def consulta_clave_aCero(productos):
    print("-"*60)
    print("Consulta de Articulos con Stock a Cero(0) ")
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(
                f"Codigo: {codigo} Producto: {productos[codigo][0]} Precio: ${productos[codigo][1]}")
    print("-"*60)


productos = cargar_datos()
listado_productos(productos)
consulta_clave(productos)
consulta_clave_aCero(productos)
