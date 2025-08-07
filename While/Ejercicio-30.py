"""  
Desarrollar un programa que permita la carga
de 10 valores por teclado y nos muestre
posteriormente la suma de los valores
ingresados y su promedio
"""

suma = 0
x = 1
while (x <= 10):
    valorIngresado = int(input("Ingrese un valor "))
    x = x+1
    suma = suma+valorIngresado
promedio = suma/10
print("La suma da ")
print(suma)
print("El promedio da ")
print(promedio)
