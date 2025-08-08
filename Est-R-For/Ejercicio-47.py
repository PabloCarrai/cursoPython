""" 
Confeccionar un programa que permita ingresar
un valor del 1 al 10 y nos muestre la tabla de
multiplicar del mismo(los primeros 12 terminos)
"""
valor = int(input("Ingrese un valor "))
for i in range(1, 13):
    print(valor*i)
