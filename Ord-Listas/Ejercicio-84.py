"""  
Generar un ordenamiento en una lista ubicando 
el elemento mayor al final de la misma. 
"""

sueldos = []
for x in range(5):
    valor = int(input("Valor?  "))
    sueldos.append(valor)

print("Lista original")
print(sueldos)
#   Metodo de la burbuja
for x in range(4):
    if (sueldos[x] > sueldos[x+1]):
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux
print("Ultimo elemento ordenado")
print(sueldos)
