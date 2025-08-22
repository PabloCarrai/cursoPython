"""
Confeccionar una funcion que reciba
tres enteros y nos muestre el mayor de ellos
La carga de los valores hacerlo por teclado
en otra funcion
"""


def devolverMayor(v, v1, v2):
    if ((v > v1) and (v > v2)):
        print("-----------")
        print("Mayor ")
        print(v)
        print("-----------")
    else:
        if ((v1 > v) and (v1 > v2)):
            print("-----------")
            print("Mayor ")
            print(v1)
            print("-----------")
        else:
            if ((v2 > v) and (v2 > v1)):
                print("-----------")
                print("Mayor ")
                print(v2)
                print("-----------")


def cargarValores():
    valor = int(input("Valor? "))
    valor1 = int(input("Valor? "))
    valor2 = int(input("Valor? "))
    devolverMayor(valor, valor1, valor2)


cargarValores()
