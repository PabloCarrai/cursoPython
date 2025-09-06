"""  
Confeccionar un programa que solicite la carga de un valor
entero por teclado y luego nos muestre la raiz cuadrada del
numero y el valor elevado al cubo. 
Para resolver este problema utilizaremos dos funcionalidades
que nos provee el modulo math de la biblioteca estandar de python
from math import sqrt,pow

"""

#   Importo solo dos funcionalidades de math
from math import sqrt, pow


valor = int(input("Valor? "))
valor1 = sqrt(valor)
valor2 = pow(valor, 3)
print(f"Raiz cuadrada {valor1}")
print(f"Cubo {valor2}")
