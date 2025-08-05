"""  
Confaccionar un programa que permita 
cargar un numero entero positivo de hasta 
tres cifras y muestre un mensaje indicando 
si tiene 1, 2 o 3 cifras. 
Mostrar un mensaje de error si el numero
es mayor
"""

numero = int(input("Ingrese un numero "))
if (numero > 999):
    print("Numero erroneo(Mas de 3 Cifras)")
    print(numero)
else:
    if (numero > 99):
        print("Numero de 3 Cifras")
        print(numero)
    else:
        if (numero > 9):
            print("Numero de 2 Cifras")
            print(numero)
        else:
            print("Numero de 1 Cifra")
            print(numero)
