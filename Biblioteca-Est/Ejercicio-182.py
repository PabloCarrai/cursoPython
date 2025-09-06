""" 
Calcular el factorial de un numero ingresado por teclado. 
El factorial de un numero es la cantidad que resulta de la
multiplicacion de determinano numero natural por todos los numeros
naturales que le anteceden escluyendo el cero. Por ejemplo el
factorial de 4 es 24 que resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial
sino hay que importar dicha funcionalidad del modulo math. 
El modulo math tiene una funcionn llamada factorial que recibe
como parametro un entero del que necesitamos que nos retorne
el factorial. Solo importar la funcionalidad del modulo math
de la biblioteca estandar de python
"""

from math import factorial as f

valor = int(input("Valor? "))
print(f"El factorial del numero {valor} es {f(valor)}")
