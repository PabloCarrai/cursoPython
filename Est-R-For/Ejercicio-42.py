"""  
Escribir un programa que lea 10
numeros enteros y luego muestre
cuantos valores ingresados fueron
multiplos de 3 y cuantos de 5
"""
cmTres = 0
cmCinco = 0
for numero in range(10):
    valor = int(input("Ingrese un valor   "))
    if (valor % 3 == 0):
        cmTres = cmTres+1
    if (valor % 5 == 0):
        cmCinco = cmCinco+1
print("Multiplos de 3")
print(cmTres)
print("Multiplos de 5")
print(cmCinco)
