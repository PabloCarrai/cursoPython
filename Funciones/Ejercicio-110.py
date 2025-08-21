"""
Desarrollar un programa con dos funciones.
La primer solicite el ingreso de un entero
y muestre el cuadrado de dicho valor.
La segunda solicite la carga de dos valores
y muestre el producto del mismo. Llamar desde
el bloque del programa principal a ambas funciones
"""


def cuadradoValor():
    print("------------------------------------")
    valor = int(input("Ingrese un Valor "))
    print("El cuadrado de dicho valor es ")
    print(valor*valor)
    print("------------------------------------")


def cargaDosValores():
    print("------------------------------------")
    valor = int(input("Valor? "))
    valor1 = int(input("valor?  "))
    print("El producto de ambos es ")
    print(valor*valor1)
    print("------------------------------------")


cuadradoValor()
cargaDosValores()
