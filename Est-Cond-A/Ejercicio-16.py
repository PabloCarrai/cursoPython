""" 
Se ingresa por teclado un valor entero. 
Mostrar una leyenda que indique si el numero es
Positivo, negativo o nulo
"""
numero = int(input("Ingrese un Numero  "))
if (numero > 0):
    print("Numero Positivo")
    print(numero)
else:
    if (numero < 0):
        print("Numero Negativo")
        print(numero)
    else:
        print("Numero Neutro")
        print(numero)
