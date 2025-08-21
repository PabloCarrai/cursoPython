""" 
Confeccionar una aplicacion que solicite la carga de dos valores enteros. 
Y muestre su suma. Repetir la cargar e impresion de la suma 5 veces. 
Mostrar una linea separadora despues de cada vez que cargamos dos 
valores y su suma
"""


def cargaDosValores():
    print("-------------------------------------------")
    print("Bienvenido a la suma de dos valores")
    print("-------------------------------------------")
    valor = int(input("Primer Valor?   "))
    valor1 = int(input("Segundo Valor?   "))
    print("-------------------------------------------")
    print("La suma de ambos valores es ")
    print("-------------------------------------------")
    print(valor+valor1)
    print("-------------------------------------------")


for x in range(5):
    cargaDosValores()
