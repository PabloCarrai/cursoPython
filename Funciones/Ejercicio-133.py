""" 
Desarrollar una aplicacion que permita ingresar
por teclado los nombres de 5 articulos y sus precios. 
Definir las siguientes funciones
1) Cargar los nombres de articulos y sus precios. 
2) Imprimir los nombres y precios
3) Imprimir nombre de articulos con un precio mayor
4) Ingresar por teclado un importe y luego mostrar
todos los articulos con un precio menor o igual al
valor ingresados. 
"""


def cargarProductosPrecio():  # 1)
    productos = []
    precios = []
    for i in range(5):
        producto = input("Producto? ")
        precio = int(input("Precio? "))
        productos.append(producto)
        precios.append(precio)
    return productos, precios


def imprimirProductosPrecio(producto, precio):  # 2)
    print("Listado de Productos:")
    for x in range(len(producto)):
        print(f"Producto: {producto[x]}, Precio: $ {precio[x]}")


def imprimirNombreProductoPrecio(producto, precio):  # 3)
    mayor = precio[0]
    mayorproducto = producto[0]
    for i in range(len(precio)):
        if (precio[i] > mayor):
            mayor = precio[i]
            mayorproducto = producto[i]
    print(
        f"El producto de mayor precio es: {mayorproducto} Su precio $ {mayor}")


def inprimirNombreProductoPrecioMenorIgual(producto, precio):  # 4)
    montoAConsultar = int(
        input("Ingrese el monto de los productos a consultar "))
    for i in range(len(precio)):
        if (precio[i] <= montoAConsultar):
            print(
                f"Productos cuyo monto son menores o iguales a {montoAConsultar}")
            print(f"Productos: {producto[i]} Precio:{precio[i]}")


productos, precios = cargarProductosPrecio()
imprimirProductosPrecio(productos, precios)
imprimirNombreProductoPrecio(productos, precios)
inprimirNombreProductoPrecioMenorIgual(productos, precios)
