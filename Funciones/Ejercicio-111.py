""" 
Desarrollar un programa que solicite la carga de tres valores
y muestre el menor. desde el bloque principal llamar 2 veces
dicha funcion (sin usar estructura repetitiva. )
"""


def menorDeTres():
    valor = int(input("Valor?"))
    valor1 = int(input("Valor?"))
    valor2 = int(input("Valor?"))
    if ((valor < valor1) and (valor < valor2)):
        print("-----------")
        print("El menor es ")
        print(valor)
        print("-----------")
    else:
        if ((valor1 < valor) and (valor1 < valor2)):
            print("-----------")
            print("El menor es ")
            print(valor1)
            print("-----------")
        else:
            if ((valor2 < valor) and (valor2 < valor1)):
                print("-----------")
                print("El menor es ")
                print(valor2)
                print("-----------")


menorDeTres()
menorDeTres()
