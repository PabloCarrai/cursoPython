""" 
Escribir un programa en el cual dada una lista de tres valores
numericos distintos se calcule e informe su rango de variacion
(mostrar el mayor y el menor)
"""
numero = int(input("Ingrese Primer Numero "))
numero1 = int(input("Ingrese Segundo Numero "))
numero2 = int(input("Ingrese Tercer Numero "))
maximo = 0
minimo = 0

if ((numero > numero1) and (numero > numero2)):
    maximo = numero
else:
    if ((numero1 > numero) and (numero1 > numero2)):
        maximo = numero1
    else:
        if ((numero2 > numero) and (numero2 > numero1)):
            maximo = numero2


if ((numero < numero1) and (numero < numero2)):
    minimo = numero
else:
    if ((numero1 < numero) and (numero1 < numero2)):
        minimo = numero1
    else:
        if ((numero2 < numero) and (numero2 < numero1)):
            minimo = numero2

print("Maximo")
print(maximo)
print("Minimo")
print(minimo)
