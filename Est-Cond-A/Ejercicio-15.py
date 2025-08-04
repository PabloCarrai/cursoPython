""" 
Se cargan por teclado tres numeros distintos. 
Mostrar por pantalla el mayor de ellos
"""
numero = int(input("Ingrese Primer Numero "))
numero1 = int(input("Ingrese Segundo Numero "))
numero2 = int(input("Ingrese Tercer Numero "))
print("El mayor numero es ")
if (numero > numero1):
    if (numero > numero2):
        print(numero)
if (numero1 > numero):
    if (numero1 > numero2):
        print(numero1)
if (numero2 > numero):
    if (numero2 > numero1):
        print(numero2)
