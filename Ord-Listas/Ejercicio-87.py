"""  
Solicitar por teclado la cantidad de empleados
que tiene la empresa. Crear y cargar una lista
con todos los sueldos de dichos empleados. 
Imprimir la lista de sueldos ordenados de 
menor a mayo
"""

sueldos = []

cuantosEmpleados = int(input("Cuantos Empleados son?   "))
for i in range(cuantosEmpleados):
    valor = int(input("Sueldo?   "))
    sueldos.append(valor)
print("Lista con sueldos Generada  ")
print(sueldos)

for i in range(len(sueldos)-1):
    for x in range(len(sueldos)-1-i):
        if (sueldos[x] > sueldos[x+1]):
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
print("Lista Ordenada")
print(sueldos)
