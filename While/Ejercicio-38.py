"""  
Desarrollar un programa que permita
cargar n numeros enteros y luego 
nos informe cuantos valores fueron
pares y cuantos inpares.
Emplear el operador % en la condicion
"""

cNPar = 0
cNInPar = 0
aux = 1
cNIngresar = int(input("Cuantos valores vas a ingresar? "))
while (aux <= cNIngresar):
    aux = aux+1
    valor = int(input("Ingresa un valor "))
    if (valor % 2 == 0):
        print("Numero Par")
        cNPar = cNPar+1
    else:
        print("Numero InPar")
        cNInPar = cNInPar+1

print("Cantidad de numeros Pares ")
print(cNPar)
print("Cantidad de numeros InPares ")
print(cNInPar)
