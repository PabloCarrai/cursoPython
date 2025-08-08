""" 
Se realiza la carga de 10 valores
enteros por teclado. Se desea conocer
a) Cantidad de valores negativos
b) Cantidad de valores positivos
c) Cantidad de multiplos de 15
d) El valor acumulado de los numeros que son pares
"""
cVNegativos = 0
cVPositivos = 0
cMquince = 0
cVPTotales = 0
for w in range(10):
    valor = int(input("Ingrese un valor    "))
    if (valor % 2 == 0):
        cVPTotales = cVPTotales+valor
    if (valor % 15 == 0):
        print("Multiplo de 15 ")
        cMquince = cMquince+1
    if (valor > 0):
        print("Valor Positivo ")
        cVPositivos = cVPositivos+1
    if (valor < 0):
        print("Valor Negativo  ")
        cVNegativos = cVNegativos+1
print("Cantidad Valores Positivos")
print(cVPositivos)
print("Cantidad Valores Negativos")
print(cVNegativos)
print("Cantidad de Multiplos de 15")
print(cMquince)
print("Cantidad Acumulada en valores Pares")
print(cVPTotales)
