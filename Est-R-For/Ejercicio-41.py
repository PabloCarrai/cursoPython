"""  
Escribir un programa que solicite
por teclado 10 notas de estudiantes
y nos informe cuantos tienen 
notas mayores o iguales a 7 y cuantos
menores
"""

cNmSiete = 0
cNmeSiete = 0
for i in range(10):
    nota = int(input("Ingrese Nota "))
    if (nota >= 7):
        cNmSiete = cNmSiete+1
    else:
        cNmeSiete = cNmeSiete+1
print("Cantidad de notas Mayores/Iguales a 7")
print(cNmSiete)
print("Cantidad de notas Menores a 7")
print(cNmeSiete)
