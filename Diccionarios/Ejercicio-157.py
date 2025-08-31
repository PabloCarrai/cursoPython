""" 
Crear un diccionario que permita almacenar
5 articulos. Utilizar como clave el nombre del
producto y como valor el precio del mismo. 
Desarrollar ademas las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los articulos con presio superio a 100
"""


def cargar():
    productos = {}
    for i in range(5):
        producto = input("Producto? ")
        precio = int(input("Precio?  "))
        #   A traves de clave=precio se genera la carga
        productos[producto] = precio
    return productos


def imprimir(productos):
    print("Productos")
    for nombre in productos:
        print(nombre, productos[nombre])


def imprimir_mayores(productos):
    print("Mayores a 100 ")
    #   Consigo las claves y las guardo en nombre
    for nombre in productos:
        #   y con cada clave sobre producto averiguo su valor y pregunto si es mas grande que 100
        if productos[nombre] > 100:
            #   Si sucede lo imprimo
            print(nombre)


productos = cargar()
imprimir(productos)
imprimir_mayores(productos)
