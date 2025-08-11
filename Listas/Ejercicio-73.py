"""  
Almacenar en una lista los sueldos
(valores float) de 5 operarios. 
Imprimir la lista y el promedio
de los sueldos
"""
acumuladorSueldos = 0
listaSueldos = []
#   Cargo la lista con los sueldos
for i in range(5):
    sueldo = float(input("Sueldo?   "))
    listaSueldos.append(sueldo)

#   Totalizo los sueldos en un acumulador
for i in range(5):
    acumuladorSueldos = acumuladorSueldos+listaSueldos[i]
promedio = acumuladorSueldos/5
#   Imprimo lo que me pide el ejercicio
print("La lista de sueldos es ")
print(listaSueldos)
print("El promedio es ")
print(promedio)
