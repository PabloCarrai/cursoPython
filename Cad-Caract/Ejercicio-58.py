"""
Realizar la carga de dos nombre distintos.
Mostrar por pantalla luego ordenados
en forma alfabetica
"""
nombre = input("Ingrese un nombre   ")
nombre1 = input("Ingrese un nombre  ")
print("Listado ordenado alfabeticamente  ")
if nombre < nombre1:
    print(nombre)
    print(nombre1)
else:
    print(nombre1)
    print(nombre)
