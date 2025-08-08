""" 
Codificar un programa que lea n numeros
enteros y calcule la cantidad de valores
mayores o iguales a 1000(n se carga por teclado)
"""
#   Aca cuento los valores la cantidad de valores mayores iguales a 1000
cValoresMmil = 0
#   Ingreso la cantidad de valores a cargar
cvaloresCargar = int(input("Cuantos valores va a ingresar? "))
#   El for que hace todo
for x in range(cvaloresCargar):
    valor = int(input("Ingrese el Valor  "))
    if valor >= 1000:
        cValoresMmil = cValoresMmil+1
#   Muestro el resultado
print("Cantidad de valores mayores/iguales a 1000")
print(cValoresMmil)
