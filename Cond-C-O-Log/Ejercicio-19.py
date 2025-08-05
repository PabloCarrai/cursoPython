"""  
Confeccionar un programa que lea por teclado
tres numeros enteros distintos y nos muestre
el mayor 
"""
numero = int(input("Ingrese Primer Numero "))
numero1 = int(input("Ingrese Segundo Numero "))
numero2 = int(input("Ingrese Tercer Numero "))
print("El mayor es ")
if ((numero > numero1) and (numero > numero2)):
    print(numero)
else:
    if ((numero1 > numero2)):
        print(numero1)
    else:
        print(numero2)
