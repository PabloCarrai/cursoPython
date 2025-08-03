""" 
Realizar un programa que solicite ingresar 
dos numeros distintos y muestre
por pantalla el mayor de ellos
"""
numero = int(input("Ingrese un numero "))
numero1 = int(input("Ingrese otro numero "))
if numero > numero1:
    print("El primer numero es mayor que el segundo ")
    print(numero)
else:
    print("El segundo numero es mayor al primero ")
    print(numero1)
