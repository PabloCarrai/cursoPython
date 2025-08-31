""" 
Almacenar los nombres de 5 productos y sus precios. 
Utilizar una lista y cada elemento una tupla. 
Desarrollar las funciones. 
1) Cargar por teclado
2) Listar los productos y precios
3) Imprimir los productos con precios
comprendidos entre 10 y 15
"""


def cargar_productos():
    productos = []
    for i in range(5):
        producto = input("Producto?   ")
        precio = int(input("Precio?  "))
        productos.append((producto, precio))
    return productos


def listar_productos(productos):
    print("Productos-Precio")
    for producto, precio in productos:
        print(f"Producto: {producto} Precio: {precio}")


def imprimir_productos_entre(productos):
    for tuplas in productos:
        if tuplas[1] >= 10 and tuplas[1] <= 15:
            print(
                f"Con precio entre 10 y 15; Producto {tuplas[0]} Precio: {tuplas[1]}")


productos = cargar_productos()
listar_productos(productos)
imprimir_productos_entre(productos)
