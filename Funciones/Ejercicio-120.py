""" 
Elaborar una funcion que reciba tres enteros
y nos retorne el valor promedio de los mismo
"""


def promedio_tres(v, v1, v2):
    return (v+v1+v2)/3


valor = int(input("Valor?   "))
valor1 = int(input("Valor?   "))
valor2 = int(input("Valor?   "))
print(promedio_tres(valor, valor1, valor2))
