""" 
Confeccionar un programa que solicite la carga de un valor
entero por teclado y luego nos muestre la raiz cuadrada del
numero y el valor elevado al cubo. 
"""

#   Creamos un alia de sqrt como raiz y pow como elevar del modulo math
from math import sqrt as raiz, pow as elevar


valor = int(input("Valor? "))
valor1 = raiz(valor)
valor2 = elevar(valor, 3)
print(f"Raiz cuadrada {valor1}")
print(f"Cubo {valor2}")
