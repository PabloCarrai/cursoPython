"""    
Se ingresan un conjunto de n alturas de personas por teclado. 
Mostrar la altura promedio de las personas. 
"""
x = 1
tAlturas = 0
cIngresos = int(input("Cuantas alturas vas a ingresar? "))
while (x <= cIngresos):
    x = x+1
    altura = float(input("Ingrese la altura "))
    tAlturas = tAlturas+altura
promedio = tAlturas/cIngresos
print("Promedio de alturas ")
print(promedio)
