""" 
Crear y cargad dos listas con los nombres de
5 productos en una y sus respectivos precios
en otra. Definir dos listas paralelas. 
Mostrar cuantos productos tienen un precio
mayor al primer producto ingresado
"""
#   Contador de productos > a primer producto
contadorProductosMayor = 0
#   Listas para productos y sus precios
productos = []
precios = []
#   Hago la carga y agrego a las listas paralelas
for i in range(5):
    producto = input("Producto?  ")
    precio = float(input("Precio?  "))
    productos.append(producto)
    precios.append(precio)
#   Tomo el primer precio
precioMayor = precios[0]
#   Recorro la lista viendo si algun producto tiene precio > a precio 1 producto
for i in range(5):
    if (precios[i] > precioMayor):
        #   Acumulo el contador
        contadorProductosMayor = contadorProductosMayor+1
        #   Muestro el que cumple con ser mayor al precio del primer producto
        print("Producto Cuyo Precio Es Mayor al Primer Producto")
        print(productos[i])
        print("Precio ")
        print(precios[i])
#   Si hay algun producto con mayor precio muestro esto sino no
if contadorProductosMayor > 0:
    print("Cantidad de Producto Cuyo Precio Es Mayor al Primer Producto")
    print(contadorProductosMayor)
