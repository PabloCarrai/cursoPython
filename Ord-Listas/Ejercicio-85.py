sueldos = []
for i in range(5):
    valor = int(input("Valor? "))
    sueldos.append(valor)
print("Lista Original")
print(sueldos)
#   Metodo de la burbuja
for k in range(4):
    for x in range(4-k):
        if (sueldos[x] > sueldos[x+1]):
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
print("Lista Ordenada")
print(sueldos)
