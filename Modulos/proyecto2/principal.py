"""  
Confeccionar un modulo que implemente dos funciones,
una que retorne el mayor de dos enteros y otra que retorne
el menor de dos enteros. 
En el modulo principal importar solo la funcion que retorne el mayor
luego cargar dos enteros y mostrar el mayor de ellos
Crear una carpeta llamada proyecto2 y dentro de la misma
crear dos modulos
"""
from dosfundiones import mayordedos as mayor

valor = int(input("Primer Valor? "))
valor1 = int(input("Segundo Valor?  "))
print(f"El mayor es {mayor(valor, valor1)}")
