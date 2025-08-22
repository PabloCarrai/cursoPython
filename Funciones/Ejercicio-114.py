"""  
Desarrollar un programa que permita ingresar
el lado de un cuadrado. Luego preguntar si quiere
calcular y mostrar su perimetro o su superficio
"""


def calcularPerimetroCuadrado(lado):
    print("-------------------------------")
    print("El perimetro del cuadrado es ")
    print("-------------------------------")
    print(lado*4)
    print("-------------------------------")


def calcularSuperficieCuadrado(lado):
    print("-------------------------------")
    print("El superficie del cuadrado es ")
    print("-------------------------------")
    print(lado*lado)
    print("-------------------------------")


def queCalculamos():
    print("Que desea calcular?")
    print("El perimetro del cuadrado(1)")
    print("La superficie del cuadrado(2)")
    desicion = int(input("1 o 2?"))
    lado = int(input("Lado?"))
    if (desicion == 1):
        calcularPerimetroCuadrado(lado)
    else:
        if (desicion == 2):
            calcularSuperficieCuadrado(lado)


queCalculamos()
