""" 
Escribir un programa que solicite el ingreso de 10 notas
de alumnos y nos informe cuantas tienen notas
mayores o iguales a 7 y cuantas menores. 
"""
x = 1
nmayoresaSiete = 0
nmenoresaSiete = 0
while (x <= 10):
    x = x+1
    nota = int(input("Ingrese una nota "))
    if (nota >= 7):
        nmayoresaSiete = nmayoresaSiete+1
    else:
        nmenoresaSiete = nmenoresaSiete+1
print("Notas mayores/iguales a 7")
print(nmayoresaSiete)
print("Notas menores a 7")
print(nmenoresaSiete)
