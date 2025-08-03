""" 
Realizar un programa que solicite la carga por teclado de dos numeros.
Si el primero es mayor al segundo, informar su suma y diferencia. 
En caso contrario informar el producto y la division del primero
respecto al segundo 
"""
numero = int(input("Ingrese un numero "))
numero1 = int(input("Ingrese otro numero "))
suma = numero+numero1
resta = numero-numero1
producto = numero*numero1
div = numero/numero1
if numero > numero1:
    print("La suma de ambos es")
    print(suma)
    print("La resta entre ambos es")
    print(resta)
else:
    print("El producto entre ambos es ")
    print(producto)
    print("La division entre ambos es ")
    print(div)
