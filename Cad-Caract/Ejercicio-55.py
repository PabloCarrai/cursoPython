"""  
Realizar la carga por teclado del nombre, 
edad y altura de dos personas. Mostrar por pantalla
el nombre de la persona con mayor altura
"""

#   Pido los datos 2 veces para comparar
nombre = input("Ingrese Nombre ")
edad = int(input("Ingrese Edad "))
altura = float(input("Ingrese altura "))
nombre1 = input("Ingrese Nombre ")
edad1 = int(input("Ingrese Edad "))
altura1 = float(input("Ingrese altura "))
if altura > altura1:  # comparo la altura
    print("El mas alto es ")
    print(nombre)
    print(altura)
else:
    print("El mas alto es ")
    print(nombre1)
    print(altura1)
