"""  
Desarrollar un programa que permita
la carga de 10 valores por teclado. 
Y nos muestre posteriormente la suma
de los valores ingresados y su promedio
"""
acumulador = 0
for i in range(10):
    valor = int(input("Ingrese un valor "))
    acumulador = acumulador+valor
promedio = acumulador/10
print("El total es ")
print(acumulador)
print("Promedio ")
print(promedio)
