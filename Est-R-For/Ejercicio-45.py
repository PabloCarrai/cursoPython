""" 
Desarrollar un programa que solicite la carga
de 10 numeros e imprimir la suma de los ultimos
5 valores ingresados. 
"""
cUltimosCinco = 0
for i in range(10):
    valor = int(input("Ingrese un Valor "))
    if i > 4:
        cUltimosCinco = cUltimosCinco+valor
print("La suma de los ultimos valores es ")
print(cUltimosCinco)
